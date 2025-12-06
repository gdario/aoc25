from part2 import get_joltage
import unittest


class TestJoltage(unittest.TestCase):
    def test_correct(self):
        test_data = """987654321111111
        811111111111119
        234234234234278
        818181911112111""".split('\n')
        self.assertEqual(get_joltage(test_data[0]), 987654321111)
        self.assertEqual(get_joltage(test_data[1]), 811111111119)
        self.assertEqual(get_joltage(test_data[2]), 434234234278)
        self.assertEqual(get_joltage(test_data[3]), 888911112111)
