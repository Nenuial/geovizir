import unittest
from geovizir.features import ne_countries, ne_states
import geopolars as gpl

class TestFeatures(unittest.TestCase):
    def setUp(self):
        # Setup code goes here. This could be common set up for all the tests.
        pass

    def test_ne_countries_valid_scale(self):
        # Test with valid scale
        result = ne_countries(10)
        self.assertIsInstance(result, gpl.GeoDataFrame, "Expected result to be a GeoDataFrame")

    def test_ne_countries_invalid_scale(self):
        # Test with invalid scale
        with self.assertRaises(ValueError):
            ne_countries(20)

    def test_ne_countries_columns(self):
        # Test the columns of the resulting GeoDataFrame
        result = ne_countries(10)
        expected_columns = ['geometry', 'NAME', 'ADM0_A3']
        # Test that the columns exist in the resulting GeoDataFrame
        self.assertTrue(all([col in result.columns for col in expected_columns]))

    def test_ne_states_valid_scale(self):
        # Test with valid scale
        result = ne_states('CHE', 10)
        self.assertIsInstance(result, gpl.GeoDataFrame, "Expected result to be a GeoDataFrame")

    def test_ne_states_invalid_scale(self):
        # Test with invalid scale
        with self.assertRaises(ValueError):
            ne_states('CHE', 20)

    def test_ne_states_columns(self):
        # Test the columns of the resulting GeoDataFrame
        result = ne_states('CHE', 10)
        expected_columns = ['geometry', 'name', 'adm0_a3']
        # Test that the columns exist in the resulting GeoDataFrame
        self.assertTrue(all([col in result.columns for col in expected_columns]))

if __name__ == '__main__':
    unittest.main()
