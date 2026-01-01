import unittest

from tally import count


class Edge(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count(""), {})

    def test_spaces(self):
        self.assertEqual(count("  \n\t "), {})


class Count(unittest.TestCase):
    def test_words(self):
        self.assertEqual(count("a b a"), {"a": 2, "b": 1})

    def test_case(self):
        self.assertEqual(count("A a"), {"a": 2})

    def test_lines(self):
        self.assertEqual(count("a b\na"), {"a": 2, "b": 1})
