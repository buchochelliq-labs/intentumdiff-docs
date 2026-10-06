# Makefile

[All languages](../gallery.md)

These real terminal captures use a historical development build. They are not current release certification; independent output review and current installed-wheel scenario checks remain pending.

## Overview

This worked example compares `Makefile`. Advertised filename extensions: `Makefile`, `GNUmakefile`, `.mk`, `.make`.

## What changes

Change compiler optimization from -O2 to -O3 in build recipe; add clean target removing app.

## Before

````text
CC = gcc

build: main.c
	$(CC) -O2 -o app main.c
````

## After

````text
CC = gcc

build: main.c
	$(CC) -O3 -o app main.c

clean:
	rm -f app
````

## Things to know

- clean is not declared .PHONY, so an existing file named clean can suppress that recipe.

## Recorded output

![Actual Makefile terminal capture](meaningful-change.svg)

Recorded from a real native CLI through rs-rich-record. A refactoring label does not prove equivalent behavior. [Build identities](../provenance.md).

## Scenario coverage

| Scenario | Status |
|---|---|
| Meaningful edit | Source example reviewed; output captured; independent result certification pending |
| Unchanged content | Not yet certified for this candidate |
| Populate / clear a file | Not yet certified for this candidate |
| Add / delete an entity | Not yet certified for this candidate |
| Rename a symbol | Not yet certified for this candidate |
| Move / reorder code | Not yet certified for this candidate |
| Formatting only | Not yet certified for this candidate |
| Git file rename / move | Not yet certified for this candidate |
| Mixed move and edit | Not yet certified for this candidate |
| Invalid syntax / actionable error | Not yet certified for this candidate |
| Guardrail review | Not yet certified for this candidate |

## Try it

Save the two source blocks as separate files with the shown extension, then compare them:

```bash
intentumdiff file before/Makefile after/Makefile
```

The installed Python wheel includes its parser components. The native CLI requires a component directory. Compare the result with the source change described above; agreement between APIs alone is not proof of correctness.
