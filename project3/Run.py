"""
CS2300
PROJECT3
UCCS
DUE 13 NOV 2020
"""

# IMPORTS
import numpy as np
import time


#######################################
# MY FUNCTIONS
#######################################

def calcVector(matrix):
    calc = 3
    # DO DET CALC
    # calculating the determinant of matrix
    det = np.linalg.det(matrix)

    print("\nCalculating Vector Subspace of Linear Combination ... ")
    calc = det

    if calc == 0:
        # If 0, then the 3rd vector is in subspace
        # print("det() = 0")
        return 0
    elif calc == 1:
        # If not 0, then no it is not in the subspace
        # print("det() != 0")
        return 1
    elif calc != 1 or 0:
        # print("det() == " + str(det))
        return det


#######################################
# MAIN
#######################################

# Welcome
print("--------------------------------------------------------------")
print("\n@ UCCS\nCS 2300 PROJECT (3)\n")
print("--------------------------------------------------------------")


# VARS DATA POINTS FOR INPUT
p1 = [1, 0, 1, 0, 1, 0, 15, -10, 15]
p2 = [6.9, 0, 0, 0, -3.2, 0, 1.5, -6.2, 0.37]
p3 = [-3, 3, 4, 0, 1, 0, -6, 4, -8]
p4 = [-3, 3, 4, 1, 1, 1, 1, 7, 8]

# TEMPS
tempInput = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# v1 = [0,0,0]
# v2 = [0,0,0]
# c1 = [0,0,0]

# ASK USER WHICH PROBLEM HE WANTS TO CHECK
print("\nHere are the four inputs our professor included to test for our assignment/Project3 : ")
print("[1] = 1, 0, 1, 0, 1, 0, 15, -10, 15")
print("[2] = 6.9, 0, 0, 0, -3.2, 0, 1.5, -6.2, 0.37")
print("[3] = -3, 3, 4, 0, 1, 0, -6, 4, -8")
print("[4] = -3, 3, 4, 1, 1, 1, 1, 7, 8")

print(f"\n.\n.\n.\n")
# HE APPROVED IT IN CLASS, WE CAN DO IT THIS WAY
problem = int(input("\nWhich of the four inputs do you wish to test? Options are :\n[1] [2] [3] or [4] ?\n\n >"))

if problem == 1:
    tempInput = p1
elif problem == 2:
    tempInput = p2
elif problem == 3:
    tempInput = p3
elif problem == 4:
    tempInput = p4
elif problem != 1 or 2 or 3 or 4 or 5:
    print("WARNING !!! Unknown input and or selection !!!")
    print("ENDING PROGRAM... GOODBYE")
    time.sleep(2)
    exit()

# CALCULATION
v1 = [tempInput[0], tempInput[1], tempInput[2]]
v2 = [tempInput[3], tempInput[4], tempInput[5]]
c1 = [tempInput[6], tempInput[7], tempInput[8]]

# Print them
print(f"\nBasis Set = <{v1}>, <{v2}> and candidate vector <{c1}>")

# Combine Vectors into 3x3 matrix
tMatrix = np.array([[v1[0], v2[0], c1[0]],
                    [v1[1], v2[1], c1[1]],
                    [v1[2], v2[2], c1[2]]])

# Displaying the Matrix
print("\nR3 :")
print(tMatrix)

# Calculate determinant of matrix
result = calcVector(tMatrix)

# PRINT
if result == 0:
    print(f"Yes, the vector <{c1}> is in the subspace spanned by <{v1}> <{v2}>\n\n")
else:
    print(f"No, the vector <{c1}> is not in the subspace.\n\n")
