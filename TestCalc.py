import unittest
from Calculator import add, subtract, multiply, divide, power, sqrroot

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 3), 0)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(-4, 2), -2)
        self.assertEqual(divide(4, -2), -2)
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(2,0), -1)



        # test if exception is raised
        # with self.assertRaises(ValueError):
         #   divide(2, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(2, 0), 1)

    def test_sqrroot(self):
        self.assertEqual(sqrroot(4), 2)
        self.assertEqual(sqrroot(9), 3)
        self.assertEqual(sqrroot(0), 0)

if __name__ == '__main__':
    unittest.main()

