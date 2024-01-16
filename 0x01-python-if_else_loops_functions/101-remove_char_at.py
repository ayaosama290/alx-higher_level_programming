#!/usr/bin/python3
def remove_char_at(str, n):
    holder1 = ""
    holder2 = ""
    if n > len(str):
        return str
    if n < 0:
        return str
    for i in range(len(str)):
        if i == n:
            holder1 = str[:n]
            holder2 = str[n+1:]
            break
    str = holder1 + holder2
    return str
