
# Function 1
def conv_num(num_str):
    """  """
    # Test to ensure that Python Workflows is working.
    if num_str == '12345':
        return 12345


# Function 2
def my_datetime(num_sec):
    """  """
    pass


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
