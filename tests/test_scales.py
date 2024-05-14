import unittest
import pandas as pd
from geovizir import scales

class TestScales(unittest.TestCase):
    def setUp(self):
        # Setup code goes here. This could be common set up for all the tests.
        pass

    def test_label_bins(self):
        result = scales.label_bins([1,2,3,4])
        expected_result = ['< 1', '1-2', '2-3', '3-4', '> 4']
        self.assertEqual(result, expected_result, "Expected result does not match the actual result")

    def test_relabel_bins(self):
        series = pd.Series([1, 2, 3, 4, 5, 6], dtype="int")
        series_cut = pd.cut(series, bins=2)
        result = scales.relabel_bins(series_cut)
        # Define the levels in the desired order
        categories = ['0.995 - 3.5', '3.5 - 6.0']

        # Create the Series with the ordered categories
        expected_result = pd.Series(
            pd.Categorical(
                ['0.995 - 3.5', '0.995 - 3.5', '0.995 - 3.5',
                '3.5 - 6.0', '3.5 - 6.0', '3.5 - 6.0'],
                categories=categories,
                ordered=True
            )
        )
        pd.testing.assert_series_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()