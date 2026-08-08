# Python library and CLI

```bash
pip install intentumdiff-python
```

Requires **Python ≥ 3.12**. The wheel is self-contained — see [Getting started](getting-started.md).

!!! note "Two names, one package"

    The **distribution** is `intentumdiff-python` (what you `pip install`). The **import
    package** is `intentumdiff` (what you `import`). This mismatch is normal on PyPI, and it is
    why the install command and the import line do not look alike.

## The library

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

The third argument is a **filename**, not a path that must exist. It is how the engine picks a
parser, so the extension matters even for source held in memory.

## The CLI

The package installs an `intentumdiff` command. It is also runnable as a module, which is
useful when several interpreters are on your `PATH`:

```bash
python -m intentumdiff --help
```

Both forms are equivalent.

### Commands

| Command | What it does |
|---|---|
| `file` | Diff two local files |
| `git` | Diff files or commits in a git repository |
| `github-pr` | Parse a GitHub pull request URL into a review target |
| `gist-diff` | Parse a GitHub Gist URL into a diff target |
| `assets` | Perceptual diffs for non-text assets such as images |
| `guardrails` | Check protected-config guardrail policy |
| `index` | Pre-index a git repository to warm caches |
| `cache` | Inspect or manage the local cache database |
| `diagnostics` | Query local diagnostics |
| `live-server` | Start the editor-facing LiveServer JSON protocol |

Every command takes `--help`. Run it — the help text is generated from the code and is
therefore always correct, which is more than can be promised for any table in a document.

```bash
intentumdiff file --help
```

### Two files

```bash
intentumdiff file old.py new.py
```

### Inside a git repository

```bash
intentumdiff git --help
```

`git` is the command most reviewers spend their time in: it compares against a ref rather than
requiring you to materialise two files yourself.

### The live server

`live-server` speaks the JSON protocol the VS Code extension uses. You are unlikely to run it
by hand, but it is a documented, stable surface if you want to build your own front end.

## Suppressing the banner

The CLI prints a banner when attached to a terminal. In scripts and CI:

```bash
intentumdiff --no-banner file old.py new.py
```
