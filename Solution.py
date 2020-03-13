from HighCard import HighCard
from CardType import CardType
import unittest
import random
import constant


class Solution(object):

    def generate_testcase(self):
        return_value = []
        for i in range(5):
            temp_number = random.randint(0, 3)
            if temp_number == 0:
                temp_char = 'D'
            elif temp_number == 1:
                temp_char = 'S'
            elif temp_number == 2:
                temp_char = 'H'
            else:
                temp_char = 'C'
            temp_number = random.randint(2, 14)
            return_value.append((temp_char, temp_number))
        return return_value

    def compare(self, list1, list2):
        cardtype1 = HighCard.check_Card_Type(self, list1)
        cardtype2 = HighCard.check_Card_Type(self, list2)
        return CardType.compare_after_every_card_type_got(self, cardtype1, cardtype2)


class SolutionSuit(unittest.TestCase):
    def test_should_print_testcase(self):
        print(Solution.generate_testcase(self))

    def test_should_judge_for_two_testcase1(self):
        testcase1 = [('S', 3), ('H', 5), ('C', 4), ('C', 6), ('C', 7)]
        testcase2 = [('S', 8), ('H', 5), ('C', 4), ('C', 6), ('C', 7)]
        self.assertEqual(Solution.compare(self, testcase1, testcase2), True)

    def test_should_judge_for_two_testcase2(self):
        testcase1 = [('C', 3), ('C', 3), ('C', 4), ('C', 6), ('C', 7)]
        testcase2 = [('S', 8), ('H', 5), ('C', 4), ('C', 6), ('C', 7)]
        self.assertEqual(Solution.compare(self, testcase1, testcase2), False)

    def test_should_judge_for_two_testcase3(self):
        testcase1 = [('C', 3), ('C', 9), ('D', 4), ('C', 6), ('D', 7)]
        testcase2 = [('S', 8), ('H', 5), ('C', 4), ('C', 11), ('C', 7)]
        self.assertEqual(Solution.compare(self, testcase1, testcase2), True)

    def test_should_judge_for_two_testcase4(self):
        testcase1 = [('D', 3), ('C', 3), ('S', 4), ('C', 6), ('H', 4)]
        testcase2 = [('S', 2), ('H', 4), ('C', 4), ('D', 2), ('C', 9)]
        self.assertEqual(Solution.compare(self, testcase1, testcase2), constant.EQUAL)

    def test_should_judge_for_two_equal_testcase(self):
        testcase1 = [('S', 3), ('H', 5), ('C', 4), ('C', 6), ('C', 7)]
        testcase2 = [('S', 3), ('H', 5), ('C', 4), ('C', 6), ('C', 7)]
        self.assertEqual(Solution.compare(self, testcase1, testcase2), constant.EQUAL)


if __name__ == '__main__':
    unittest.main()
    SystemExit
