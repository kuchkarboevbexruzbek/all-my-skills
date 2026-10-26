# Montage and render

## Technical spec

- Canvas 1080 x 1920 (9:16), 30 fps.
- Export MP4, H.264 video, AAC audio, 44.1 or 48 kHz, constant frame rate.
- Length 20 to 35 seconds by default. Instagram allows longer Reels, but shorter finishes more often.
- Cover frame: the first frame doubles as the cover in many views, so it must show the hook text clearly.

## Safe zones (approximate)

Instagram overlays its interface on top of the video: account name and caption at the bottom, action buttons on the right, header at the top. Keep all important text and faces inside the safe area:

- Top: leave about 12 percent empty.
- Bottom: leave about 22 percent empty.
- Right edge: leave about 12 percent empty.
- Left edge: keep a margin of at least 6 percent.

These are working values, not official ones. If the user reports text being covered, widen the margins.

## Shot table (deliverable of Stage 3)

Produce a table like this for the whole Reel:

| # | Time | Visual | Motion | On screen text | Voice line | Sound | Transition |
|---|---|---|---|---|---|---|---|
| 1 | 0.0 to 2.2 | What is on screen | Camera or element move | 3 to 5 words | Line 1 | Whoosh, hit | Cut |

Rules for the table:

- Every scene has exactly one visual idea and at most one piece of on screen text.
- No scene longer than 4 seconds without a visible change.
- Name the asset source for each scene: `code`, `gemini-image`, `character`, or `stock`.
- Note which scenes carry the hook, the turn, and the call to action.

## Visual formats

Pick the format by topic, then stay consistent within the Reel.

1. **Illustrated sticker collage explainer.** Cut-out images with a white outline, slight paper shadow, quick zooms and pops, handwritten feeling text. Best for lists, myths, habits, careers.
2. **Presenter cut-out with animated infographics.** A cut-out character on a clean background with charts, counters and text building around them. Best for explaining a number or a process.
3. **3D low poly dialogue sketch.** Three.js scene with a human and two AI robot characters, short everyday dialogues, expressive voices. Best for relatable humor and "everyday situation" topics.
4. **Pure kinetic typography.** Words as the main visual with icons and shapes. Best for the instant draft when no images exist yet, and for strong one line statements.

## Draft mode: building from code

When the user has not supplied images or voice, build a complete draft anyway:

- Scene visuals from React and SVG: shapes, icons drawn as SVG paths, big numbers counting up, simple charts, phone and browser mockups drawn with divs, emoji only if the style allows.
- Motion from Remotion primitives: `spring` for pops and settles, `interpolate` for slides and fades, staggered delays of 3 to 6 frames between elements.
- Subtitles from `timing.json` words.
- Placeholder voice track: none. Do not generate or fake a voice. Time the scenes from the estimate and say so.

The draft must already look intentional. Do not ship gray boxes.

## Final mode: user assets

- **Images** (usually generated in Gemini): keep the style cut-out with a white outline. If an image has a background, remove it with a tool or mask. Place each image on its scene with a slow push in, a pop in, or a slide, not static.
- **Voice** (the user's own recordings or ElevenLabs files, numbered by line): one file per scene. Play each at the chosen speed (default 1.25x) using `playbackRate` on the Remotion `Audio` component, and set the scene length from the real duration divided by that speed.
- **Music**: low under the voice, about 12 to 18 percent of voice level, ducked while speaking. Use only royalty free or original tracks, and say which one. If none is available, skip music rather than guess.

## Timing pipeline

1. Write `script.json`:

```json
{
  "fps": 30,
  "speed": 1.25,
  "gap": 0.12,
  "scenes": [
    {"id": "s1", "text": "Sun'iy intellekt ishingizni olib qo'yadimi?", "audio": "1.ogg"},
    {"id": "s2", "text": "Keling, bosqichma bosqich ko'ramiz."}
  ]
}
```

2. Run `python3 scripts/make_timing.py script.json --audio-dir assets/voice --out timing.json`.
3. In Remotion, load `timing.json` and use `calculateMetadata` to set the total `durationInFrames` from it, so the composition adapts when real audio replaces estimates.
4. Each scene is a `Sequence` with `from` and `durationInFrames` taken from the file. Words for subtitles come from each scene's `words` list, with start and end frames.

## Subtitles

- Word by word reveal, the current word highlighted in the green accent.
- Two lines at most, 3 to 6 words visible at once.
- Large type, bold weight, high contrast with a solid dark or outlined backing so it reads over any image. Use a font with full Uzbek Latin coverage (Poppins or Manrope).
- Uzbek apostrophes: use the proper letters (o', g' with the same apostrophe as the source script) and check they render.
- Position in the lower middle of the safe area, never over a face.

## Remotion project structure

```
reel/
  package.json
  src/
    index.ts          registerRoot
    Root.tsx          Composition with calculateMetadata
    Reel.tsx          maps timing.json to Sequences
    scenes/           one component per scene or reusable scene types
    components/       Subtitle, PopImage, KineticText, Background, Character
    data/timing.json
  public/
    images/  voice/  music/
```

Commands:

```
npm install
npx remotion render src/index.ts Reel out/reel.mp4 --codec=h264 --crf=20
```

If `remotion-mcp` tools are available, call `read_me` and the rule tools (animations, sequencing, text animations, timing, transitions, trimming) before writing scene code.

Performance: keep images at the size they are displayed, avoid very heavy blur and shadows on many layers, and render at a concurrency the machine can handle.

## Motion rules

- Everything that enters decelerates into place. No linear motion for UI style elements.
- Pop in with a small overshoot, 8 to 12 frames. Slide and fade in 10 to 16 frames.
- Hold each key element long enough to read: at least 0.8 seconds for 3 words, longer for more.
- Use transitions sparingly: hard cuts for rhythm, one whip or zoom for a big moment.
- Sound effects: a short hit on each text pop, a whoosh on each big move, a soft riser before the turn. Keep them quiet.

## Quality gate (run before delivering)

Extract frames and inspect:

```
ffmpeg -y -i out/reel.mp4 -vf "select=eq(n\,0)+eq(n\,150)+eq(n\,300)" -vsync 0 qa_%02d.png
```

Then check every item:

- [ ] 1080 x 1920, 30 fps, H.264, audio present (if final), duration as planned. Confirm with ffprobe.
- [ ] First frame shows the hook text.
- [ ] Nothing important in the unsafe zones.
- [ ] No overlapping elements. No text over faces.
- [ ] Subtitles readable and synced with the voice.
- [ ] No moving progress bar or other decorative clutter unless the user asked for it.
- [ ] Voice and music levels balanced, no clipping.
- [ ] Every fact in the script is sourced.
- [ ] Accent color is green. No pink.
- [ ] The last second leads naturally back to the first or ends on the call to action.

If something fails, fix it and re-render. Do not deliver a video that fails a gate item without saying which one.
