import unittest

from tally import count


class Count(unittest.TestCase):
    def test_words(self):
        self.assertEqual(count("a b a"), {"a": 2, "b": 1})

    def test_case(self):
        self.assertEqual(count("A a"), {"a": 2})
