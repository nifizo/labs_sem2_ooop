import unittest
from lab1a import BPlusMinusTree

class TestBPlusMinusTree(unittest.TestCase):
    def test_insert_and_search(self):
        tree = BPlusMinusTree(3)
        tree.insert(5)
        tree.insert(10)
        tree.insert(3)
        tree.insert(7)

        self.assertTrue(tree.search(5))
        self.assertTrue(tree.search(10))
        self.assertTrue(tree.search(3))
        self.assertTrue(tree.search(7))
        self.assertFalse(tree.search(1))
        self.assertFalse(tree.search(9))

if __name__ == '__main__':
    unittest.main()