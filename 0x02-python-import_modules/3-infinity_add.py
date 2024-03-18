#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    total = 0

    x = len(argv) - 1

    for i in range(1, x+1):
        total += int(argv[i])
    print("{}". format(total))
