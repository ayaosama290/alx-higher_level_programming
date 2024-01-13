#!/usr/bin/python3
startChar = 'a'
endChar = 'z'
startChar = ord(startChar)
endChar = ord(endChar) + 1
for i in range(startChar, endChar):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    else:
        print("{}".format(chr(i)),end="")
