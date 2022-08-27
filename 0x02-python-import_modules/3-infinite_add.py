#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    resultAll = 0
    for a in range(1, len(argv)):
        resultAll = resultAll + int(argv[a])
    print(resultAll)
