#!/usr/bin/env python3

def main():
    L = [(x, y) for x in range(1, 7) for y in range(1, 7) if (x + y) == 5]
    for items in L:
        print(items)
    pass


if __name__ == "__main__":
    main()
