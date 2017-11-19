import bitcoinprice
import unittest
from pprint import pprint 

class Testbitcoinprice(unittest.TestCase):
    
    def test_price_simple(self):
        result = bitcoinprice.get_price_simple()
        self.assertIsInstance(result, str)

    def test_price_simple_eur(self):
        result = bitcoinprice.get_price_simple(curr='eur')
        self.assertIsInstance(result, str)

    def test_price(self):
        result = bitcoinprice.get_price()
        self.assertIsInstance(result, dict)

    def test_price_last(self):
        result = bitcoinprice.get_price()
        self.assertTrue(result['last'])

    def test_price_eur(self):
        result = bitcoinprice.get_price(curr='eur')
        self.assertIsInstance(result, dict)

    def test_price_not_string(self):
        result = bitcoinprice.get_price()
        self.assertIsNot(result, str)

    def test_float_convert(self):
        result = bitcoinprice.get_price_simple()
        self.assertTrue(float(result))


if __name__ == '__main__':
    unittest.main()
