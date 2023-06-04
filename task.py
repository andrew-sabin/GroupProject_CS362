
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
    """  """
    pass


# Function 3
def conv_endian(num, endian='big'):
    """  """
    pass


print(conv_num('0xAD4'))
