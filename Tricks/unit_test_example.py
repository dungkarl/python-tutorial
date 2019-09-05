
"""
    file include functions unittest
"""
import unittest
import calculate


class TestCalculate(unittest.TestCase):
    """
    """
    def test_add(self):
        result = calculate.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(calculate.add(-2, -4), -6)
        self.assertEqual(calculate.add(-1, 4), 3)
        self.assertEqual(calculate.add(-7, 4), -3)

    def test_sub(self):
        result = calculate.sub(10, 5)
        self.assertEqual(result, 5)
        self.assertEqual(calculate.sub(-1, -1), 0)
        self.assertEqual(calculate.sub(-1, 1), -2)


    def test_mul(self):
        result = calculate.mul(10, 5)
        self.assertEqual(result, 50)
        self.assertEqual(calculate.mul(2.0, 3), 6.0)

    
    def test_div(self):
        result = calculate.div(10, 5)
        self.assertEqual(2, result)
        #self.assertRaises(ValueError, calculate.div, 10,0)
        with self.assertRaises(ValueError):
            calculate.div(10, 0)

if __name__ == "__main__":
    unittest.main()
    