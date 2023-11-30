#!/usr/bin/python3

for char in range(ord('z'), ord('A') - 1, -1):
    if char % 2 == 1:
        print(chr(char), end='')
    else:
        print(chr(char), end='')
