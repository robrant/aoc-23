import unittest
import day01_part01

class TestDay01Part01(unittest.TestCase):
    """ """
    def get_first_digit(self):
        """ Tests the get_first_digit function """

        test_data = [
            {"cal_val": "1a2", "truth": 1},
            {"cal_val": "1a", "truth": 1},
            {"cal_val": "a1a", "truth": 1},
            {"cal_val": "12a", "truth": 1},
            {"cal_val": "onetwo2", "truth": 1},
            {"cal_val": "1two", "truth": 1},
            {"cal_val": "aa1two", "truth": 1},
            {"cal_val": "three1two", "truth": 3},
            {"cal_val": "oneeight2", "truth": 1}
            ]

        for data in test_data:
            print (data["cal_val"])
            res = day01_part01.get_first_digit(data["cal_val"])
            self.assertEqual(res, data["truth"])

    def test_get_last_digit(self):
        """ Tests the get_last_digit function """

        test_data = [
            {"cal_val": "1a2", "truth": 2},
            {"cal_val": "1a", "truth": 1},
            {"cal_val": "a1a", "truth": 1},
            {"cal_val": "12a", "truth": 2},
            {"cal_val": "onetwo2", "truth": 2},
            {"cal_val": "1two", "truth": 2},
            {"cal_val": "aa1two", "truth": 2},
            {"cal_val": "three1two", "truth": 2},
            {"cal_val": "2oneight", "truth": 8}
            ]

        for data in test_data:
            print (data["cal_val"])
            res = day01_part01.get_last_digit(data["cal_val"])
            self.assertEqual(res, data["truth"])

if __name__ == '__main__':
    unittest.main()