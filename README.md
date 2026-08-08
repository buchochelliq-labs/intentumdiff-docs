# IntentumDiff documentation

Source for the IntentumDiff documentation site.

**Live site:** https://buchochelliq-labs.github.io/intentumdiff-docs/

## Why this repo exists separately

The docs describe a product made of several repositories — the Rust core, the Python package,
the VS Code extension and 78 language parsers. No single one of them is the right home, so the
docs live alongside all of them rather than inside one.

## The rule that matters

**Every Python example in these docs is executed in CI against a real installed wheel, and its
documented output is compared with what it actually prints.** Every link is checked.

IntentumDiff 0.0.1 shipped a README whose headline example raised `NameError`, and an error
message pointing at a domain that did not exist. Both were obvious within a minute of trying
them, and neither was caught, because nothing ever ran the docs.

So: a doc that claims an output it cannot produce fails the build.

```bash
pip install -r requirements-docs.txt
mkdocs serve                        # preview at http://127.0.0.1:8000
python scripts/verify_examples.py   # run the examples (needs the engine installed)
```

## Contributing

Docs target the release-candidate branch like everything else in the estate — see the
`intentumdiff-release` skill. If something here is wrong, that is a bug worth reporting on its
own; docs rot is why 0.0.1 had to be pulled.
