#!/usr/bin/env python3
"""Turn a Reel script into frame accurate timing for Remotion.

Usage:
  python3 make_timing.py script.json [--audio-dir DIR] [--out timing.json]

script.json:
  {"fps": 30, "speed": 1.25, "gap": 0.12, "min_scene": 1.2,
   "scenes": [{"id": "s1", "text": "...", "audio": "1.ogg"}, {"id": "s2", "text": "..."}]}

If a scene has an "audio" file that exists in --audio-dir, its real duration (via ffprobe)
divided by "speed" is used. Otherwise the duration is estimated from the text length.
The output lists every scene with start and duration in frames, plus per word timings.
"""
import argparse, json, os, re, subprocess, sys

CHARS_PER_SEC = 13.0  # normal speaking pace for Uzbek, non space characters (estimate)


def probe(path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", path],
            capture_output=True, text=True, timeout=30, check=True).stdout.strip()
        return float(out)
    except Exception:
        return None


def words_of(text):
    return [w for w in re.split(r"\s+", text.strip()) if w]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--audio-dir", default=".")
    ap.add_argument("--out", default="timing.json")
    a = ap.parse_args()

    with open(a.script, encoding="utf-8") as f:
        cfg = json.load(f)
    fps = int(cfg.get("fps", 30))
    speed = float(cfg.get("speed", 1.25))
    gap = float(cfg.get("gap", 0.12))
    min_scene = float(cfg.get("min_scene", 1.2))
    tail = float(cfg.get("tail", 0.4))

    scenes, cursor, estimated = [], 0, 0
    for i, sc in enumerate(cfg["scenes"]):
        text = sc.get("text", "")
        ws = words_of(text)
        dur, source = None, "estimate"
        audio = sc.get("audio")
        if audio:
            p = os.path.join(a.audio_dir, audio)
            if os.path.isfile(p):
                d = probe(p)
                if d:
                    dur, source = d / speed, "audio"
        if dur is None:
            chars = sum(len(w) for w in ws)
            dur = max(chars / (CHARS_PER_SEC * speed), 0.0)
            estimated += 1
        dur = max(dur, min_scene if not sc.get("allow_short") else dur)
        dur += tail if i == len(cfg["scenes"]) - 1 else gap
        frames = max(int(round(dur * fps)), 1)

        total_chars = sum(len(w) for w in ws) or 1
        speak_frames = max(frames - int(round(gap * fps)), 1)
        t, wlist = 0, []
        for w in ws:
            wf = max(int(round(speak_frames * len(w) / total_chars)), 1)
            wlist.append({"word": w, "start": cursor + t, "end": cursor + min(t + wf, frames)})
            t += wf
        scenes.append({"id": sc.get("id", f"s{i+1}"), "text": text, "audio": audio,
                       "source": source, "start": cursor, "duration": frames,
                       "words": wlist})
        cursor += frames

    result = {"fps": fps, "speed": speed, "totalFrames": cursor,
              "totalSeconds": round(cursor / fps, 2), "scenes": scenes}
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    msg = f"{len(scenes)} scenes, {result['totalSeconds']} s, {cursor} frames -> {a.out}"
    if estimated:
        msg += f" ({estimated} scene(s) estimated from text, no audio found)"
    print(msg)


if __name__ == "__main__":
    sys.exit(main())
