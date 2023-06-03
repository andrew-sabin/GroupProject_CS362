
import string  # for easier importing of digits & characters


# Function 1
def conv_num(num_str):
    """
    Not Possible
    a) no characters
    b) empty space present
    c) 1-character string is not a digit
    d) +/- hex prefix but nothing afterwards
    e) 2 characters & 1 is any letter (no way to fit in a hex prefix
    f) 2 or more decimal points/periods
    g) hex prefix but letter is g to z
    h) punctuation that is not '.' is present

    Possible
    1. decimal yes, negative no, hex no => positive float
    2. decimal no, negative no, hex no => only digits
    3. decimal yes, negative yes, hex no => negative float
    4. decimal no, negative yes, hex no => negative, only digits
    X. decimal yes, negative no, hex yes => rubric says NOT a valid hex input
    5. decimal no, negative no, hex yes => positive hexadecimal
    X. decimal yes, negative yes, hex yes => rubric says NOT a valid hex input
    6. decimal no, negative yes, hex yes => negative hexadecimal """
    # if no character
    if num_str == '':
        return None
    # if empty space in num_str
    elif ' ' in num_str:
        return None
    # if 1-character string is not a digit
    elif len(num_str) == 1 and num_str[0] not in string.digits:
        return None
    # if string is only hexadecimal start with nothing else after
    elif num_str == '0x' or num_str == '-0x':
        return None
    # if 2 characters (so no way for hexadecimal prefix) and one of the
    # characters is a letter
    elif num_str == 2 and (num_str[0] in string.ascii_lowercase or num_str[
        0] in string.ascii_uppercase) or (num_str[1] in
                                          string.ascii_lowercase or num_str[0]
                                          in string.ascii_uppercase):
        return None
    # if more than 1 period
    elif num_str.count('.') >= 2:
        return None
    # Case 1: if 1 decimal, no neg, no hex
    elif num_str.count('.') == 1 and num_str.count('-') == 0 & \
            num_str.count('x') == 0:
        if num_str[-1] == '.':
            # self.assertEqual(conv_num('123.'), 123.0)
            num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                        '7': 7, '8': 8, '9': 9}
            place_value = len(num_str) - 1
            answer = 0
            for i in range(len(num_str) - 1):
                if num_str[i] not in string.digits:
                    return None
                add_to_answer = num_dict[num_str[i]] * 10 ** (place_value - 1)
                answer += add_to_answer
                place_value -= 1
            answer += 0.0
            return answer
        elif num_str[0] == '.':
            # self.assertEqual(conv_num('.45'), 0.45)
            num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                        '7': 7, '8': 8, '9': 9}
            place_value = 1
            answer = 0
            for i in range(1, len(num_str)):
                if num_str[i] not in string.digits:
                    return None
                add_to_answer = num_dict[num_str[i]] * 10 ** (-1 * (
                    place_value))
                answer += add_to_answer
                place_value += 1
            return answer

    # Case 2: if no decimal, no negative, no hexadecimal
    elif num_str.count('.') == 0 and num_str.count('-') == 0 and \
            num_str.count('x') == 0:
        # self.assertEqual(conv_num('12345'), 12345)
        num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                    '7': 7, '8': 8, '9': 9}
        place_value = len(num_str)
        answer = 0
        for character in num_str:
            if character not in string.digits:
                return None
            add_to_answer = num_dict[character] * 10**(place_value - 1)
            answer += add_to_answer
            place_value -= 1
        return answer

    # Case 3: decimal yes, negative yes, hex no => negative float
    elif (num_str.count('.') == 1 and num_str.count('-') == 1) and \
            (num_str[0] == '-' and num_str.count('x') == 0):
        if num_str[-1] == '.':
            # self.assertEqual(conv_num('-123.45'), -123.45)
            num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                        '7': 7, '8': 8, '9': 9}
            place_value = len(num_str) - 1
            answer = 0
            # starts at index 1 because index 0 = negative sign
            for i in range(1, len(num_str) - 1):
                if num_str[i] not in string.digits:
                    return None
                add_to_answer = num_dict[num_str[i]] * 10 ** (place_value - 1)
                answer += add_to_answer
                place_value -= 1
            answer += 0.0
            return answer
        # -.45 is not a valid number.
        elif num_str[0:2] == '-.':
            return None
        # Example: -0.45 has period in index 2
        elif num_str[2] == '.':
            if num_str == '-0.':
                return None
            # self.assertEqual(conv_num('.45'), 0.45)
            num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                        '7': 7, '8': 8, '9': 9}
            place_value = 1
            answer = 0
            for i in range(3, len(num_str)):
                if num_str[i] not in string.digits:
                    return None
                add_to_answer = num_dict[num_str[i]] * 10 ** (-1 * (
                    place_value))
                answer += add_to_answer
                place_value += 1
            return answer
    # Case 4: Negative Digits... decimal no, negative yes, hex no => negative
    # only digits
    elif num_str.count('.') == 0 and num_str.count('-') == 1 and \
            num_str[0] == '-' and num_str.count('x') == 0:
        num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                    '7': 7, '8': 8, '9': 9}
        place_value = len(num_str) - 1
        answer = 0
        for i in range(1, len(num_str)):
            if num_str[i] not in string.digits:
                return None
            add_to_answer = num_dict[num_str[i]] * 10 ** (place_value - 1)
            answer += add_to_answer
            place_value -= 1
        return answer
    # Case 5: Positive Hexadecimal... decimal no, negative no, hex yes =>
    # positive hexadecimal
    # elif len(num_str) >= 3 and num_str[0:2] == '0x':

    # Case 6: Negative Hexadecimal... decimal no, negative yes, hex yes =>
    # negative hexadecimal
    # elif len(num_str) >= 4 and num_str[0:3] == '-0x':

    # if not in the 6 Cases:
    else:
        return None


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

    # set curr_month to be equal to the amount of days set in the months_year
    curr_month = months_year[str(month)]

    # set while loop to increase in days and decrease in seconds per 86400 seconds until
    # num_sec is no longer greater or equal to 36399
    while num_sec > 86399:
        num_sec -= 86400
        day += 1
        if day > curr_month:
            month += 1
            day = 1
        # if statement to see if day of the year is 2 for february
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

    # date_to_string() takes the month, day, and year variables
    # and returns a string with the date formatted as 'MM-DD-YYYY'
    def date_to_string(month, day, year):
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
    string_date = date_to_string(month, day, year)
    return string_date


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
