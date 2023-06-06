# Function 1 Alwin Nocom
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

    # if not in the 6 Cases:
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
    # converts answer to float
    decimal_index = num_str.index('.')
    return None if answer is None else round((answer + 0.0), 10 - decimal_index)


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
    else:  # Else decimal point is in the middle of the string
        decimal_index = num_str.index('.')
        answer = conv_float_helper(num_str, decimal_index - 2,
                                   1, decimal_index)
    decimal_index = num_str.index('.')
    # neg float
    return None if answer is None else (round(((answer)), 10 - (decimal_index-1)) + 0.0) * -1


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
    return None if answer is None else answer * -1


# Function 2 Andrew Sabin
def my_datetime(num_sec):
    """ Returns a mm-dd-yyyy date based on the number of seconds in days after 01-01-1970
    where num_sec represents the number of seconds placed into the function. """
    # default values for month, day, year based on 01-01-1970
    month = 1
    day = 1
    year = 1970

    # dictionary for the days of each month for normal years
    # key is the month, value is the amount of days in that month
    months_year = {'1': 31, '2': [28, 29], '3': 31, '4': 30, '5': 31,
                   '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

    # curr_month to be equal to the amount of days set in the months_year
    curr_month = months_year[str(month)]

    # while loop to increase in days and decrease in seconds for num_sec per 86400 seconds
    # until num_sec is no longer greater or equal to 36399
    # resets days to 1 if larger than curr_month and month back to 1 if month is larger than 12
    # once month reaches 2 it checks to see if the year is a leap year and curr_month to 28 if not and 29 if it is
    while num_sec > 86399:
        num_sec -= 86400
        day += 1
        if day > curr_month:
            month += 1
            day = 1
            if month > 12:
                month = 1
                year += 1
                curr_month = months_year[str(month)]
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    curr_month = months_year['2'][1]
                else:
                    curr_month = months_year['2'][0]
            else:
                curr_month = months_year[str(month)]

    return date_to_string(month, day, year)


def date_to_string(month, day, year):
    """Helper function for my_datetime that takes in the day, month, and year variables to be
    placed into a calander date format of MM-DD-YYYY."""
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    if day < 10:
        str_day = '0'+str(day)
    else:
        str_day = str(day)
    mmDdYy = str_month + '-' + str_day + '-' + str(year)

    return mmDdYy


# Function 3  Christopher O Neill
def endian_formatting(split_answer, endian, negative):
    """This function properly formats the answer as a hex including
    endian into account and adding spaces where needed."""
    answer = ''
    # If little edian reverse list
    if endian == 'little':
        split_answer.reverse()
    # Format answer with characters properly grouped
    for element in split_answer:
        answer += element
        answer += ' '
    # Add negative if needed
    if negative is True:
        answer = '-' + answer
    # Remove extra space added at end of string
    answer = answer[:-1]
    return answer


def endian_split(answer, endian, negative):
    """Takes the hex and splits it into two characters per element in a list
    to allow for proper formating"""
    split_answer = []
    segment = ''
    # Add each pair of characters as an element to the list
    for i in range(len(answer)):
        segment += answer[i]
        if i % 2 != 0:
            split_answer.append(segment)
            segment = ''
    return endian_formatting(split_answer, endian, negative)


def conv_endian(num, endian='big'):
    # return None if endian is not big or little
    if endian not in ['big', 'little']:
        return None
    negative = False
    # Check if number is negative, flag it and make positive if so
    if num < 0:
        negative = True
        num *= -1
    # Return '0' if number is 0
    if num == 0:
        return '0'
    else:
        # convert to unformatted hex string
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
    # add leading zero if needed
    if len(answer) % 2 != 0:
        answer += '0'
    for char in reversed(answer):
        new_answer += char
    return endian_split(new_answer, endian, negative)
