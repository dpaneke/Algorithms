import unittest

from binsearch.Binsearch import Bsearch

class TestBinsearch(unittest.TestCase):
    def setUp(self):
        self.bs = Bsearch()

    def test_binsearch_right(self):
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 10), None)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 0), 0)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 3.5), 3)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 2.5), 2)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 1.5), 1)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 2), 1)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 3), 2)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 1), 0)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3, 4], 4), 3)
        self.assertEqual(self.bs.binsearch_right([1, 2, 2, 2, 2, 2, 2, 3, 4], 2), 1)
        self.assertEqual(self.bs.binsearch_right([1, 2, 2, 2, 2, 2, 2, 3, 4], 2.5), 7)
        self.assertEqual(self.bs.binsearch_right([], 4), None)
        self.assertEqual(self.bs.binsearch_right([4], 4), 0)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3], 10), None)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3], 0), 0)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3], 2.5), 2)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3], 1.5), 1)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3], 2), 1)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3], 3), 2)
        self.assertEqual(self.bs.binsearch_right([1, 2, 3], 1), 0)
        self.assertEqual(self.bs.binsearch_right([1, 2], 1.5), 1)
        self.assertEqual(self.bs.binsearch_right([1, 2], 2), 1)
        self.assertEqual(self.bs.binsearch_right([1, 2], 1), 0)
        self.assertEqual(self.bs.binsearch_right([1, 2], 0), 0)


    def test_binsearch_left(self):
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 10), 3)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 0), None)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 3.5), 2)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 2.5), 1)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 1.5), 0)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 2), 1)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 3), 2)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 1), 0)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3, 4], 4), 3)
        self.assertEqual(self.bs.binsearch_left([1, 2, 2, 2, 2, 2, 2, 3, 4], 2), 6)
        self.assertEqual(self.bs.binsearch_left([1, 2, 2, 2, 2, 2, 2, 3, 4], 1.5), 0)
        self.assertEqual(self.bs.binsearch_left([], 4), None)
        self.assertEqual(self.bs.binsearch_left([4], 4), 0)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3], 10), 2)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3], 0), None)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3], 2.5), 1)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3], 1.5), 0)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3], 2), 1)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3], 3), 2)
        self.assertEqual(self.bs.binsearch_left([1, 2, 3], 1), 0)
        self.assertEqual(self.bs.binsearch_left([1, 2], 1.5), 0)
        self.assertEqual(self.bs.binsearch_left([1, 2], 2), 1)
        self.assertEqual(self.bs.binsearch_left([1, 2], 1), 0)
        self.assertEqual(self.bs.binsearch_left([1, 2], 0), None)

if __name__=="__main__":
    unittest.main()
