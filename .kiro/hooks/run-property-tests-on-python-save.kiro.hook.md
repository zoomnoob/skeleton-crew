---
name: run-property-tests-on-python-save
description: Runs the property-based test suite whenever a Python file under word-frequency-cli/ is saved.
category: Save File
event: fileSaved
fileMatch: word-frequency-cli/**/*.py
---

When this hook fires, run:

```bash
cd word-frequency-cli && python3 -m unittest -v test_properties
```

If a property fails, report the counterexample printed by the test and stop.
Do not "fix" the property by loosening the invariant — the property comes from
`.kiro/specs/word-frequency/requirements.md`, so a failing invariant means the
implementation is wrong.
