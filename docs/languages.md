# Languages

**78 parsers ship inside the wheel.** There is nothing extra to download and no
language pack to enable — installing `intentumdiff-python` installs all of them.

If a file's language is not recognised, IntentumDiff degrades to a token-level comparison
rather than failing: you still get a diff, just without semantic categories.

## Supported

- `abap`
- `adf`
- `asciidoc`
- `asm`
- `assemblyscript`
- `astro`
- `bash`
- `clojure`
- `cmake`
- `cpp`
- `csharp`
- `css`
- `dart`
- `databricks`
- `dax`
- `dbt_enricher`
- `dbt_schema`
- `dbt_sql`
- `delphi`
- `dockerfile`
- `elixir`
- `freebasic`
- `generic`
- `gitignore`
- `go`
- `gomod`
- `graphql`
- `groovy`
- `haskell`
- `html`
- `html_renderer`
- `index_engine`
- `ini`
- `java`
- `js_ts`
- `json`
- `kotlin`
- `latex`
- `llm_renderer`
- `lua`
- `make`
- `markdown`
- `mdx`
- `ocaml`
- `odin`
- `patch_renderer`
- `perl`
- `php`
- `plsql`
- `plugin_sdk`
- `po`
- `postscript`
- `powershell`
- `proto`
- `puppet`
- `python`
- `qsharp`
- `r`
- `reasonml`
- `ruby`
- `rust`
- `sas`
- `scala`
- `scss`
- `sql`
- `squirrel`
- `svelte`
- `swift`
- `terminal_renderer`
- `terraform`
- `toml`
- `tsql`
- `vbnet`
- `vue`
- `wat`
- `xml`
- `yaml`
- `zig`

## Adding a language

Each parser is an independent WebAssembly component built against a published SDK, so a
new language does not require a change to the engine. See the
[plugin SDK](https://github.com/buchochelliq-labs/intentumdiff-plugin-sdk).
