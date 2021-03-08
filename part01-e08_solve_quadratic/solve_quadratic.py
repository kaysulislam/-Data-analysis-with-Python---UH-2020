#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    result1 = (-b-math.sqrt(d))/(2*a)
    result2 = (-b+math.sqrt(d))/(2*a)
    return(result1, result2)


def main():
    print(solve_quadratic(1, 5, 6))
    pass


if __name__ == "__main__":
    main()
