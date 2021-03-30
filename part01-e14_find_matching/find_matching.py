#!/usr/bin/env python3

def find_matching(L, pattern):
    matching_index = []
    for i, value in enumerate(L):
        if(pattern in value):
            matching_index.append(i)
    return matching_index


def main():
    pass


if __name__ == "__main__":
    main()
