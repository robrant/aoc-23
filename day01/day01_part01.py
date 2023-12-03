import re

f = open("./day01/day01_part01_input.txt", 'r')
data = []
valid_pswds = []
invalid_pswds = []

def get_first_digit(cal_val: str) -> int:
    """ Gets first digit """
    digits = re.findall(r'^\D*(\d)', cal_val)
    if len(digits) == 0:
        raise IndexError
    else:
        first_digit = int(digits[0])
    return first_digit

def get_last_digit(cal_val: str) -> int:
    """ Gets last digit """
    digits = re.findall(r'(\d)', cal_val)
    if len(digits) == 0:
        raise IndexError
    else:
        last_digit = int(digits[-1])
    return last_digit

total_cal_value = 0

for line in f.readlines():
    line = line.strip()
    first = get_first_digit(line)
    last = get_last_digit(line)
    cal_val = int(str(first) + str(last))
    print(line, first, last, cal_val)
    total_cal_value += cal_val

print (total_cal_value)
