#!/usr/bin/env python3


def main():
    numRange = list(range(1, 11))
    for i in range(1, 11):
        multiplied_list = [element * i for element in numRange]
        print(*multiplied_list, sep='\t')
    pass


if __name__ == "__main__":
    main()
