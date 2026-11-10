# Design: word-frequency

`main.py` exposes one pure function, `top_words(text, limit)`, over an
`argparse` front door. Keeping the counting pure is what lets
`test_properties.py` drive it with generated strings instead of files.

- Token pattern: `[A-Za-z][A-Za-z'-]+` — satisfies AC-1 (apostrophes and hyphens
  stay inside a word, digits and lone letters fall out).
- `collections.Counter.most_common(limit)` — satisfies AC-2.
