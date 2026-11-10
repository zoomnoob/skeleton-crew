# Requirements: pomodoro-timer

## Introduction

A browser-only focus timer. No account, no server, no storage beyond the page.

## Requirements

### AC-1 Focus cycle

- **When** the page loads, **the timer** shall show `25:00` with phase `Focus`.
- **When** the user presses Start, **the timer** shall count down once per second.

### AC-2 Phase switch

- **When** `Focus` reaches zero, **the timer** shall switch to `Break` at `05:00`.
- **When** `Break` reaches zero, **the timer** shall switch back to `Focus` at `25:00`.

### AC-3 Controls

- **When** the user presses Pause, **the timer** shall stop decrementing and keep the
  remaining time.
- **When** the user presses Reset, **the timer** shall stop and return to `Focus 25:00`.

### AC-4 Independence

- The app shall not read from or write to the other application in this repository.
