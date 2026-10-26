---
name: design-skill-router
description: "Master skill for ALL design work. Use it first whenever the request touches design, UX, UI, branding, landing pages, dashboards, design systems, user research, design thinking, prototyping, usability, critique, accessibility, typography, color, layout, motion, or turning a design into video. It reads the situation, picks the right skills out of the 138+ installed design skills, loads only the best one to three, merges their rules into one brief, resolves conflicts between them, and delivers. Trigger even when the user does not name a skill, says only 'make it look good', 'design this', 'review my UI', 'what should I do first', or asks which skill to use."
---

# Design Skill Router

One entry point for every design task. The user should never have to remember which skill exists. This skill decides which skills apply, in what order, and how to combine the best parts into one result.

Do not load many skills. Loading too many dilutes the work and creates contradictions. The target is **one primary skill, up to two supporting skills**, loaded with the Skill tool.

## The protocol

Run these five steps every time. Keep the thinking short and the output focused.

### 1. Classify the request

Decide two things from the user's words and any attached files:

- **Phase** the work is in: Discover, Define, Ideate and decide, Design, Critique, Build and ship, or Communicate.
- **Artifact**: a page, a screen, a component, a system, a study, a plan, a document, a video.

If the user only says something vague like "make it better", look at the artifact first (read the file, view the screenshot) and infer the phase. Ask at most one question, and only when the phase cannot be inferred. If the user is not present to answer, state the assumption in one line and continue.

### 2. Choose skills using the routing table

Match the phase and artifact to the table below. Pick the **primary** skill by the most specific match, never the most general. Add at most two **supporting** skills that cover a gap the primary leaves open.

### 3. Load them

Call the Skill tool for each chosen skill. Read each one fully before using it. If a skill is missing from the session, read its entry in `references/catalog.md` and apply the same idea from your own knowledge, and tell the user that skill was not loaded.

### 4. Merge into one brief

Before producing anything, write a short internal brief:

- Goal, audience, constraint, and the single outcome that defines success.
- The non negotiable rules pulled from each loaded skill (hard values, required sections, forbidden patterns).
- The conflicts between them and how each is resolved (see precedence below).

Then produce the work from that one brief, not from several skills in parallel.

### 5. Verify and report

Finish with a verification pass using one critique or audit skill that fits the artifact (for example `critique-visual-hierarchy`, `accessibility-audit`, `heuristic-evaluation`, `web-design-guidelines`). Fix what it finds. End with one line naming the skills used, for example: "Used: landing-page-design, design-taste-frontend, accessibility-audit."

## Routing table

### Build a new page or site
| Situation | Primary | Supporting |
|---|---|---|
| Landing page, marketing site, waitlist, offer page | `landing-page-design` | `design-taste-frontend` for art direction, `web-typography`, `color-system` |
| Portfolio, one pager, "make it look award level or not AI made" | `design-taste-frontend` | `hallmark` as the alternative voice, `landing-page-design` for structure and copy |
| Brand new page where the user names Hallmark | `hallmark` | `web-design-guidelines` |
| Generic build with no strong direction | `frontend-design` | `impeccable` |

### Build or improve product UI
| Situation | Primary | Supporting |
|---|---|---|
| Dashboard, admin panel, SaaS app, settings, data screens | `interface-design` | `impeccable`, `data-visualization` |
| Polish, simplify, harden, animate, make bolder or quieter, UX copy | `impeccable` | the matching `critique-*` skill |
| Generate a full design system from a project description | `ui-ux-pro-max` | `design-system`, `color-system` |
| Native iPhone or iPad app | `ios-hig-design` | `platform-conventions`, `microinteractions` |
| Hard to understand, "users keep making mistakes" | `design-everyday-things` | `ux-heuristics`, `error-handling-ux` |

