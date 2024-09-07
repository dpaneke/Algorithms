import unittest

from PrefixFunction import prefix_function

class TestPrefixFunction(unittest.TestCase):
    def test_prefix_function(self):
        self.assertEqual(prefix_function("aaaaa"), [0, 1, 2, 3, 4])
        self.assertEqual(prefix_function("xyzxyzx"), [0, 0, 0, 1, 2, 3, 4])
        self.assertEqual(prefix_function("xxyxxxy"), [0, 1, 0, 1, 2, 2, 3])

if __name__=="__main__":
    unittest.main()


