import unittest
from unittest.mock import patch
import pandas as pd
from io import StringIO
from geovizir.dplyr import glimpse

class TestGlimpse(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['a', 'b', 'c', 'd', 'e'],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })

    @patch('sys.stdout', new_callable=StringIO)
    def test_glimpse(self, mock_stdout):
        glimpse(self.df)
        expected_output = (
            "<class 'pandas.core.frame.DataFrame'>:  5 rows of 3 columns\n"
            "A:  int64     [1, 2, 3, 4, 5]\n"
            "B:  object    ['a', 'b', 'c', 'd', 'e']\n"
            "C:  float64   [1.1, 2.2, 3.3, 4.4, 5.5]\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_glimpse_max_width(self, mock_stdout):
        glimpse(self.df, max_width=30)
        expected_output = (
            "<class 'pandas.core.frame.DataFrame'>:  5 rows of 3 columns\n"
            "A:  int64     [1, 2, 3, 4, 5]\n"
            "B:  object    ['a', 'b', ' ...\n"
            "C:  float64   [1.1, 2.2, 3 ...\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()