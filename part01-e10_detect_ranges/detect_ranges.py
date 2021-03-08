#!/usr/bin/env python3
from itertools import groupby


def detect_ranges(L):
    lst = sorted(L)

    newArray = []
    pos = (j - i for i, j in enumerate(lst))
    t = 0
    for i, els in groupby(pos):
        l = len(list(els))
        el = lst[t]
        t += l
        newArray.append([el, el+l])

    result = []
    for j in newArray:
        if (j[1] - j[0]) == 1:
            result.append(j[0])
        elif (j[1] - j[0]) != 1:
            result.append(tuple(j))

    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(f"Result {result}")


if __name__ == "__main__":
    main()
