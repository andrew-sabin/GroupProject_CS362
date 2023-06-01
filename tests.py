import unittest

from task import conv_num, my_datetime, conv_endian


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_conv_num_examples(self):
        """ Test cases provided as examples by the Group Project pt 2
        description to test Function 1, which is conv_num(num_str). Any test
        cases created by the group appear after this testing function.

        Comments explaining the purpose of each test case were not part of
        the rubric but were made by the group."""
        # A string with all integer characters returns an integer.
        # self.assertEqual(conv_num('12345'), 12345)

        # A string that starts with '-' and has a '.' should return a
        # negative float.
        # self.assertEqual(conv_num('-123.45'), -123.45)

        # A string that starts with '.' should return a float less than 1.
        # self.assertEqual(conv_num('.45'), 0.45)

        # A string that ends with '.' should return a float.
        # self.assertEqual(conv_num('123.'), 123.0)

        # A string that starts with 0x should return the integer version of
        # the hexadecimal.
        # self.assertEqual(conv_num('0xAD4'), 2772)

        # A string that starts with 0x & has letters from G to Z is not a
        # real hexadecimal, so None is returned.
        # self.assertEqual(conv_num('0xAZ4'), None)

        # A string with letters & no 0x is not a real hexadecimal, so None
        # is returned.
        # self.assertEqual(conv_num('12345A'), None)

        # A string with 2 or more dots is not a real float, so None is
        # returned.
        # self.assertEqual(conv_num('12.3.45'), None)

    def test_my_datetime_examples(self):
        """ Test cases provided as examples by the Group Project pt 2
        description to test Function 2, which is my_datetime(num_sec). Any test
        cases created by the group appear after this testing function.

        Comments explaining the purpose of each test case were not part of
        the rubric but were made by the group."""
        # No seconds = original date
        # self.assertEqual(my_datetime(0), '01-01-1970')

        # Less than 4 years => no leap day in calculation, date determined by
        # number of days in each specific month, with Feb having 28
        # self.assertEqual(my_datetime(123456789), '11-29-1973')

        # Less than 400 years => leap day determined by (years // 4 - years //
        # 100). February has 29 days on leap years.
        # self.assertEqual(my_datetime(9876543210), '12-22-2282')

        # More than 400 years => leap days determined by (years // 4 - years
        # / 100 + years // 400)
        # self.assertEqual(my_datetime(201653971200), '02-29-8360')


if __name__ == '__main__':
    unittest.main()
