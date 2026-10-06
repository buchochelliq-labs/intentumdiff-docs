Write before.yaml 'server:\n  host: localhost\n'
Write after.yaml 'server:\n  host: prod.example.com\n'
Write policy.yaml 'guardrails:\n  protected:\n    - id: server-host\n      language: yaml\n      path: server.host\n      severity: immutable\n      message: Server host changed\n'
Set Size 110x24
Set TypingDelay 15ms
Set Title "IntentumDiff 0.0.2b1 · installed wheel"
Set Caption "Protected server.host changes; strict review fails"
Type "intentumdiff --no-banner file before.yaml after.yaml --guardrails-policy policy.yaml --guardrails-strict"
Enter
Wait /Immutable semantic guardrail violation detected/
Sleep 1200ms
Screenshot guardrail
