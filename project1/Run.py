"""
CS2300
PROJECT1
UCCS
27 AUG 2020
DUE 12 SEP 2020
"""

# THE ONLY TIME I USE NUMPY IS FOR .reshape AND PROFESSOR APPROVED THIS IN CLASS
# SEE LINE LINE 28
import numpy


#######################################
# MY FUNCTIONS
#######################################


def matrixRead(filename):
    # Read file information into a list from file
    file = open(filename, 'r')
    file.readline()  # skip the first line
    numbers = []
    for line in file:
        words = line.split()
        numbers.append(words)
    file.close()
    return numbers

def matrixListPrint(file, array, row, cols, name):
    # Open a file and write the matrix to it, with row and col value
    with open(file, 'w') as f:
        f.write(str(name) + ' ' + str(row) + ' ' + str(cols))
        for item in array:
            f.write(' ' + str(item))

def matrixFlat1D(array):
    # Flatten the list back down to 1D from matrix
    newFlatList = []
    for sublist in array:
        for item in sublist:
            # Append all items to new flattened list
            newFlatList.append(item)

    # To see the new flat matrix, use these print values:
    #print('\n' + str(newFlatList))
    #print('\n')
    #print(' '.join(str(n) for n in newFlatList))
    return newFlatList


def matrixReshape(array, name, row, col):
    # Print the list by reshaping it and returns new row/col matrix
    print('\n' + name)
    # ONLY TIME I USED NUMPY AND BILL SAID IT WAS OKAY TO USE HERE
    newArray = numpy.array(array).reshape(row, col)
    print(newArray)
    return newArray


def matrixWrite(file, array, name):
    # Open a file and write the matrix to it (and includes the matrix char)
    with open(file, 'w') as f:
        f.write(str(name) + '\n')
        for item in array:
            f.write("%s\n" % item)


#######################################
# MAIN
#######################################

# Read Raw data from the file
# NOTE that I have two commands (one commented) so you can read in matrixFile.txt instead of practiceData.txt
data_raw = []
data_raw = matrixRead("practiceData.txt")

# First line from the file will be the first list in the list
# Second line is the second matrix (2nd list within the list)
firstMatrix_raw = data_raw[0]
secondMatrix_raw = data_raw[1]

# If these are not the same size, flag the user
if len(firstMatrix_raw) != len(secondMatrix_raw):
    print("WARNING !!! ARRAYS ARE NOT EQUAL. INVALID READ IN OF MATRIX")

# Print out the string of data from files
print(' '.join(str(k) for k in firstMatrix_raw))
print(' '.join(str(k) for k in secondMatrix_raw))

# Chop up the data from the line to (Matrix name, rows, cols)

# First Matrix
firstName = str(firstMatrix_raw[0])
firstRow = firstMatrix_raw[1]
firstCol = firstMatrix_raw[2]

# Delete the first 3 values in the list (we dont need the matrix name, rows, cols in the list anymore)
del firstMatrix_raw[0:3]

# For second line/matrix; Chop up the data from the line to (Matrix name, rows, cols)

# Second Matrix
secondName = secondMatrix_raw[0]
secondRow = secondMatrix_raw[1]
secondCol = secondMatrix_raw[2]

# Again; Delete the first 3 values in the list (we dont need the matrix name, rows, cols in the list anymore)
del secondMatrix_raw[0:3]

# Split the the two matrices from one file, as they were together in one list
firstMatrix_raw = data_raw[0]
secondMatrix_raw = data_raw[1]

# STDOUT (python version though)
# Take first Array and reshape/print it to stdout
new1Array = matrixReshape(firstMatrix_raw, firstName, int(firstRow), int(firstCol))
# Take second Array and reshape/print it to stdout
new2Array = matrixReshape(secondMatrix_raw, secondName, int(secondRow), int(secondCol))

# Write the matrix to the text files:
# NOTE I WAS UNCLEAR HOW THEY WERE SUPPOSED TO BE PRINTED TO THE OUTPUT FILES SO I HAVE TWO VERSIONS:

# First Matrix to firstMatrix.txt
a1FlatMatrix = matrixFlat1D(new1Array)
matrixListPrint("firstMatrix.txt", a1FlatMatrix, firstRow, firstCol, firstName)
# Second Matrix to secondMatrix.txt
a2FlatMatrix = matrixFlat1D(new2Array)
matrixListPrint("secondMatrix.txt", a2FlatMatrix, secondRow, secondCol, secondName)

# USE THIS WAY IF NEED THE FULL MATRIX PRINTED
# matrixWrite("firstMatrix.txt", new1Array, firstName)
# matrixWrite("secondMatrix.txt", new2Array, secondName)

# Instead of copying an existing matrix (for size), it wasn't keeping data since the input has only one char per spot)
# I decided to create a temp matrix that I can resize (I was getting issues originally where my output was only Ints)
tempMatrix = [[0, 0, 0], [0, 0, 0]]
# Lambda function to resize the tempmatrix and make it append 0's to empty spaces otherwise would be empty
rArray = list(map(lambda x: x + ([0] * (int(firstCol) - len(x))),
                  tempMatrix + ([[0] * int(firstCol)] * (int(firstRow) - len(tempMatrix)))))

# Nested For Loops to do 1.5V-2.5S calculation
# i
for i in range(len(new1Array)):
    # j
    for j in range(len(new1Array[0])):
        # 1.5V - 2.5S = R
        newValue = 1.5 * (int(new2Array[i][j])) - 2.5 * (int(new1Array[i][j]))
        # Set newValue to the result array (I had to make two commands here as I was getting an indexing error)
        rArray[i][j] = newValue

# Print calcMatrix to stdout
# Matrix 'R' denotes the resultant calculated matrix
# TO PRINT OUT THE FULL 1.5B - 2.5A EQUATION IN STDOUT:
#print("\n1.5" + str(secondName) + " - 2.5" + str(firstName) + "\n= R")
print('\nR')

# For loop to print
for r in rArray:
    # Print matrix 'R'
    print(r)

#
# Write 1.5V - 2.5S = R to calcMatrix.txt
#
# TO SEE THE MATRIX IN ROWS/COLS FORMAT, UNDO NEXT LINE:
rFlatMatrix = matrixFlat1D(rArray)
matrixListPrint("calcMatrix.txt", rFlatMatrix, firstRow, firstCol, 'R')

# Make a copy of the array to be duplicated (don't want to mess the original up!)
copy = new2Array
# Really cool function to transpose the matrix into a new one called transposedMatrix
transposedMatrix = [[copy[j][i] for j in range(len(copy))] for i in range(len(copy[0]))]

# Print Transposed Matrix to stdout
# Matrix 'V' denotes that it's V Matrix transposed
print('\n' + secondName)
# For loop to print
for t in transposedMatrix:
    # Print Matrix 'T'
    print(t)

#
# Write Transposed matrix to transposedMatrix.txt
#
# TO SEE THE MATRIX IN ROWS/COLS FORMAT, UNDO NEXT LINE:

tFlatMatrix = matrixFlat1D(transposedMatrix)
matrixListPrint("transposedMatrix.txt", tFlatMatrix, secondCol, secondRow, 'T')
