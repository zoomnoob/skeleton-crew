# Tech

- `word-frequency-cli/`: Python 3.9+ standard library only (`argparse`, `re`,
  `collections.Counter`). Entrypoint `main.py`, no packaging metadata needed to
  run it.
- `pomodoro-web/`: static files (`index.html`, `styles.css`, `app.js`). No
  framework, no bundler, no network calls.

There is deliberately no root-level toolchain. Each app is launched from inside
its own folder.
