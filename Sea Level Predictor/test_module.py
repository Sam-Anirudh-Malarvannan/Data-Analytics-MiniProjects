import unittest
from sea_level_predictor import draw_plot
from matplotlib.axes import Axes

class TestSeaLevelPredictor(unittest.TestCase):
    def test_return_type(self):
        self.assertIsInstance(draw_plot(), Axes)

if __name__ == '__main__':
    unittest.main()