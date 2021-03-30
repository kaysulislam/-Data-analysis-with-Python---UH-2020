#!/usr/bin/env python3

def distinct_characters(L):
    my_d = {}
    for i in L:
        newRecord = {i: len(set(i))}
        my_d.update(newRecord)
    return my_d


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
