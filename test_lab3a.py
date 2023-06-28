import unittest
from threading import Thread
from lab3a import BPlusMinusTree


class BPlusMinusTreeTestCase(unittest.TestCase):
    def test_insert_and_search(self):
        tree = BPlusMinusTree(order=3)
        values = [5, 1, 8, 2, 3, 9, 4, 7, 6]

        for value in values:
            tree.insert(value)

        for value in values:
            result = tree.search(value)
            self.assertTrue(result)

        self.assertFalse(tree.search(10))


if __name__ == '__main__':
    unittest.main()
