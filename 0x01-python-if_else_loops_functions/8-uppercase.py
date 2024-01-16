#!/usr/bin/python3
def uppercase(str):
    h1 = ""
    for i in str:
        for j in range(97, 123):
            if ord(i) == j:
                i = j - 32
                i = chr(i)
                h1 = h1 + i
                break
    return h1
