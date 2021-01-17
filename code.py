#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a Nested Loops program.


import math


def volume(userinput_radius, userinput_height):
    final = userinput_radius * userinput_radius * userinput_height * math.pi
    return final


def main():
    userinput_radius = input("Enter the radius of the cylinder ")
    userinput_height = input("Enter the height of the cylinder ")
    print("")

    try:
        userinput_radius = int(userinput_radius)
        userinput_height = int(userinput_height)
        if userinput_height > 0 and userinput_radius > 0:
            solution = volume(userinput_radius, userinput_height)
            print(("The volume of cylinder with radius {}mm and height {}mm is"
                   "{}mm²").format(userinput_radius, userinput_height,
                                   solution))
        else:
            print("You are not type in positive integer.")
    except Exception:
        print("It is not an integer")


if __name__ == "__main__":
    main()
