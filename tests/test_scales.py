import unittest
from geovizir import scales

class TestScales(unittest.TestCase):
    def setUp(self):
        # Setup code goes here. This could be common set up for all the tests.
        pass

    def test_label_bins(self):
        result = scales.label_bins([1,2,3,4])
        expected_result = ['< 1', '1-2', '2-3', '3-4', '> 4']
        self.assertEqual(result, expected_result, "Expected result does not match the actual result")

if __name__ == '__main__':
    unittest.main()