"""
CS2300
PROJECT2
UCCS
16 SEP 2020
DUE 04 OCT 2020
"""

# IMPORTS
import math


#######################################
# MY FUNCTIONS
#######################################

# START HERE IF PARAMETRIC
def parametric(data):
    # Use the 1st, 2nd, 3rd, 4th spots after the letter to preload p and v
    p1 = float(data[1])
    p2 = float(data[2])
    v1 = float(data[3])
    v2 = float(data[4])

    # PRINT (using p and v values)
    print(f'Parametric Form :\t\tl(t) = [{p1},{p2}] + t[{v1},{v2}]')
    a = -1 * v2
    b = v1
    c = -1 * ((a * p1) + (b * p2))
    # PRINT Implicit Form
    print(f'Implicit Form :\t\t\t{a}x1 + {b}x2 + {c} = 0')
    normal(a, b, c)

    distance = 0
    # Step through each of the remainder of the data points in the file
    # This part took the longest but I finally realized to step using +2
    for x in range(5, 10, 2):
        # Get the first point
        x1 = x
        # Get the second point
        x2 = x + 1

        # Get the point value from the exact spots in input list
        point1 = float(data[x1])
        point2 = float(data[x2])

        # calculate distance for these three and return d (the actual distance)
        d = distanceLine(point1, point2, a, b, c)

        # IF d is 0 then it is on the line, otherwise just print its normal value.
        if d != 0:
            print("Distance from point [{:0.2f},{:0.2f}]\tto the line is {:0.2f}.".format(point1, point2, d))
        elif d == 0:
            # Print the distance normally
            print('Distance from point [{:0.2f},{:0.2f}]\tto the line is {:0.2f}. The point is on the line.'.format(
                point1, point2, d))


# START HERE IF IMPLICIT
def implicit(data):
    # Use the 1st, 2nd, 3rd spots after the letter to preload a, b, c
    a = float(data[1])
    b = float(data[2])
    c = float(data[3])

    # Print the implicit form with the a b c values obtained
    print('Implicit Form :\t\t\t{:0.2f}x1 + {:0.2f}x2 + {:0.2f} = 0'.format(a, b, c))

    p1 = 0
    v1 = -1 * b
    v2 = a

    # FIX NEGATIVE SIGNS
    v1 = v1 * -1
    v2 = v2 * -1

    # Solve for X and find what X is using V and C
    num = solveForX(c, v1, v2)
    p2 = num

    # FIX NEGATIVE SIGNS
    p2 = p2 * -1
    p2 = abs(p2)

    # Print the parametric form with all new values
    print('Parameter Form :\t\tl(t) = [{:0.2f},{:0.2f}] + t[{:0.2f},{:0.2f}]'.format(p1, p2, v1, v2))
    normal(a, b, c)

    distance = 0
    # Step through each of the remainder of the data points in the file
    # Similar to above but since there are less used initial data points, we have to start at the 4th point
    # This part took the longest but I finally realized to step using +2
    for x in range(4, 9, 2):
        x1 = x
        x2 = x + 1

        # Get the point value from the exact spots in input list
        point1 = float(data[x1])
        point2 = float(data[x2])

        # calculate distance for these three and return d (the actual distance)
        d = distanceLine(point1, point2, a, b, c)

        # IF d is 0 then it is on the line, otherwise just print its normal value.
        if d != 0:
            print("Distance from point [{:0.2f},{:0.2f}]\tto the line is {:0.2f}.".format(point1, point2, d))
        elif d == 0:
            # Print the distance normally
            print('Distance from point [{:0.2f},{:0.2f}]\tto the line is {:0.2f}. The point is on the line.'.format(
                point1, point2, d))


def distanceLine(x1, y1, a, b, c):
    # Find the distance from the line from two points
    d = ((a * x1) + (b * y1) + (c)) / abs(math.sqrt((a * a) + (b * b)))
    return d


def normal(a1, b1, c):
    # Get point-normal form of the line
    # Set the denom to ||a|| = (a^2 + b^2)^2
    denom = abs(math.sqrt((a1 * a1) + (b1 * b1)))
    # Do all elements divided by ||a||
    x1 = a1 / denom
    x2 = b1 / denom
    c1 = c / denom
    # Print these new values into point-normal form
    print('Point-Normal Form :\t\t{:0.2f}a + {:0.2f}b + {:0.2f} = 0\n'.format(x1, x2, c1))
    # return this denom value
    return denom


def solveForX(c, b1, a2):
    # Solve for P by setting p1 to 0 and seeing what the value becomes
    # preset nNum just incase
    nNum = 1.0
    # Set the a2 val to 0 to use 0
    fA = a2 * 0
    # ready b for the formula
    fB = b1
    # make c negative
    fC = c * (-1.0)
    # Solve the formula for -C+0/B
    formula = (fC + fA) / (fB)
    nNum = formula
    # Return nNum (formula result)
    return nNum


#######################################
# MAIN
#######################################


# Read file information into a list from file
file = open("s_input.txt", 'r')
# Premake the list
numbers = []
# For every line in the file, read in the data
for line in file:
    # Chop up the line into pieces
    words = line.split()
    # Clear the list ahead of time (otherwise I'd get lists in a list)
    numbers.clear()
    # Add the new words to the list
    numbers.append(words)
    # Shorten the list (since it is a list in a list because it was appended)
    data_raw = numbers[0]
    # Made a new list a now we will print the input as we saw it in the text file
    # PRINT
    print('\n')
    print(' '.join(str(n) for n in data_raw))
    # IF it is 'p' then it is parametric already, and follow those steps
    if str(data_raw[0][0]) == 'p':
        parametric(data_raw)
    # IF it is 'i' then it is implicit and we just do those steps
    elif str(data_raw[0][0]) == 'i':
        implicit(data_raw)
    else:
        print('\nERROR !!! DETECTED INVALID INPUT FROM FILE !!!')
file.close()
