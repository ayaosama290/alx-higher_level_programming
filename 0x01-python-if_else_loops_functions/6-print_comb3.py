#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i == j:
            continue
        elif i+j != 17:
            print(f"{i}{j}, ", end="")
        else:
            print(f"{i}{j}")
