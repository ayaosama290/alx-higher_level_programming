#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i == j:
            continue
        elif i+j != 17:
            print("{}{}, ".format(i, j), end="")
        else:
            print("{}{}".format(i, j))
