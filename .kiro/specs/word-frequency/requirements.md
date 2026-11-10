# Requirements: word-frequency

## Introduction

A command line tool that reports the most frequent words of a UTF-8 text file.

## Requirements

### AC-1 Counting

- **The tool** shall count ASCII words of two or more characters, case-insensitively,
  treating `Don't` and `well-known` as single words.
- **The tool** shall ignore runs of digits and single letters.

### AC-2 Ordering

- **The tool** shall print at most `-n` lines (default 10), highest count first.
- **When** two words share a count, **the tool** may order them arbitrarily.

### AC-3 Properties (checked by `word-frequency-cli/test_properties.py`)

- **P-1** Every reported count is ≥ 1 and ≤ the number of words found.
- **P-2** Reported counts are monotonically non-increasing.
- **P-3** Summing the counts of *all* distinct words equals the total word count
  (no word is dropped or double counted).
- **P-4** Repeating the text with a newline between the copies doubles every count.
  (Plain concatenation is not used as a property: a trailing letter and a leading
  letter would merge into one token.)
