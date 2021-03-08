#!/usr/bin/env python3
def triple(x):
    return x*3


def square(x):
    return x**2


def main():
    for i in range(1, 11):
        tripleValue = triple(i)
        squareValue = square(i)
        if (squareValue > tripleValue):
            break
        else:
            print(f"triple({i})=={tripleValue} square({i})=={squareValue}")


if __name__ == "__main__":
    main()
