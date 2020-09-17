import unittest

from numtext.numtext import numtext, map_one_digit, map_two_digit, map_three_digit, config


class TestNumtext(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)
    
    def test_map_one_digit(self):
        """Unit test for the map_one_digit function"""
        self.assertEqual(map_one_digit(0), 'zero')
        self.assertEqual(map_one_digit(1), 'one')
        self.assertEqual(map_one_digit(2), 'two')
        self.assertEqual(map_one_digit(3), 'three')
        self.assertEqual(map_one_digit(4), 'four')
        self.assertEqual(map_one_digit(5), 'five')
        self.assertEqual(map_one_digit(6), 'six')
        self.assertEqual(map_one_digit(7), 'seven')
        self.assertEqual(map_one_digit(8), 'eight')
        self.assertEqual(map_one_digit(9), 'nine')

        with self.assertRaises(ValueError):
            map_one_digit(10)

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

    def test_map_two_digit(self):
        """Unit test for the map_two_digit function"""
        self.assertEqual(map_two_digit(11), 'eleven')
        self.assertEqual(map_two_digit(12), 'twelve')
        self.assertEqual(map_two_digit(16), 'sixteen')
        self.assertEqual(map_two_digit(19), 'nineteen')

        self.assertEqual(map_two_digit(10), 'ten')
        self.assertEqual(map_two_digit(40), 'fourty')
        self.assertEqual(map_two_digit(60), 'sixty')
        self.assertEqual(map_two_digit(90), 'ninety')

        self.assertEqual(map_two_digit(21), 'twenty one')
        self.assertEqual(map_two_digit(45), 'fourty five')
        self.assertEqual(map_two_digit(67), 'sixty seven')
        self.assertEqual(map_two_digit(99), 'ninety nine')

        with self.assertRaises(ValueError):
            map_two_digit(100)

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

    def test_map_three_digit(self):
        """Unit test for map_three_digit"""
        self.assertEqual(map_three_digit(100), 'one hundred')
        self.assertEqual(map_three_digit(400), 'four hundred')
        self.assertEqual(map_three_digit(800), 'eight hundred')

        self.assertEqual(map_three_digit(202), 'two hundred and two')
        self.assertEqual(map_three_digit(308), 'three hundred and eight')
        self.assertEqual(map_three_digit(605), 'six hundred and five')

        self.assertEqual(map_three_digit(111), 'one hundred and eleven')
        self.assertEqual(map_three_digit(483), 'four hundred and eighty three')
        self.assertEqual(map_three_digit(990), 'nine hundred and ninety')

    def test_numtext_three_digit(self):
        """Test handling of three digit numbers"""
        self.assertEqual(map_three_digit(100), 'one hundred')
        self.assertEqual(map_three_digit(400), 'four hundred')
        self.assertEqual(map_three_digit(800), 'eight hundred')

        self.assertEqual(map_three_digit(202), 'two hundred and two')
        self.assertEqual(map_three_digit(308), 'three hundred and eight')
        self.assertEqual(map_three_digit(605), 'six hundred and five')

        self.assertEqual(map_three_digit(111), 'one hundred and eleven')
        self.assertEqual(map_three_digit(483), 'four hundred and eighty three')
        self.assertEqual(map_three_digit(990), 'nine hundred and ninety')

        self.assertEqual(numtext(-876), 'negative eight hundred and seventy six')

    def test_numtext_large_numbers(self):
        self.assertEqual(
            numtext(1000), 
            'one thousand'
        )
        self.assertEqual(
            numtext(5000), 
            'five thousand'
        )
        self.assertEqual(
            numtext(1111), 
            'one thousand one hundred and eleven'
        )
        self.assertEqual(
            numtext(76543), 
            'seventy six thousand five hundred and fourty three'
        )
        self.assertEqual(
            numtext(1000000),
            'one million'
        )
        self.assertEqual(
            numtext(123456789),
            'one hundred and twenty three million four hundred and fifty six thousand seven hundred and eighty nine'
        )
        self.assertEqual(
            numtext(1000100),
            'one million one hundred'
        )
        self.assertEqual(
            numtext(1000000000), 
            'one billion'
        )
        self.assertEqual(
            numtext(-999999),
            'negative nine hundred and ninety nine thousand nine hundred and ninety nine'
        )

    def test_switch_naming_scheme(self):
        """Test switching to a different naming scheme"""
        self.assertEqual(numtext(1000000000), 'one billion')
        config.naming_scheme = 'eu_long'
        self.assertEqual(numtext(1000000000), 'one milliard')
