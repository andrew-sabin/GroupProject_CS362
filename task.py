
import string  # for easier importing of digits & characters


# Function 1
def conv_num(num_str):
    """


    Possible
    1. decimal yes, negative no, hex no => positive float
    2. decimal no, negative no, hex no => positive, only digits
    3. decimal yes, negative yes, hex no => negative float
    4. decimal no, negative yes, hex no => negative, only digits
    X. decimal yes, negative no, hex yes => rubric says NOT a valid hex input
    5. decimal no, negative no, hex yes => positive hexadecimal
    X. decimal yes, negative yes, hex yes => rubric says NOT a valid hex input
    6. decimal no, negative yes, hex yes => negative hexadecimal """

    if is_valid_conv_num_str(num_str) is False:
        return None

    # Case 1: if 1 decimal, no neg, no hex
    elif num_str.count('.') == 1 and num_str.count('-') == 0 and \
            num_str.count('x') == 0:
        return positive_float(num_str)

    # Case 2: if no decimal, no negative, no hexadecimal
    elif num_str.count('.') == 0 and num_str.count('-') == 0 and \
            num_str.count('x') == 0:
        return positive_integer(num_str)

    # Case 3: decimal yes, negative yes, hex no => negative float
    elif (num_str.count('.') == 1 and num_str.count('-') == 1) and \
            (num_str[0] == '-' and num_str.count('x') == 0):
        return negative_float(num_str)

    # Case 4: Negative Digits... decimal no, negative yes, hex no => negative
    # only digits
    elif num_str.count('.') == 0 and num_str.count('-') == 1 and \
            num_str[0] == '-' and num_str.count('x') == 0:
        return negative_integer(num_str)

    # Case 5: Positive Hexadecimal... decimal no, negative no, hex yes =>
    # positive hexadecimal
    elif len(num_str) >= 3 and num_str[0:2] == '0x' and num_str.count('.') \
            == 0 and num_str.count('-') == 0:
        return positive_hexadecimal(num_str)

    # Case 6: Negative Hexadecimal... decimal no, negative yes, hex yes =>
    # negative hexadecimal
    elif len(num_str) >= 4 and num_str[0:3] == '-0x':
        return negative_hexadecimal(num_str)


    # if not in the 6 Cases:
    else:
        return None


def is_valid_conv_num_str(num_str):
    """ Not Possible
    a) no characters
    b) empty space present
    c) 1-character string is not a digit
    d) +/- hex prefix but nothing afterwards
    e) 2 characters & 1 is any letter (no way to fit in a hex prefix
    f) 2 or more decimal points/periods
    g) hex prefix but letter is g to z
    h) punctuation that is not '.' is present """
    # if no character
    if num_str == '':
        return False
    # if empty space in num_str
    elif ' ' in num_str:
        return False
    # if 1-character string is not a digit
    elif len(num_str) == 1 and num_str[0] not in string.digits:
        return False
    # if string is only hexadecimal start with nothing else after
    elif num_str == '0x' or num_str == '-0x':
        return False
    # if 2 characters (so no way for hexadecimal prefix) and one of the
    # characters is a letter
    elif len(num_str) == 2 and ((num_str[0] in string.ascii_lowercase or
                                num_str[
        0] in string.ascii_uppercase) or (num_str[1] in
                                          string.ascii_lowercase or num_str[1]
                                          in string.ascii_uppercase)):
        return False
    # if more than 1 period
    elif num_str.count('.') >= 2:
        return False
    else:
        return True


def conv_int_or_hex_helper(num_str, allowed_digits, start, end,
                           place_value, multiplier):
    """  """
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
                'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12,
                'd': 13, 'e': 14, 'f': 15}
    answer = 0
    for i in range(start, end):
        if num_str[i] not in allowed_digits:
            return None
        answer += hex_dict[num_str[i]] * (multiplier ** (place_value - 1))
        place_value -= 1
    return answer


def conv_float_helper(num_str, allowed_digits, place_value,
                      start, decimal_index):
    """  """
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
                'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12,
                'd': 13, 'e': 14, 'f': 15}
    answer = 0
    for i in range(start, decimal_index):
        if num_str[i] not in allowed_digits:
            return None
        answer += hex_dict[num_str[i]] * 10 ** place_value
        place_value -= 1

    decimal_place_value = 1
    for j in range(decimal_index + 1, len(num_str)):
        if num_str[j] not in allowed_digits:
            return None
        answer += (hex_dict[num_str[j]] / (10 ** decimal_place_value))
        decimal_place_value += 1
    return answer


def positive_float(num_str):
    """ decimal yes, negative no, hex no => positive float """
    if num_str[-1] == '.':
        # self.assertEqual(conv_num('123.'), 123.0)
        answer = conv_int_or_hex_helper(num_str, string.digits, 0,
                                        len(num_str) - 1, len(num_str) - 1,
                                        10)
    elif num_str[0] == '.':
        # self.assertEqual(conv_num('.45'), 0.45)
        answer = conv_float_helper(num_str, string.digits, 1, 1, 0)
    else:
        decimal_index = num_str.index('.')
        answer = conv_float_helper(num_str, string.digits, decimal_index - 1,
                                   0, decimal_index)
    return None if answer is None else answer + 0.0


