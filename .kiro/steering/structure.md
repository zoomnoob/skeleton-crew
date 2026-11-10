# Structure

```
.kiro/steering/   this folder — committed, and never listed in .gitignore
.kiro/specs/      one subfolder per feature spec (requirements / design / tasks)
word-frequency-cli/   application 1, self-contained
pomodoro-web/         application 2, self-contained
```

Rules that keep the two apps independent:

1. No imports across app folders.
2. No shared `package.json`, `requirements.txt` or build script at the root.
3. A change to one app never requires running the other app's tests.
