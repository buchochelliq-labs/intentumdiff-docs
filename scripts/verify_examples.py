"""Run every Python example in the docs and check its documented output is real.

# Why this exists

IntentumDiff 0.0.1 shipped a README whose headline example raised `NameError` — it was a
fragment nobody had ever executed. The docs also linked to a domain that did not exist.

Prose cannot be unit tested, but examples can, and examples are the part readers actually
copy. So every ```python block here is extracted, executed against a **real installed
wheel**, and its output compared with the ```text block that follows it.

A doc that claims an output it cannot produce fails the build. That is the whole idea.

Usage:
    python scripts/verify_examples.py          # check every page
    python scripts/verify_examples.py docs/getting-started.md
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

# A python block, optionally followed by a text block holding its expected output. The text
# block is what makes this a test rather than a smoke run.
PAIR = re.compile(
    r"```python\n(?P<code>.*?)```\n+(?:```text\n(?P<want>.*?)```)?",
    re.DOTALL,
)


def examples(page: Path):
    body = page.read_text(encoding="utf-8")
    for m in PAIR.finditer(body):
        line = body[: m.start()].count("\n") + 1
        yield line, m.group("code"), m.group("want")


def run(code: str) -> tuple[int, str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "example.py"
        script.write_text(code, encoding="utf-8")
        p = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=180,
        )
        return p.returncode, p.stdout, p.stderr


def main() -> int:
    pages = [Path(a) for a in sys.argv[1:]] or sorted(DOCS.rglob("*.md"))
    failures: list[str] = []
    checked = 0

    for page in pages:
        for line, code, want in examples(page):
            checked += 1
            where = f"{page.as_posix()}:{line}"
            rc, out, err = run(code)

            if rc != 0:
                failures.append(f"{where} raised:\n      {err.strip().splitlines()[-1][:200]}")
                continue

            # Stderr is part of the user experience. 0.0.1 returned correct results while
            # printing 69 error lines, and exit code alone called that a pass.
            noisy = [ln for ln in err.splitlines() if ln.strip()]
            if noisy:
                failures.append(f"{where} wrote to stderr:\n      {noisy[0][:200]}")
                continue

            if want is None:
                print(f"  RUN   {where}  (no documented output to compare)")
                continue

            if out.strip() != want.strip():
                failures.append(
                    f"{where} output does not match the documented result\n"
                    f"      documented: {want.strip()[:160]!r}\n"
                    f"      actual:     {out.strip()[:160]!r}"
                )
                continue

            print(f"  PASS  {where}")

    print(f"\n  {checked} example(s) checked")
    if failures:
        print(f"  {len(failures)} FAILED\n")
        for f in failures:
            print(f"    - {f}")
        return 1
    print("  all examples produce their documented output")
    return 0


if __name__ == "__main__":
    sys.exit(main())
