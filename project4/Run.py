"""
CS2300
PROJECT4
UCCS
DUE 4 DEC 2020
"""

# IMPORTS
import numpy as np
from pprint import pprint

#######################################
# MY FUNCTIONS
#######################################

# Filter through the points list
def getPoints(i, co):
    mat3D = co[i]
    return mat3D


# Return a collection of the assignment coordinates
def getCoords():
    # Provided coordinates in assignment
    coords1 = [10, 10, 10]
    coords2 = [-10, 10, 10]
    coords3 = [10, -10, 10]
    coords4 = [-10, -10, 10]
    # Combine lists into one collection
    coordsAll = [coords1, coords2, coords3, coords4]
    return coordsAll


# Calculate matrix to homogenous points for 3D
def convert3Dp(matrix):
    reshMatr = [[0, 0, 0, 0]]
    matrix.append(1)
    print("Homogenous Points to Intersect Image Plane\t:\t[{} {} {} {}]".format(matrix[0], matrix[1], matrix[2],
                                                                                matrix[3]))
    reshMatr = [[matrix[0], matrix[1], matrix[2], matrix[3]]]
    matrix = reshMatr
    return matrix


# Calculate image coordinates
# Part 1
def image(f, plist):
    # Arguments: f = focal length, plist = point list
    # Start Part 1
    # Loop 4 times to get calculate for all 4 points in coordinates
    for spot in range(0, 4):
        # Set
        focal_l = f
        # Get the the points from assignment
        pointM = getPoints(spot, plist)
        # Print result of new 3D point
        print("\n3D Point For Image Plane Intersection\t\t:\t[{} {} {}]".format(pointM[0], pointM[1], pointM[2]))
        bMatrix = convert3Dp(pointM)
        # Get the new image plane
        projectedM = [0.0, 0.0, 0.0]

        # Set values for T, U, V
        t = (float(pointM[0]) / float(pointM[2]))
        u = focal_l * t
        v = focal_l * (float(pointM[1]) / float(pointM[2]))

        # Set U V and 1 to the new Image Plane Matrix with calculated values
        projectedM[0] = u
        projectedM[1] = v
        projectedM[2] = 1
        print("Image Coordinate Projected Points\t\t\t:\t" + str(projectedM))


#######################################
# MAIN
#######################################

# Limit print options for decimals
np.set_printoptions(precision=3)

# Create a blank template List for future use
calc3D = [0, 0, 0, 0]

# Default for Assignment :
# pi/4
alpha = 45

# IF pi/2 then use the following:
# pi/2
# alpha = 90

sin = np.sin(np.radians(alpha))
cos = np.cos(np.radians(alpha))

# Setup Rotation Matrix
rotationMatrix = [[cos, -sin, 0],
                  [sin, cos, 0],
                  [0, 0, 1],
                  [0, 0, 0]]

# Convert to matrix from list
B = np.array(rotationMatrix)

# Print R Matrix for reference
print("\n\nRotation Matrix Without Translation : ")
print(B)

# Run Part1 of Assignment
# Include value for focal lengths
print("\n\n PART 1 (Focal Length = 1,5)")
image(1, getCoords())
# Print to deliniate between parts
print("\n\n PART 2 (Focal Length = 2 & ROTATION)")
image(5, getCoords())

# Do the same as above but with Part 2 attached
for coordinate in range(0, 4):
    # Setup Focal Length for 3D Plot setup test with F=5
    focal_length = 2
    # Get coordinates from list
    matrix3D = getPoints(coordinate, getCoords())
    # Print the 3D points
    print("\n3D Point For Image Plane Intersection\t\t:\t[{} {} {}]".format(matrix3D[0], matrix3D[1], matrix3D[2]))
    # Duplicate a matrix by converting to projected matrix
    newMatrix = convert3Dp(matrix3D)
    # Calculate the Image Plane Matrix
    imagePlaneMat = [0.0, 0.0, 0.0]
    # Set values for T, U, V
    t = (float(matrix3D[0]) / float(matrix3D[2]))
    u = focal_length * t
    v = focal_length * (float(matrix3D[1]) / float(matrix3D[2]))

    # Set U V and 1 to the new Image Plane Matrix with calculated values
    imagePlaneMat[0] = u
    imagePlaneMat[1] = v
    imagePlaneMat[2] = 1
    # Print New Image Coordinate Point Matrix
    print("Image Coordinate Projected Points\t\t\t:\t" + str(imagePlaneMat))

    # PART 2 BEGINS
    # APPLY MATRIX ROTATION

    # Make a new matrix comprising of the previous made Image Plane Matrix with Focal Point calculation
    noTmatrix = np.array(imagePlaneMat)

    # Take the multiplication / dot product of the two matrices
    # Apply the Rotation Matrix to map the 3D points
    A = np.dot(noTmatrix, B.T)
    # Convert back to list for consistency reasons
    Z = A.tolist()
    # Delete excess matrix overhang
    del Z[-1]
    # Print each rotation for each point
    print("ZRotationTranslationMatrix\t\t\t\t\t:\t<{:.3f}, {:.3f}, {:.3f}>".format(Z[0], Z[1], Z[2]))
    # Set each point (rotated) to new global matrix
    calc3D[coordinate] = Z

# FINISH ROTATION AND GRAPH
# Print the Result
print("\n\nCalculated Rotated Image Coordinates : ")
pprint(calc3D)
# FIN
