# Diffing images

A line diff of a PNG tells you the bytes changed. That is true and useless.

Re-export an image from a different tool and every byte moves while the picture is identical.
Change one icon in a sprite sheet and almost no bytes move while something visible broke.
Neither case is answerable by comparing bytes, so most review tools show "binary file differs"
and leave you to open both in another application.

IntentumDiff compares images **perceptually** — what the picture looks like, not how it was
encoded.

## A worked example

Two renders of the same scene. One thing changed — the name on the hull.

<figure markdown>
![The same seascape, hull reading SEA BREEZE](assets/perceptual/sailboat-before.png)
<figcaption>Before — the hull reads <code>SEA BREEZE</code></figcaption>
</figure>

<figure markdown>
![The same seascape, hull reading IntentumDiff](assets/perceptual/sailboat-after.png)
<figcaption>After — the hull reads <code>IntentumDiff</code></figcaption>
</figure>

Both files were re-encoded, so **every byte differs**. A byte comparison reports "binary file
differs" and stops there — technically true, and useless. It cannot tell you whether the sky
changed, the boat moved, or someone edited two characters.

Here is what the engine reports:

```text
changed pixels : 10,418  (0.6510% of the image)
dimensions     : 1600x1000 -> 1600x1000  (unchanged)
```

And the overlay marks *only* the lettering — not the sea, the sun, the clouds or the sand:

<figure markdown>
![Overlay highlighting only the hull lettering in red](assets/perceptual/overlay.png)
<figcaption>Overlay — changed regions in red, everything unchanged left alone</figcaption>
</figure>

The heatmap answers the follow-up question, "is that the only place?", at a glance:

<figure markdown>
![Heatmap showing a single hotspot at the hull](assets/perceptual/heatmap.png)
<figcaption>Heatmap — a single hotspot, so nothing else moved</figcaption>
</figure>

"0.15% of pixels changed, all of them here" is something you can act on. "The bytes differ" is
not.

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