### Discover (research)
| Situation | Primary | Supporting |
|---|---|---|
| Prepare or run customer interviews | `mom-test` | `interview-script`, `summarize-interview` |
| Make sense of many notes or sessions | `affinity-diagram` | `qual-quant-triangulation` |
| Who is the user | `user-persona` | `empathy-map`, `jobs-to-be-done` |
| End to end experience, pain points | `journey-map` | `experience-map`, `service-blueprint` |
| Surveys, diary studies, card sorts | `survey-design`, `diary-study-plan`, `card-sort-analysis` | `research-repository` |
| Weekly discovery habit, opportunity trees | `continuous-discovery` | `inspired-product` |
| Read funnels and retention as a designer | `behavioural-analytics` | `metrics-definition` |

### Define (frame the problem)
| Situation | Primary | Supporting |
|---|---|---|
| Kickoff, scope, success criteria | `design-brief` | `design-principles` |
| Long term direction | `north-star-vision` | `opportunity-framework` |
| What to work on first | `opportunity-framework` | `competitive-analysis`, `business-design` |
| Structure of content and navigation | `information-architecture` | `navigation-patterns`, `content-strategy` |
| Align people, defend a decision | `stakeholder-alignment` | `design-negotiation`, `design-rationale` |

### Ideate and decide (design thinking core)
| Situation | Primary | Supporting |
|---|---|---|
| High stakes idea, validate before building | `design-sprint` | `design-sprint-plan`, `mom-test` |
| Lightweight, hypothesis driven design with a team | `lean-ux` | `continuous-discovery` |
| Only one direction exists, avoid refining it by default | `parallel-concepts` | `concept-selection` |
| Several directions alive, one must win | `concept-selection` | `a-b-test-design` |
| Open ended thinking across strategy, UX, brand and growth | `thinkfull` | the phase skill that follows |

### Prototype and test
| Situation | Primary | Supporting |
|---|---|---|
| Decide how much to prototype | `prototype-strategy` | `wireframe-spec`, `user-flow-diagram` |
| Plan a usability session | `usability-test-plan` | `test-scenario`, `click-test-plan` |
| Expert review without participants | `heuristic-evaluation` | `ux-heuristics` |
| Test with assistive technology users | `accessibility-test-plan` | `accessibility-audit` |
| Quantitative experiment | `a-b-test-design` | `metrics-definition` |

### Interaction and psychology
| Situation | Primary | Supporting |
|---|---|---|
| Forms | `form-design` | `error-handling-ux`, `feedback-patterns` |
| First run, activation | `onboarding-design` | `hooked-ux`, `zeigarnik-effect` |
| Waiting, empty, failure, confirmation | `loading-states`, `error-handling-ux`, `feedback-patterns` | `doherty-threshold` |
| Small details, UI feels dead | `microinteractions` | `micro-interaction-spec`, `animation-principles` |
| Too many options, memory limits, target size | `hicks-law`, `millers-law`, `fitts-law` | `jakobs-law` |
| Habit loops, retention | `hooked-ux` | `peak-end-rule`, `serial-position-effect` |
| Search, gestures, voice | `search-ux`, `gesture-patterns`, `conversational-ux` | `state-machine` |

### Visual fundamentals
| Situation | Primary | Supporting |
|---|---|---|
| Attention lands in the wrong place | `visual-hierarchy` | `critique-visual-hierarchy`, `von-restorff-effect` |
| Grid, spacing, breakpoints | `layout-grid` | `spacing-system`, `responsive-design` |
| Type | `typography-scale` | `web-typography`, `readable-measure` |
| Color, dark mode, charts | `color-system` | `dark-mode-design`, `data-visualization` |
| Grouping and depth | `law-of-proximity` | `law-of-common-region`, `law-of-similarity`, `law-of-figure-ground` |
| Icons, illustration | `icon-system`, `illustration-style` | `brand` |
| Brand voice and identity | `brand` | `critique-brand-consistency` |

