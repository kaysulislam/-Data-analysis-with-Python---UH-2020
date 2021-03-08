#!/usr/bin/env python3

from typing import List


def merge(L1, L2):
    mergedList = [*L1, *L2]
    newSorted = []
    for i in range(len(mergedList)):
        minNum = min(mergedList)
        newSorted.append(minNum)
        mergedList.remove(minNum)
    return [newSorted][0]


def main():
    L1 = [1, 5, 8]
    L2 = [6, 8, 9]
    L = merge(sorted(L1), sorted(L2))
    print(L)
    pass


if __name__ == "__main__":
    main()
