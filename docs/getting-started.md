# Getting started

There is **one** thing to install. Everything else comes with it.

!!! warning "Python 3.12 or newer is required"

    IntentumDiff requires **Python ≥ 3.12**. On an older interpreter `pip` reports:

    ```
    ERROR: Could not find a version that satisfies the requirement intentumdiff-python
    ```

    That message means *your Python is too old*, not that the package is missing.
    Check with `python --version` before anything else.

## 1. Install the engine

```bash
pip install intentumdiff-python
```

That is the whole installation. The wheel is self-contained — roughly 22 MB — and already
includes:

| Component | What it is |
|---|---|
| The Rust core | The engine that parses, matches and classifies changes |
| 78 language parsers | WebAssembly components, one per language |
| The Python API and CLI | The `intentumdiff` command and the `intentumdiff` module |

There is **no second download**. You do not install the Rust core separately, and nothing is
fetched from the network the first time you run it.

Check it worked:

```bash
intentumdiff --version
```

## 2. Try it on two files

```bash
intentumdiff file old.py new.py
```

Or from Python:

```python
from intentumdiff import SemanticDiffer

old = "def greet(name):\n    return 'hi ' + name\n"
new = "def greet(name):\n    if not name:\n        return None\n    return 'hi ' + name\n"

diff = SemanticDiffer().diff_strings(old, new, "example.py")
for change in diff.changes:
    print(change.change_type, change.description)
```

```text
ChangeType.ADDITION Insert -> if_statement('if_statement')
```

A textual diff would tell you three lines were added. IntentumDiff tells you a **guard clause
was introduced** — which is the thing a reviewer actually needs to know.

## 3. Install the VS Code extension

Search for **IntentumDiff** in the Extensions view, or install from the
[Marketplace](https://marketplace.visualstudio.com/) / [Open VSX](https://open-vsx.org/).

!!! important "The extension needs the engine from step 1"

    The extension is a thin front end. It runs the `intentumdiff` command, so **step 1 is a
    prerequisite** — installing the extension on its own is not enough.

    If `intentumdiff` is not on your `PATH`, point the extension at it directly:

    ```json
    { "intentumdiff.executable": "/full/path/to/intentumdiff" }
    ```

    This setting is machine-scoped, so a workspace cannot override it — a repository you
    clone cannot make your editor run an arbitrary binary.

Once both are installed, open a diff the way you normally would. IntentumDiff adds intent
annotations above each change rather than replacing the editor you already know.

## Where to go next

- [VS Code extension](vscode.md) — what the annotations mean and how to configure them
- [Python library and CLI](python.md) — the full API and command surface
- [How it works](concepts.md) — why the results differ from a line diff
- [Troubleshooting](troubleshooting.md) — if any of the above did not behave as described
