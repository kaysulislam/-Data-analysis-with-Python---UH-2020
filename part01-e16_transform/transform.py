#!/usr/bin/env python3

def transform(s1, s2):
    s1_int = [int(x) for x in s1.split()]
    s2_int = [int(x) for x in s2.split()]
    zipped_list = list(zip(s1_int, s2_int))
    import math
    result = list(map(math.prod, zipped_list))
    return result


def main():
    pass


if __name__ == "__main__":
    main()
