#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        userInput = input("Choose a shape (triangle, rectangle, circle): ")
        if userInput == " ":
            break
        elif userInput == "triangle":
            while True:
                try:
                    triangleBase = int(input("Give base of the triangle: "))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    # better try again... Return to the start of the loop
                    continue
                else:
                    break
            while True:
                try:
                    triangleHeight = int(
                        input("Give height of the triangle: "))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    # better try again... Return to the start of the loop
                    continue
                else:
                    break
            triangleArea = 0.5*(triangleBase)*(triangleHeight)
            print(f"The area is {triangleArea}")
        elif userInput == "rectangle":
            while True:
                try:
                    rectangleWidth = int(
                        input("Give width of the rectangle: "))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    # better try again... Return to the start of the loop
                    continue
                else:
                    break
            while True:
                try:
                    rectangleHeight = int(
                        input("Give height of the rectangle: "))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    # better try again... Return to the start of the loop
                    continue
                else:
                    break
            rectangleArea = rectangleWidth * rectangleHeight
            print(f"The area is {rectangleArea}")
        elif userInput == "circle":
            while True:
                try:
                    circleRadius = int(input("Give radius of the circle: "))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    # better try again... Return to the start of the loop
                    continue
                else:
                    break
            circleArea = (math.pi)*(circleRadius)**2
            print(f"The area is {circleArea}")
        else:
            print("unknown shape!")


if __name__ == "__main__":
    main()
