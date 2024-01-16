#!/usr/bin/python3
from add_0 import add


def print_add():
    a = 1
    b = 2
    addvar = add(a, b)
    print("{} + {} = {}".format(a, b, addvar))


if __name__ == "__main__":
    print_add()