def positive_integer(num_str):
    """ decimal no, negative no, hex no => positive, only digits """
    # self.assertEqual(conv_num('12345'), 12345)
    return conv_int_or_hex_helper(num_str, string.digits, 0, len(num_str),
                                  len(num_str), 10)


def negative_float(num_str):
    """ 3. decimal yes, negative yes, hex no => negative float """
    if num_str[-1] == '.':
        # self.assertEqual(conv_num('-123.45'), -123.45)
        answer = conv_int_or_hex_helper(num_str, string.digits, 1,
                                        len(num_str) - 1, len(num_str) - 2,
                                        10)
    # -.45 is not a valid number.
    elif num_str[0:2] == '-.':
        return None
    # Example: -0.45 has period in index 2
    elif num_str[2] == '.':
        if num_str == '-0.':
            return None
        # self.assertEqual(conv_num('.45'), 0.45)
        answer = conv_float_helper(num_str, string.digits, 1,
                                   1, 2)
    else:
        decimal_index = num_str.index('.')
        answer = conv_float_helper(num_str, string.digits, decimal_index - 2,
                                   1, decimal_index)
    return None if answer is None else (answer + 0.0) * -1


def negative_integer(num_str):
    """ 4. decimal no, negative yes, hex no => negative, only digits """
    answer = conv_int_or_hex_helper(num_str, string.digits, 1, len(num_str),
                                    len(num_str) - 1, 10)
    return None if answer is None else answer * -1


def positive_hexadecimal(num_str):
    """ 5. decimal no, negative no, hex yes => positive hexadecimal """
    return conv_int_or_hex_helper(num_str, string.hexdigits, 2, len(num_str),
                                  len(num_str) - 2, 16)


def negative_hexadecimal(num_str):
    """ 6. decimal no, negative yes, hex yes => negative hexadecimal """
    answer = conv_int_or_hex_helper(num_str, string.hexdigits, 3, len(num_str),
                                    len(num_str) - 3, 16)
    return None if answer is None else answer * -1


# Function 2
def my_datetime(num_sec):
    """ Returns the mm-dd-yyyy string value based on how many seconds were entered for num_sec"""
    # set values for default month, day, year
    month = 1
    day = 1
    year = 1970

    # set dictionary for the days of each month for normal years
    # key is the month, value is the amount of days in that month
    months_year = {'1': 31, '2': [28, 29], '3': 31, '4': 30, '5': 31,
                   '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    # set dictionary for the days of each month for leap years
    # leap_year = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}

    # set curr_month to be equal to the amount of days set in the months_year
    curr_month = months_year[str(month)]

    # set for loop for increase in days, 86400 seconds in a day
    while num_sec > 86399:
        num_sec -= 86400
        day += 1
        # if-statement to see if day is less than or equal to the amount of days in month
        # if false add to month by 1 and reset days to 1
        if day > curr_month:
            month += 1
            day = 1
        # if statement to see if day of the year is 2 for february
            if month == 2:
                if year % 4 == 0:
                    curr_month = months_year['2'][1]
                else:
                    curr_month = months_year['2'][0]
            else:
                curr_month = months_year[str(month)]
        # if True, test to see if the year % 4 is equal to 0
        # if True set the days_in_month to 29
        # if False set the days_in_month to 28

        # if-statement to see if the month in the year is less than or equal to 12
        # if False, add to year by 1 and reset month back to 1

    # set a string value based on the month-day-year
    if month < 10:
        month = '0'+str(month)
    else:
        month = str(month)

    if day < 10:
        day = '0'+str(day)
    else:
        day = str(day)
    mmDdYy = month + '-' + day + '-' + str(year)

    return mmDdYy


# Function 3
def endian_formatting(split_answer, endian, negative):
    answer = ''
    if endian == 'little':
        split_answer.reverse()
    for element in split_answer:
        answer += element
        answer += ' '
    if negative is True:
        answer = '-' + answer
    answer = answer[:-1]
    return answer


def endian_split(answer, endian, negative):
    split_answer = []
    segment = ''
    for i in range(len(answer)):
        segment += answer[i]
        if i % 2 != 0:
            split_answer.append(segment)
            segment = ''
    return endian_formatting(split_answer, endian, negative)


def conv_endian(num, endian='big'):

    if endian not in ['big', 'little']:
        return None
    negative = False
    if num < 0:
        negative = True
        num *= -1
    if num == 0:
        return '0'
    else:
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        answer = ''
        new_answer = ''
        while num != 0:
            remainder = num % 16
            if remainder < 10:
                answer += str(remainder)
            else:
                answer += letters[remainder - 10]
            num = num // 16
    if len(answer) % 2 != 0:
        answer += '0'
    for char in reversed(answer):
        new_answer += char
    return endian_split(new_answer, endian, negative)
