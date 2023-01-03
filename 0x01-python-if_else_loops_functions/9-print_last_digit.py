#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        print(0, end='')
        return
    if number < 0:
        pos_num = number * 1
        neg_str = str(pos_num)
        neg_last_digit_str = neg_str[-1]
        neg_last_digit_num = int(neg_last_digit_str)
        print(neg_last_digit_num, end='')
        return
    num_str = str(number)
    last_str = num_str[-1]
    last_digit = int(last_str)
    (print(last_digit, end=''))
