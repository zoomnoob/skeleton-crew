# Skeleton Crew

Two independent applications that share nothing but this repository.

| Folder | App | Stack |
| --- | --- | --- |
| [`word-frequency-cli/`](word-frequency-cli) | Count the most frequent words in a text file | Python 3, stdlib only |
| [`pomodoro-web/`](pomodoro-web) | 25/5 focus timer that runs in the browser | HTML + CSS + vanilla JS |

## Layout

```
.
├── .kiro/                  # committed on purpose, never gitignored
│   ├── steering/           # product / tech / structure guidance
│   └── specs/              # one subfolder per feature spec
├── word-frequency-cli/     # application 1
└── pomodoro-web/           # application 2
```

Each app folder is self-contained: its own README, its own entrypoint, no
shared code, no workspace manifest at the root. Delete either folder and the
other still runs.

## License

[MIT](LICENSE)
