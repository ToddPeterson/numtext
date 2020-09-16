import unittest

from numtext.numtext import numtext, map_single, map_double


class TestNumtext(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)
    
    def test_map_single(self):
        """Unit test for the map_single function"""
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
        """Test calling numtext on single digit numbers"""
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
    
    def test_numtext_negative(self):
        """Test handling of negative numbers"""
        self.assertEqual(numtext(-1), 'negative one')
        self.assertEqual(numtext(-3), 'negative three')
        self.assertEqual(numtext(-7), 'negative seven')

    def test_map_double(self):
        """Unit test for the map_double function"""
        self.assertEqual(map_double(11), 'eleven')
        self.assertEqual(map_double(12), 'twelve')
        self.assertEqual(map_double(16), 'sixteen')
        self.assertEqual(map_double(19), 'nineteen')

        self.assertEqual(map_double(10), 'ten')
        self.assertEqual(map_double(40), 'fourty')
        self.assertEqual(map_double(60), 'sixty')
        self.assertEqual(map_double(90), 'ninety')

        self.assertEqual(map_double(21), 'twenty one')
        self.assertEqual(map_double(45), 'fourty five')
        self.assertEqual(map_double(67), 'sixty seven')
        self.assertEqual(map_double(99), 'ninety nine')

        with self.assertRaises(ValueError):
            map_double(1)
        with self.assertRaises(ValueError):
            map_double(100)

    def test_numtext_two_digit(self):
        """Test handling of two digit numbers"""
        self.assertEqual(numtext(11), 'eleven')
        self.assertEqual(numtext(12), 'twelve')
        self.assertEqual(numtext(16), 'sixteen')
        self.assertEqual(numtext(19), 'nineteen')

        self.assertEqual(numtext(10), 'ten')
        self.assertEqual(numtext(40), 'fourty')
        self.assertEqual(numtext(60), 'sixty')
        self.assertEqual(numtext(90), 'ninety')

        self.assertEqual(numtext(21), 'twenty one')
        self.assertEqual(numtext(45), 'fourty five')
        self.assertEqual(numtext(67), 'sixty seven')
        self.assertEqual(numtext(99), 'ninety nine')

        self.assertEqual(numtext(-33), 'negative thirty three')
