import unittest
import medical_data_visualizer

class TestMedicalDataVisualizer(unittest.TestCase):
    def test_cat_plot(self):
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertEqual(str(type(fig)), "<class 'matplotlib.figure.Figure'>")

    def tes_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertEqual(str(type(fig)), "<class 'matplotlib.figure.Figure'>")

    if __name__ == "__main__":
        unittest.main()