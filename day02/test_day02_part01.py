import unittest
import day02_part01

class TestDay02Part01(unittest.TestCase):
    """ """

    def test_get_sub_game_list(self):
        """ Tests get_sub_game_list function """

        test_data = [
            {"input": "14 blue, 3 green", "truth": [{'blue': 14}, {'green': 3}]},
            {"input": "14 blue, 3 green", "truth": [{'blue': 14}, {'green': 3}]},
            ]

        for data in test_data:
            res = day02_part01.get_sub_game_list(data["input"])
            self.assertEqual(res, data["truth"])

if __name__ == '__main__':
    unittest.main()