import unittest
import pandas as pd
from geovizir.data import get_data, get_data_most_recent

class TestGetData(unittest.TestCase):
    def setUp(self):
        self.indicator = "SP.POP.TOTL"
        self.year = 2020

    def test_get_data(self):
        df = get_data(self.indicator, self.year)
        self.assertTrue(df[df["country"] == "Spain"]["iso3c"].item(), "ESP")
        self.assertTrue(df[df["country"] == "Spain"]["value"].item(), 47365655.0)
        self.assertIsInstance(df, pd.DataFrame, "Expected result to be a DataFrame")

class TestGetDataMostRecent(unittest.TestCase):
    def setUp(self):
        self.indicator = "SP.POP.TOTL"

    def test_get_data_most_recent_type(self):
        df = get_data_most_recent(self.indicator)
        self.assertIsInstance(df, pd.DataFrame, "Expected result to be a DataFrame")

    def test_get_data_most_recent_columns(self):
        df = get_data_most_recent(self.indicator)
        expected_columns = ["country", "iso3c", "date", "value"]
        self.assertTrue(set(expected_columns).issubset(df.columns), "Expected DataFrame to have columns: " + ", ".join(expected_columns))

    def test_get_data_most_recent_not_empty(self):
        df = get_data_most_recent(self.indicator)
        self.assertFalse(df.empty, "Expected DataFrame to not be empty")

if __name__ == '__main__':
    unittest.main()