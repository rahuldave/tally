import unittest

from tally import count


class Edge(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count(""), {})

    def test_spaces(self):
        self.assertEqual(count("  \n\t "), {})
