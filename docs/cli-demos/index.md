# CLI in action

These recordings run the installed `0.0.2b1` wheel from Python #97. Each command uses the
Rust semantic engine. The main terminal diff panels and change tables use Rust-owned
**rs-rich 0.0.9**; Python supplies terminal settings and writes the returned text.

The four videos were captured with **rs-rich-record 0.0.3**. They are real terminal sessions,
not reconstructed result mockups. The separate guardrail report, errors and other CLI
surfaces still use existing presentation paths; rs-rich adoption is not yet complete.

Install the runtime using [Getting started](../getting-started.md). `--no-banner` keeps each
example focused on its result. The command remains usable without that option.

## Meaningful edit

The assigned integer changes from 1 to 2. Expect one modification, not style-only output. The command exits 0.

```bash
intentumdiff --no-banner string 'value = 1' 'value = 2' --lang python
```

<video controls muted playsinline preload="metadata" poster="../assets/cli/current/meaningful.png" style="width:100%;height:auto">
  <source src="../assets/cli/current/meaningful.mp4" type="video/mp4">
  <a href="../assets/cli/current/meaningful.mp4">Download the meaningful edit video</a>.
</video>

[Recorder tape](../assets/cli/current/meaningful.tape)

## Formatting only

Only spaces around the assignment change. Expect a style-only result with zero semantic changes. The command exits 0.

```bash
intentumdiff --no-banner string 'value=1' 'value = 1' --lang python
```

<video controls muted playsinline preload="metadata" poster="../assets/cli/current/style.png" style="width:100%;height:auto">
  <source src="../assets/cli/current/style.mp4" type="video/mp4">
  <a href="../assets/cli/current/style.mp4">Download the formatting only video</a>.
</video>

[Recorder tape](../assets/cli/current/style.tape)

## Actionable error

With these files absent, the command names the missing input and exits 1. Create the file or correct the path before retrying. It does not substitute an empty successful diff.

```bash
intentumdiff --no-banner file missing-before.py missing-after.py
```

<video controls muted playsinline preload="metadata" poster="../assets/cli/current/error.png" style="width:100%;height:auto">
  <source src="../assets/cli/current/error.mp4" type="video/mp4">
  <a href="../assets/cli/current/error.mp4">Download the actionable error video</a>.
</video>

[Recorder tape](../assets/cli/current/error.tape)

## Protected configuration review

The protected server.host value changes from localhost to prod.example.com. Expect an IMMUTABLE violation, the actual source modification, and exit 2. The policy decision is owned by Rust.

```bash
intentumdiff --no-banner file before.yaml after.yaml --guardrails-policy policy.yaml --guardrails-strict
```

<video controls muted playsinline preload="metadata" poster="../assets/cli/current/guardrail.png" style="width:100%;height:auto">
  <source src="../assets/cli/current/guardrail.mp4" type="video/mp4">
  <a href="../assets/cli/current/guardrail.mp4">Download the protected configuration review video</a>.
</video>

[Recorder tape](../assets/cli/current/guardrail.tape)

Create `before.yaml`:

```yaml
server:
  host: localhost
```

Create `after.yaml`:

```yaml
server:
  host: prod.example.com
```

Create `policy.yaml`:

```yaml
guardrails:
  protected:
    - id: server-host
      language: yaml
      path: server.host
      severity: immutable
      message: Server host changed
```

## Candidate and recorder provenance

| Item | Identity |
|---|---|
| Wheel SHA-256 | `5d4dff214aa8fdb17ccc88f3b787880044c9f944bf335918f28c5d3e15c237f5` |
| Python tested merge commit | `9d1d150e3cdbaa8fef754ef916f8e1b3eb6e297d` |
| Python PR head | `256a9d9a8bcca48cb512503e1ac3024b51b4bc29` |
| Rust core | `74eeb809ab663df91c3b3fd501240dc96d925f60` |
| Wheel artifact | `11407195708` |
| Recorder crate | `rs-rich-record = 0.0.3` from crates.io |
| Recorder wrapper source | core `6cf7fb9e1a7b447c06e09826e7dc4f2c0260fc0e`, `tools/record-demo` |

[Four-platform wheel verification run](https://github.com/buchochelliq-labs/intentumdiff-python/actions/runs/37448070098)
passed. These recordings are Linux terminal evidence; they are not screenshots of Windows
or macOS. Stills were visually inspected and all four video durations verified.
[Full public provenance and media checksums](../assets/cli/current/provenance.json) includes
recorder binary and lockfile hashes.

## Feedback from using rs-rich and rs-rich-record

- Shared Rust panels and tables clearly distinguish a meaningful change from formatting-only output.
- Literal source labels survive without being interpreted as markup. Narrow wrapping is tested in core.
- Recorder tapes can wait for real output and export stills plus MP4 from the same session.
- The recorder uses an isolated workspace and environment. `Write` steps make the guardrail tape
  self-contained; assuming the caller’s working directory initially produced a missing-file error.
- Rounded panel corners look less complete in the raster export than in the terminal text grid.
  A box-drawing glyph regression set would help distinguish recorder font/rendering behaviour.
- Recording a real application makes partial adoption visible: the standalone guardrail report
  still uses the existing Python formatter. These examples do not claim every CLI surface is migrated.
