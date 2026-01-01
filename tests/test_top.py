import unittest

from tally import top


class Top(unittest.TestCase):
    def test_most_common_first(self):
        self.assertEqual(top({"a": 1, "b": 3, "c": 2}, 2), [("b", 3), ("c", 2)])
