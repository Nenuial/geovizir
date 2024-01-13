import unittest
import pandas as pd
from geovizir.data import get_data

class TestGetData(unittest.TestCase):
    def setUp(self):
        self.indicator = "SP.POP.TOTL"
        self.year = 2020

    def test_get_data(self):
        df = get_data(self.indicator, self.year)
        self.assertTrue(df[df["country"] == "Spain"]["iso3c"].item(), "ESP")
        self.assertTrue(df[df["country"] == "Spain"]["value"].item(), 47365655.0)
        self.assertIsInstance(df, pd.DataFrame, "Expected result to be a DataFrame")

if __name__ == '__main__':
    unittest.main()