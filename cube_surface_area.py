#!/usr/bin/env python 3

# Created by: Dahrio Francois
# Created on: January 2021
# this programs calculates the surface area of a cube
#     with user input


def main():
    # this function calculates a cube's surface area

    # input
    length = int(input("Enter the length of the cube: "))

    # process
    surface_area = 6*(length**2)

    # output
    print("")
    print("The surface area of this cube is {}m^2".format(surface_area))


if __name__ == "__main__":
    main()
