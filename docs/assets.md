# Diffing images

A line diff of a PNG tells you the bytes changed. That is true and useless.

Re-export an image from a different tool and every byte moves while the picture is identical.
Change one icon in a sprite sheet and almost no bytes move while something visible broke.
Neither case is answerable by comparing bytes, so most review tools show "binary file differs"
and leave you to open both in another application.

IntentumDiff compares images **perceptually** — what the picture looks like, not how it was
encoded.

## Comparison modes

Because no single view answers every question, the review surface offers several and lets you
switch between them:

| Mode | Best for |
|---|---|
| **Side by side** | The overview — what am I looking at |
| **Swipe** | Dragging a divider across the two, for alignment and layout shifts |
| **Onion skin** | Fading between them, for gradual differences like colour grading |
| **Difference** | Only what changed, everything unchanged going dark |
| **Blink** | Alternating rapidly — the eye is extremely good at catching what jumps |

## Finding the change

- **Hotspots** highlight regions that differ most, so a single altered icon in a large sprite
  sheet is found for you rather than hunted
- **Change lasso** outlines changed regions directly on the image
- **Histograms** compare colour distribution, which catches global changes — a re-encode, a
  colour-profile shift, a compression-quality drop — that are easy to miss by eye

## Why this catches real problems

The cases that reach production are usually the invisible ones:

- An asset re-exported at lower quality. Looks fine at review size, blocky at full size —
  the histogram shows it immediately
- A colour profile change that shifts every pixel slightly. Byte diff: everything changed.
  Perceptual diff: a uniform shift, visible in one glance at the difference view
- One sprite altered in a large sheet. Byte diff: a small change somewhere. Hotspots: exactly
  where

## From the command line

```bash
intentumdiff assets --help
```

## Where the work happens

All image artifacts are produced by the **Rust engine**, not the editor. The review surface
displays what the engine computed and does no image processing of its own, so the CLI and the
extension give identical results — and a comparison is reproducible outside the editor.
