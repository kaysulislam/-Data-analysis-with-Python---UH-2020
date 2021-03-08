#!/usr/bin/env python3

def interleave(*lists):
    zippedLists = zip(*lists)

    result = []
    for i in list(zippedLists):
        result.append(list(i))
        print(i)
    return sum(result, [])


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
