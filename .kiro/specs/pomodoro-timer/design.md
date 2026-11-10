# Design: pomodoro-timer

## Files

| File | Responsibility |
| --- | --- |
| `pomodoro-web/index.html` | three text nodes (`#phase`, `#clock`) and two buttons |
| `pomodoro-web/styles.css` | centred layout, tabular numerals so digits do not jitter |
| `pomodoro-web/app.js` | state machine and rendering |

## State

```
remaining : seconds left in the current phase
breaking  : false = Focus, true = Break
ticker    : null | setInterval handle
```

`tick()` decrements `remaining`; when it drops below zero it flips `breaking`
and reloads the constant (`FOCUS` 1500 s / `BREAK` 300 s), then calls `render()`.
`render()` is the only writer of the DOM, which keeps AC-1 to AC-3 testable by
reading one function.

## Decisions

- No `localStorage`: a refresh restarting the cycle is acceptable behaviour and
  removes the only state that could leak between sessions.
- No framework: AC-4 requires zero coupling with the other app, and a bundler
  would add a root-level toolchain we deliberately do not have.
