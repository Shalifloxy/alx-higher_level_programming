#!/usr/bin/python3

for char in range(ord('z'), ord('A') - 1, -1):
    print('{:c}'.format(char if char % 2 == 1 else char + 32), end='')
