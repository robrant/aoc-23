import re

f = open("./day01/day01_part01_input.txt", 'r')
data = []
valid_pswds = []
invalid_pswds = []

def get_numerical_digit(digit: str) -> int:
    """ Retrieves the numerical digit """

    lookup = {"one":1,
              "two":2,
              "three":3,
              "four":4,
              "five":5,
              "six":6,
              "seven":7,
              "eight":8,
              "nine":9}

    return lookup[digit]

def get_first_digit(cal_val: str) -> int:
    """ Gets first digit where the digit can be numerical or text """

    # Set the min index to be the length of the input
    min_index = len(cal_val)
    match_value = None

    # Find the lowest index position of a number word
    for num in ['one','two','three','four','five','six','seven','eight','nine']:
        matched_text = re.finditer(rf'({num})', cal_val)
        for candidate in matched_text:
            match_idx = candidate.start()
            if match_idx < min_index:
                min_index = match_idx
                match_value = candidate.group()
    
    if match_value:
        match_value = get_numerical_digit(match_value)

    # Find the lowest index position of a number digit
    pattern = r'(\d)'
    matched_numbers = re.finditer(pattern, cal_val)
    for candidate in matched_numbers:
        match_idx = candidate.start()
        if match_idx < min_index:
            min_index = match_idx
            match_value = candidate.group()

    return int(match_value)

def get_last_digit(cal_val: str) -> int:
    """ Gets last digit where the digit can be numerical or text """

    # Set the min index to be the length of the input
    min_index = -1
    match_value = None

    # Find the lowest index position of a number word
    for num in ['one','two','three','four','five','six','seven','eight','nine']:
        matched_text = re.finditer(rf'({num})', cal_val)
        for candidate in matched_text:
            match_idx = candidate.start()
            if match_idx > min_index:
                min_index = match_idx
                match_value = candidate.group()

    if match_value:
        match_value = get_numerical_digit(match_value)

    # Find the lowest index position of a number digit
    pattern = r'(\d)'
    matched_numbers = re.finditer(pattern, cal_val)
    for candidate in matched_numbers:
        match_idx = candidate.start()
        if match_idx > min_index:
            min_index = match_idx
            match_value = candidate.group()

    return int(match_value)


if __name__ == '__main__':

    total_cal_value = 0

    for line in f.readlines():
        line = line.strip()
        first = get_first_digit(line)
        last = get_last_digit(line)
        cal_val = int(str(first) + str(last))
        print(line, first, last, cal_val)
        total_cal_value += cal_val

    print (total_cal_value)
