#!/usr/bin/env python 3

# Created by: Dahrio Francois
# Created on: November 2020
# this programs calculates the surface area of a cube
#     with user input


def area_surf_cube(side):
    return 6 * side * side

# input


side = int(input("Enter the side of the cube : "))

# process
result = area_surf_cube(side)


# output
print("the surface area of the cube is : " + str(result))

if __name__ == "__area_surf_cube__":
    area_surf_cube(side)
