# CMake

[All languages](../gallery.md)

These real terminal captures use a historical development build. They are not current release certification; independent output review and current installed-wheel scenario checks remain pending.

## Overview

This worked example compares `CMakeLists.txt`. Advertised filename extensions: `CMakeLists.txt`, `.cmake`.

## What changes

Add utils.c to the app executable source list; retain project and m library linkage.

## Before

````text
project(demo)

add_executable(app main.c)

target_link_libraries(app m)
````

## After

````text
project(demo)

add_executable(app main.c utils.c)

target_link_libraries(app m)
````

## Things to know

- Referenced files and build environment are absent; source-list change affects the build.

## Recorded output

![Actual CMake terminal capture](meaningful-change.svg)

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
intentumdiff file before/CMakeLists.txt after/CMakeLists.txt
```

The installed Python wheel includes its parser components. The native CLI requires a component directory. Compare the result with the source change described above; agreement between APIs alone is not proof of correctness.
