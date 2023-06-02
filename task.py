
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
    """  """
    pass


# Function 3
def conv_endian(num, endian='big'):
    """  """
    pass
