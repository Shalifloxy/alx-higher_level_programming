#!/usr/bin/python3

def uppercase(s):
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            uppercase_char = chr(ord(i) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(i), end="")
    print()  # Print a new line after the loop
