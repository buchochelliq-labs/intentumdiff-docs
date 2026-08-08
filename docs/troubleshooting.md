# Troubleshooting

## `pip install` fails with "Could not find a version that satisfies the requirement"

Almost always an interpreter that is too old. IntentumDiff requires **Python ≥ 3.12**.

```bash
python --version
```

On 3.11 or earlier, pip finds no compatible wheel and reports the requirement as unsatisfiable,
which reads like a missing package but is not one. Install a newer Python, or create a
virtual environment with one:

```bash
py -3.12 -m venv .venv
```

The same message appears if your platform has no published wheel. IntentumDiff publishes
wheels for Windows (x64 and ARM64), macOS and Linux.

## The VS Code extension does nothing / cannot find the engine

The extension is a front end for the `intentumdiff` command. If the engine is not installed,
or not on your `PATH`, the extension has nothing to talk to.

1. Confirm the engine is installed:

    ```bash
    intentumdiff --version
    ```

2. If that works in your shell but not in VS Code, VS Code is using a different `PATH` —
   common when the engine lives in a virtual environment. Point the extension at it directly:

    ```json
    { "intentumdiff.executable": "/full/path/to/intentumdiff" }
    ```

3. Check the output panel: **View → Output → IntentumDiff**. The launch line records which
   executable was chosen and why.

!!! info "Why this setting is machine-scoped"

    `intentumdiff.executable` is deliberately machine-scoped, so a workspace `settings.json`
    cannot change which binary runs. Otherwise cloning a repository could make your editor
    execute an arbitrary program.

## Many "Failed to catalog parser plugin" errors

A bug in **0.0.1** — see [the full account](release-0-0-1.md). Fixed since. The published package omitted its own distribution name from
its first-party trust list, so all 78 bundled parsers were rejected as untrusted third-party
code. Results were still produced, but every run printed a wall of errors.

Upgrade:

```bash
pip install --upgrade intentumdiff-python
```

If you see this on a current version, please
[open an issue](https://github.com/buchochelliq-labs/intentumdiff-python/issues) — it means the
trust list is wrong again and we want to know immediately.

## `python -m intentumdiff` fails on 0.0.1

Also fixed. 0.0.1 shipped without a `__main__.py`, so only the console script worked. Upgrade,
or use the `intentumdiff` command directly.

## Windows Defender or a browser warns about the extension download

We have investigated this and found no malicious content: the extension VSIX contains **no
native binaries at all**, and a full Defender signature scan reports it clean.

The likely cause is a reputation warning — new, low-download-count files trigger
"this file isn't commonly downloaded and may be dangerous" regardless of content.

If you hit this, we would genuinely like the detail, because it is the only way to confirm it:
open **Windows Security → Protection history**, find the entry, and report the exact **threat
name** on
[this issue](https://github.com/buchochelliq-labs/intentumdiff-vscode/issues/20).

## A diff falls back to line-level results

If a language's parser cannot load, IntentumDiff degrades to a token-level comparison rather
than failing. You still get a diff, but not semantic categories.

Check the output panel for parser load errors and include them in a bug report.

## Something else

Please [open an issue](https://github.com/buchochelliq-labs/intentumdiff-python/issues) and
include your OS, `python --version`, and `intentumdiff --version`. If the docs told you
something that turned out not to be true, that is a bug in the docs and worth reporting on its
own.
