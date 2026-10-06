# VS Code review workflow

This 16-second desktop recording shows a real Python `return 2 → return 3` edit:
CodeLens beside the source, the native VS Code diff, then the custom review and source evidence.
The changed return value independently warrants a behavioural change.

<video controls muted playsinline preload="metadata" poster="../../assets/vscode/current/source-codelens.png" style="width:100%;height:auto">
  <source src="../../assets/vscode/current/workflow.mp4" type="video/mp4">
  Your browser cannot play this video.
  <a href="../../assets/vscode/current/workflow.mp4">Download the MP4</a>.
</video>

The clip is a real desktop recording from the installed-VSIX acceptance run, not a generated
animation. It contains no CLI footage. It demonstrates navigation between these three views;
it does not demonstrate staging, revert, loading transitions or every review tab.

See [capabilities](../../vscode.md) and [candidate provenance](../../vscode-evidence.md).

Video SHA-256: `ead87ac46456142052f5fd21176abe97b1abc2139d6c8cf1cd435d6c8a1b71c9`.
