#!/usr/bin/python3
import sys


def func():
    add = 0
    for i in range(1, len(sys.argv)):
        add = add + int(sys.argv[i])
    print(add)


if __name__ == "__main__":
    func()
