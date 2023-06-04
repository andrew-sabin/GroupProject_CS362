# Function 1
import string  # for easier importing of digits & characters


def conv_num(num_str):
    """ Takes in a string of characters that should represent either an
    integer, a float, or a hexadecimal number that represents an integer.

    If the string does not represent a valid integer or float or hexadecimal
    representing an integer, then it returns None. Else, the string is
    converted to a valid integer or float. """

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

    # Case 4: Negative Integers... decimal no, negative yes, hex no
    elif num_str.count('.') == 0 and num_str.count('-') == 1 and \
            num_str[0] == '-' and num_str.count('x') == 0:
        return negative_integer(num_str)

    # Case 5: Positive Hexadecimal... decimal no, negative no, hex yes
    elif len(num_str) >= 3 and num_str[0:2] == '0x' and num_str.count('.') \
            == 0 and num_str.count('-') == 0:
        return positive_hexadecimal(num_str)

    # Case 6: Negative Hexadecimal... decimal no, negative yes, hex yes
    elif len(num_str) >= 4 and num_str[0:3] == '-0x':
        return negative_hexadecimal(num_str)

    # if not in the 6 Cases, such as Positive/Negative Float Hexadecimals:
    else:
        return None


def is_valid_conv_num_str(num_str):
    """ Returns True if the num_str is valid for converting into an integer
    or a float. Returns False is the num_str is not valid. Not Valid includes:
    a) no characters
    b) empty space present
    c) 1-character string is not a digit
    d) +/- hex prefix but nothing afterwards
    e) 2 characters & 1 is any letter (cannot fit a hex prefix if length of 2)
    f) 2 or more decimal points/periods
    g) hex prefix but letter is g to z OR G to Z
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
    # if 2 characters (no hex prefix) and one of the characters is a letter
    elif len(num_str) == 2 and ((num_str[0] in string.ascii_lowercase or
                                num_str[0] in string.ascii_uppercase) or
                                (num_str[1] in string.ascii_lowercase or
                                 num_str[1] in string.ascii_uppercase)):
        return False
    # if more than 1 period
    elif num_str.count('.') >= 2:
        return False
    else:
        return True


def conv_int_or_hex_helper(num_str, allowed_digits, start, end,
                           place_value, multiplier):
    """ Takes in a string representing an integer or a hexadecimal and
    converts it to an integer to return. Sometimes returns an integer that
    is later added to 0.0 to convert to a float.
    a) num_str = string to convert
    b) allowed_digits = integer or hex digits, with string module as a shortcut
    c) start = starts when the string index starts at the actual number
    - depends on hex prefix, decimal point, negative sign
    d) end = ends when the string index is done with the actual number
    - depends on if decimal point is the last index or not
    e) place_value = determines the power of 10 if integer or 16 if hexadecimal
    f) multiplier = 10 if integer, 16 if hex
    - For example: '12345' means that '1' is 1 * 10**4, as place_value
    starts at 5 - 1 = 4 because the length of the string is 5. """
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


def conv_float_helper(num_str, place_value, start, decimal_index):
    """ Takes in a string representing a number with a decimal point
    represented by a period. Converts into a float.
    a) num_str = string to convert
    b) place_value = determines the power of 10 for the characters that
    represent the numbers to the left of the decimal point
    c) start = starts when the string index starts at the actual number
    - depends on decimal point, negative sign
    d) decimal_index = determines where to stop calculating the integer &
    start calculating the tenths, hundredths, ... place
    -1.45 => '1' = 1 * 10**1, '4' = 4 / 10**1, '5' = 5 / 10**2 """
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
                'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12,
                'd': 13, 'e': 14, 'f': 15}
    answer = 0
    for i in range(start, decimal_index):
        if num_str[i] not in string.digits:
            return None
        answer += hex_dict[num_str[i]] * 10 ** place_value
        place_value -= 1

    decimal_place_value = 1
    for j in range(decimal_index + 1, len(num_str)):
        if num_str[j] not in string.digits:
            return None
        answer += (hex_dict[num_str[j]] / (10 ** decimal_place_value))
        decimal_place_value += 1
    return answer


def positive_float(num_str):
    """ Positive Float = decimal yes, negative no, hex no """
    # If the decimal point is at the end of the string.
    if num_str[-1] == '.':
        answer = conv_int_or_hex_helper(num_str, string.digits, 0,
                                        len(num_str) - 1, len(num_str) - 1, 10)
    # Elif decimal point is at the beginning of the string.
    elif num_str[0] == '.':
        answer = conv_float_helper(num_str, 1, 1, 0)
    # Else decimal point is somewhere in the middle of the string.
    else:
        decimal_index = num_str.index('.')
        answer = conv_float_helper(num_str, decimal_index - 1,
                                   0, decimal_index)
    return None if answer is None else answer + 0.0  # converts answer to float


def positive_integer(num_str):
    """ Positive Integer = decimal no, negative no, hex no """
    return conv_int_or_hex_helper(num_str, string.digits, 0, len(num_str),
                                  len(num_str), 10)


def negative_float(num_str):
    """ Negative Float = decimal yes, negative yes, hex no """
    # If the decimal point is at the end of the string.
    if num_str[-1] == '.':
        answer = conv_int_or_hex_helper(num_str, string.digits, 1,
                                        len(num_str) - 1, len(num_str) - 2,
                                        10)
    elif num_str[0:2] == '-.':
        return None  # Example: -.45 is not a valid number.
    elif num_str[2] == '.':
        if num_str == '-0.':
            return None  # Example: -0.45 has period in index 2
        answer = conv_float_helper(num_str, 1,
                                   1, 2)
    else:  # Else decimal point is in the middle of the string
        decimal_index = num_str.index('.')
        answer = conv_float_helper(num_str, decimal_index - 2,
                                   1, decimal_index)
    return None if answer is None else (answer + 0.0) * -1  # neg float


def negative_integer(num_str):
    """ Negative Integer = decimal no, negative yes, hex no """
    answer = conv_int_or_hex_helper(num_str, string.digits, 1, len(num_str),
                                    len(num_str) - 1, 10)
    return None if answer is None else answer * -1  # convert to neg


def positive_hexadecimal(num_str):
    """ Positive Hex = decimal no, negative no, hex yes """
    return conv_int_or_hex_helper(num_str, string.hexdigits, 2, len(num_str),
                                  len(num_str) - 2, 16)


def negative_hexadecimal(num_str):
    """ Negative Hex = decimal no, negative yes, hex yes """
    answer = conv_int_or_hex_helper(num_str, string.hexdigits, 3, len(num_str),
                                    len(num_str) - 3, 16)
    return None if answer is None else answer * -1  # convert to neg
