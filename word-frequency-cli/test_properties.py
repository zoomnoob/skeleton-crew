"""Property-based tests for top_words() — see .kiro/specs/word-frequency/requirements.md AC-3.

Randomised with a fixed seed so a failure prints a reproducible counterexample:
    python3 -m unittest -v test_properties
"""

import random
import unittest
from collections import Counter

from main import WORD, top_words

ALPHABET = "aBz 019'-.,\n\téß\""
CASES = 300


def sample(rnd: random.Random) -> str:
    return "".join(rnd.choice(ALPHABET) for _ in range(rnd.randrange(0, 200)))


class TestProperties(unittest.TestCase):
    def setUp(self) -> None:
        self.rnd = random.Random(20261109)
        self.texts = [sample(self.rnd) for _ in range(CASES)]

    def check(self, predicate, case):
        self.assertTrue(predicate(case), f"property violated for input: {case!r}")

    def test_p1_counts_are_within_bounds(self):
        for case in self.texts:
            total = len(WORD.findall(case))
            self.check(
                lambda t: all(1 <= c <= total for _, c in top_words(t, 10)), case
            )

    def test_p2_counts_are_non_increasing(self):
        for case in self.texts:
            self.check(
                lambda t: (
                    lambda c: all(x >= y for x, y in zip(c, c[1:]))
                )([c for _, c in top_words(t, 10)]),
                case,
            )

    def test_p3_no_word_is_dropped_or_double_counted(self):
        for case in self.texts:
            found = len(WORD.findall(case))
            self.check(
                lambda t: sum(c for _, c in top_words(t, 10**6)) == found, case
            )

    def test_p4_duplicating_the_text_doubles_every_count(self):
        for case in self.texts:
            def holds(t):
                base = Counter(dict(top_words(t, 10**6)))
                doubled = Counter(dict(top_words(t + "\n" + t, 10**6)))
                return all(c * 2 == doubled[w] for w, c in base.items())

            self.check(holds, case)


if __name__ == "__main__":
    unittest.main()
