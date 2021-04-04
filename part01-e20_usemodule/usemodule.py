#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    # Call the functions from here
    triangle.hypothenuse(50, 40)
    triangle.area(50, 40)


if __name__ == "__main__":
    main()
