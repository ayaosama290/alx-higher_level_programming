#!/usr/bin/python3
def uppercase(str):
    h1 = ""
    for i in str:
        if ord(i) == 32:
            h1 = h1 + i
            continue
        elif ord(i) >= 48 and ord(i) <= 57:
            h1 = h1 + i
            continue
        elif ord(i) in range(65, 91):
            h1 = h1 + i
            continue
        else:
            i = ord(i) - 32
            i = chr(i)
            h1 = h1 + i
            continue
    print("{}".format(h1))
