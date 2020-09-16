import unittest

from numtext.numtext import numtext, map_single


class TestNumtext(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)
    
    def test_map_single(self):
        self.assertEqual(map_single(0), 'zero')
        self.assertEqual(map_single(1), 'one')
        self.assertEqual(map_single(2), 'two')
        self.assertEqual(map_single(3), 'three')
        self.assertEqual(map_single(4), 'four')
        self.assertEqual(map_single(5), 'five')
        self.assertEqual(map_single(6), 'six')
        self.assertEqual(map_single(7), 'seven')
        self.assertEqual(map_single(8), 'eight')
        self.assertEqual(map_single(9), 'nine')

        with self.assertRaises(ValueError):
            map_single(-1)
        with self.assertRaises(ValueError):
            map_single(10)


    def test_numtext_single_digit(self):
        self.assertEqual(numtext(0), 'zero')
        self.assertEqual(numtext(1), 'one')
        self.assertEqual(numtext(2), 'two')
        self.assertEqual(numtext(3), 'three')
        self.assertEqual(numtext(4), 'four')
        self.assertEqual(numtext(5), 'five')
        self.assertEqual(numtext(6), 'six')
        self.assertEqual(numtext(7), 'seven')
        self.assertEqual(numtext(8), 'eight')
        self.assertEqual(numtext(9), 'nine')