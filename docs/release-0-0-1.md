# 0.0.1 was broken, and we pulled it

IntentumDiff 0.0.1 was published on 4 August 2026 and withdrawn shortly afterwards.

If you were one of the people who installed it in that window: it did not work properly, you
were right to think something was wrong, and we're sorry. You spent time on something that
should not have shipped.

!!! warning "0.0.1 has been withdrawn"

    The VS Code extension has been removed from the Marketplace and Open VSX, and the Python
    package has been yanked from PyPI. `pip` will not install it, and you should not pin to
    it. There is no working release available right now; the next one will be `0.0.2b1`.

## What was wrong

| What you saw | What was actually happening |
|---|---|
| A wall of `Failed to catalog parser plugin` errors on every single run | The package left its own name off its internal trust list, so all 78 bundled parsers were rejected as untrusted third-party code |
| `python -m intentumdiff` failed outright | There was no `__main__.py`. Only the `intentumdiff` command worked |
| An error message pointed at documentation that did not exist | It linked to a domain that had never been registered |
| The README's headline example raised `NameError` | It was a code fragment, not a runnable program. Nobody had ever executed it |

Every one of these was visible within a minute of installing the package.

## Why we did not catch it

Every check was green when we shipped. That was the problem, not an excuse.

The tests proved the code compiled and behaved correctly **in a source checkout**. Nothing in
our CI ever installed the published wheel and used it the way the README says to — and three
of the four faults above exist *only* in an installed package. The fourth was in the
documentation, which nothing executed at all.

We were measuring the wrong thing and mistook a green board for a working product.

## What has changed

Not intentions — checks that fail the build:

- **The published artefact is installed into a clean environment and used before any
  release.** Install, import, console script, `python -m`, a real diff, and — the check that
  would have caught the worst of it — **stderr must be empty**. 0.0.1 returned correct results
  while printing 69 errors, and exit code 0 called that a success.
- **Every code example in this documentation is executed in CI** against a real installed
  wheel, and its output compared with what the page claims. An example that cannot run now
  fails the build.
- **Every link is checked**, so documentation cannot point at a page that does not exist.
- **Releases start as betas.** A version number without a beta marker is a claim of stability,
  and that claim should follow use, not precede it.

## Where things stand

The next release will be `0.0.2b1`. It will not go out until the checks above pass against the
real artefact rather than a source checkout.

If you hit something that does not behave the way these docs describe — including the docs
themselves — please [tell us](https://github.com/buchochelliq-labs/intentumdiff-python/issues).
That is exactly the kind of report that would have caught this one.
