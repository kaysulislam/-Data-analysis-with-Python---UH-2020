#!/usr/bin/env python3

def sum_equation(L):
    if(len(L) != 0):
        L_sum = str(sum(L))
        L_digits = " + ".join(str(x) for x in L)
        result = str(L_digits + " = " + L_sum)
        return result
    else:
        return "0 = 0"


def main():
    pass


if __name__ == "__main__":
    main()
