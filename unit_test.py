import unittest

def square_number_plus_one(number: int):
    output = (number * number) + 1
    return output

class TestSquareNumberPlusOne(unittest.TestCase):

    def test_positive_integer(self):
        result = square_number_plus_one(5)
        self.assertEqual(result, 26)

    def test_negative_integer(self):
        result = square_number_plus_one(-3)
        self.assertEqual(result, 10)

    def test_zero(self):
        result = square_number_plus_one(0)
        self.assertEqual(result, 1)

    def test_large_integer(self):
        result = square_number_plus_one(10**6)
        self.assertEqual(result, 1000000000001)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            square_number_plus_one(3.5)

if __name__ == '__main__':
    unittest.main()