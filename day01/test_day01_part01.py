import unittest
import day01_part01

class TestDay01Part01(unittest.TestCase):
    """ """
    def test_get_first_digit(self):
        """ Tests the get_first_digit function """

        test_data = [
            {"cal_val": "1a2", "truth": 1},
            {"cal_val": "1a", "truth": 1},
            {"cal_val": "a1a", "truth": 1},
            {"cal_val": "12a", "truth": 1}
            ]
        
        for data in test_data:
            res = day01_part01.get_first_digit(data["cal_val"])
            self.assertEqual(res, data["truth"])

    def test_get_last_digit(self):
        """Tests the get_last_digit function """

        test_data = [
            {"cal_val": "1a2", "truth": 2},
            {"cal_val": "1a", "truth": 1},
            {"cal_val": "a1a", "truth": 1},
            {"cal_val": "12a", "truth": 2},
            {"cal_val": "12a1a3", "truth": 3}
            ]
        
        for data in test_data:
            res = day01_part01.get_last_digit(data["cal_val"])
            self.assertEqual(res, data["truth"])

    def test_get_first_digit_error(self):
        """Tests the get_first_digit function with a faulty line"""

        test_data = [{"cal_val": "a"}]
        for data in test_data:
            #day01_part01.get_first_digit(data["cal_val"])
            self.assertRaises(IndexError, day01_part01.get_first_digit, data["cal_val"])

    def test_get_last_digit_error(self):
        """Tests the get_last_digit function with a faulty line"""

        test_data = [{"cal_val": "a"}]
        for data in test_data:
            self.assertRaises(IndexError, day01_part01.get_last_digit, data["cal_val"])

if __name__ == '__main__':
    unittest.main()