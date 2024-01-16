#!/usr/bin/python3
def print_tebahpla():
    for i in range(122, 96, -1):
        if i % 2 == 0:
            pass
        else:
            i = i - 32
        print(chr(i), end="")
