#!/usr/bin/python3

def uppercase(s):
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()  # Print a new line after the loop
