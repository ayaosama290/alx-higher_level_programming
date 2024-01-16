#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        ans = number % 10
        print("{}".format(ans), end="")
        return ans
    elif number < 0:
        ans = (number % -10) * -1
        print("{}".format(ans), end="")
        return ans
    else:
        print("{}".format(0), end="")
        return 0
