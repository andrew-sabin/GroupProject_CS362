import unittest

# from task import conv_num, my_datetime, conv_endian
from task import conv_num
from task import conv_endian
from task import my_datetime


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
        self.assertEqual(conv_num('12345'), 12345)

        # A string that starts with '-' and has a '.' should return a
        # negative float.
        self.assertEqual(conv_num('-123.45'), -123.45)

        # A string that starts with '.' should return a float less than 1.
        self.assertEqual(conv_num('.45'), 0.45)

        # A string that ends with '.' should return a float.
        self.assertEqual(conv_num('123.'), 123.0)

        # A string that starts with 0x should return the integer version of
        # the hexadecimal.
        self.assertEqual(conv_num('0xAD4'), 2772)

        # A string that starts with 0x & has letters from G to Z is not a
        # real hexadecimal, so None is returned.
        self.assertEqual(conv_num('0xAZ4'), None)

        # A string with letters & no 0x is not a real hexadecimal, so None
        # is returned.
        self.assertEqual(conv_num('12345A'), None)

        # A string with 2 or more dots is not a real float, so None is
        # returned.
        self.assertEqual(conv_num('12.3.45'), None)

    def test_conv_num_notPossible(self):
        """ Return None for any of these:
            a) no characters
            b) empty space present
            c) 1-character string is not a digit
            d) +/- hex prefix but nothing afterwards
            e) 2 characters & 1 is any letter (no way to fit in a hex prefix
            f) 2 or more decimal points/periods
            g) hex prefix but letter is g to z
            h) punctuation that is not '.' is present
        """
        self.assertEqual(conv_num(''), None)
        self.assertEqual(conv_num('123 45'), None)
        self.assertEqual(conv_num('A'), None)
        self.assertEqual(conv_num('0x'), None)
        self.assertEqual(conv_num('-0x'), None)
        self.assertEqual(conv_num('2B'), None)
        self.assertEqual(conv_num('B2'), None)
        self.assertEqual(conv_num('123.45.'), None)
        self.assertEqual(conv_num('0xA5J'), None)
        self.assertEqual(conv_num('-0xA5J'), None)
        self.assertEqual(conv_num('1234/5'), None)

    def test_conv_num_case1(self):
        """ Positive Float
        decimal yes, negative no, hex no => positive float
        """
        self.assertEqual(conv_num('123.45'), 123.45)
        self.assertEqual(conv_num('123.'), 123.0)
        self.assertEqual(conv_num('.45'), 0.45)

    def test_conv_num_case2(self):
        """ Positive Digits
        decimal no, negative no, hex no => only digits """
        self.assertEqual(conv_num('12345'), 12345)
        self.assertEqual(conv_num('10234567'), 10234567)

    def test_conv_num_case3(self):
        """ Negative Float
        decimal yes, negative yes, hex no => positive float
        """
        self.assertEqual(conv_num('-123.'), 123.0)
        self.assertEqual(conv_num('-0.45'), -0.45)
        self.assertEqual(conv_num('-.45'), None)

    def test_conv_num_case4(self):
        """ Negative Digits
        decimal no, negative yes, hex no => only digits """
        self.assertEqual(conv_num('-12345'), -12345)
        self.assertEqual(conv_num('-10234567'), -10234567)

    def test_conv_num_case5(self):
        """ Positive Hexadecimal
        decimal no, negative no, hex yes """
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test_conv_num_case6(self):
        """ Negative Hexadecimal
        decimal no, negative yes, hex yes """
        self.assertEqual(conv_num('-0xAD4'), -2772)

    # ---------------------TESTS FOR MY_DATETIME----------------------------------

    # def test_my_datetime_examples(self):
    #     """ Test cases provided as examples by the Group Project pt 2
    #     description to test Function 2, which is my_datetime(num_sec). Any test
    #     cases created by the group appear after this testing function.

    #     Comments explaining the purpose of each test case were not part of
    #     the rubric but were made by the group."""

    # No seconds = original date
    def test_my_datetime_example1(self):
        self.assertEqual(my_datetime(0), '01-01-1970')

        # Less than 4 years => no leap day in calculation, date determined by
        # number of days in each specific month, with Feb having 28
        # self.assertEqual(my_datetime(123456789), '11-29-1973')

        # Less than 400 years => leap day determined by (years // 4 - years //
        # 100). February has 29 days on leap years.
        # self.assertEqual(my_datetime(9876543210), '12-22-2282')

        # More than 400 years => leap days determined by (years // 4 - years
        # // 100 + years // 400)
        # self.assertEqual(my_datetime(201653971200), '02-29-8360')

    # ----------------- Non-Example Tests-------------------------------

    # Test to see if day is increased by program, num_sec = 86400
    def test_my_datetime_personal1(self):
        self.assertEqual(my_datetime(86400), '01-02-1970')

    # Test to see if month is changed by program, num_sec = (86400 * 31)
    def test_my_datetime_personal2(self):
        self.assertEqual(my_datetime(2678400), '02-01-1970')

    # Test to see if year is changed by program, num_sec = (86400 * 365)
    def test_my_datetime_personal3(self):
        self.assertEqual(my_datetime(31536000), '01-01-1971')


# ---------------------TESTS FOR CONV_ENDIAN--------------------------------

    def test_endian_1(self):
        """This tests a positive even digit length number with a big endian"""
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_endian_2(self):
        """This tests a positive even digit length number with no endian"""
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_endian_3(self):
        """This tests a negative even digit length number with no endian"""
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_endian_4(self):
        """This tests a positive even digit length number with little endian"""
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_endian_5(self):
        """This tests a negative even digit length number with little endian"""
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_endian_6(self):
        """This tests a negative even digit length number with little endian
        with the parameters specified"""
        self.assertEqual(conv_endian(num=-954786, endian='little'),
                         '-A2 91 0E')

    def test_endian_7(self):
        """This tests a negative even digit length number with endian
        labeled small and with the parameters specified"""
        self.assertEqual(conv_endian(num=-954786, endian='small'), None)

    def test_endian_8(self):
        """This tests a positive odd digit length number with no
        endian labeled."""
        self.assertEqual(conv_endian(54786), 'D6 02')

    def test_endian_9(self):
        """This tests 0 with no endian labeled."""
        self.assertEqual(conv_endian(0), '0')


if __name__ == '__main__':
    unittest.main()
