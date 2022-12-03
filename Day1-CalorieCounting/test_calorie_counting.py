import unittest
from calorie_counting import split_list_on_empty_element


class CalorieCounting(unittest.TestCase):
    def test_split_list_on_empty_element(self):
        # arrange
        nums_list = ['1000', '2000', '3000', '', '4000', '', '5000',
                     '6000', '', '7000', '8000', '9000', '', '10000', '',
                     ]
        expected = [6000, 4000, 11000, 24000, 10000]
        # act
        actual = split_list_on_empty_element(nums_list)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