### Critique and audit an existing design
| Situation | Primary | Supporting |
|---|---|---|
| Whole screen feels off | `impeccable` | `critique-composition` |
| One dimension: hierarchy, color, type, density, affordance, brand | the matching `critique-*` skill | `heuristic-evaluation` |
| Accessibility | `accessibility-audit` | `critique-color` |
| Team review session | `design-critique` | `design-review-process` |
| Drift and inconsistency | `design-debt-audit` | `design-token-audit` |
| Fast web guidelines check | `web-design-guidelines` | `impeccable` |
| Why a polished design still tests badly | `aesthetic-usability` | `interfaces-that-feel` |

### Systems, handoff, operations
| Situation | Primary | Supporting |
|---|---|---|
| Tokens and theming | `design-token` | `theming-system`, `naming-convention` |
| Components and patterns | `component-spec` | `pattern-library`, `documentation-template` |
| Governance and adoption | `design-system-governance` | `design-system-adoption` |
| Engineering handoff and QA | `handoff-spec` | `design-qa-checklist` |
| Motion rules for the product | `motion-system` | `animation-principles` |
| Localization | `localization-design` | `ux-writing` |

### Communicate
| Situation | Primary | Supporting |
|---|---|---|
| Portfolio story | `case-study` | `presentation-deck` |
| Stakeholder deck, impact report | `presentation-deck` | `design-impact-reporting` |
| Interface words | `ux-writing` | `content-strategy` |
| Poster, static artwork | `canvas-design` | `theme-factory` |

### Motion and video
| Situation | Primary | Supporting |
|---|---|---|
| Animate a finished design into a loop, MP4 or GIF | `design-to-motion` | `motion-system` |
| Instagram Reel, short video, any "make a video about..." | `reels-director` | none needed |

## Precedence when skills disagree

Overlapping skills will sometimes give opposite instructions. Resolve in this order:

1. **The user's explicit words, brand, and existing files.** Always win.
2. **Safety and access.** Accessibility (contrast, focus, motion reduction, tap size) is never traded away for style.
3. **The primary skill's hard rules** (required sections, token values, forbidden patterns).
4. **Supporting skills' guidance**, used for ideas, checks, and details the primary does not cover.
5. **Your own taste**, only to fill remaining gaps.

Known overlaps and the rule for each:

- `landing-page-design` and `design-taste-frontend` and `hallmark` all style web pages. Let `landing-page-design` own structure, copy, and the token values (type scale, spacing table, radii). Let `design-taste-frontend` or `hallmark` contribute composition, palette direction, and imagery ideas only. Never apply two house styles at once.
- `impeccable` and `interface-design` both cover product UI. Use `interface-design` to design and `impeccable` to polish and audit.
- `design-system` and `ui-ux-pro-max` generate systems quickly. If the user already has tokens, use `design-token` and `design-token-audit` instead and do not invent a second system.
- `brand-guidelines` applies Anthropic's own look. Use it only when the user asks for Anthropic styling, never as a general brand skill.
- Research skills overlap by design. Prefer the one named in the table and follow its own "for X use Y" pointers.

## Making the result the best of the best

When more than one skill applies, do not simply concatenate their advice.

1. Pull out each skill's strongest, most specific rules and the checklist items that would be embarrassing to miss.
2. Drop generic advice that every skill repeats.
3. Where two skills offer different solutions to the same problem, pick the one that best fits this user's audience and constraint, and say why in one line.
4. Prefer concrete values over adjectives: a named type scale, an exact spacing step, a stated contrast ratio.
5. Run the verification pass from step 5 and keep fixing until the critique has no high severity findings.

## Personal defaults for this user

- When the user writes in Uzbek, reply in Uzbek and address them with the formal "siz".
- Do not use pink in any output. Use green as the accent instead.

## When no skill fits

Search `references/catalog.md` by keyword (for example with Grep). If nothing fits, do the work from sound design principles, say that no installed skill covered it, and offer to create one with the skill-creator skill.

## Maintaining the catalog

`references/catalog.md` lists every installed design skill with its purpose. When a skill is added or removed, regenerate the catalog from the skills folder so routing stays accurate.
