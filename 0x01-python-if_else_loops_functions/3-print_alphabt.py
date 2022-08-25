#!/usr/bin/python3
for alpha in range(97, 123):
    if chr(alpha) != 112 and chr(alpha) != 101:
        print("{}".format(chr(alpha)), end="")
