import unittest
from mean_var_std import calculate


class UnitTests(unittest.TestCase):
    def test_calculate(self):
        self.assertAlmostEqual(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['mean'][2], 4.0)
        self.assertAlmostEqual(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['variance'][2], 6.666666666666667)
        self.assertAlmostEqual(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['standard deviation'][2], 2.581988897471611)
        self.assertEqual(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['max'][2], 8)
        self.assertEqual(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['min'][2], 0)
        self.assertEqual(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['sum'][2], 36)

    def test_calculate_raise(self):  # <-- Fixed the typo here
        with self.assertRaises(ValueError):
            calculate([2, 3, 4])


if __name__ == '__main__':
    unittest.main()
