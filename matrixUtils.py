import numpy as np
import time

def genMatrix(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix

def genMatrix2(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix

def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ' , end='')
        print('')

def writeToFile(matrix, fileName):
    """
    Writes a matrix out to a file
    """

    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')

def readFromFile(fileName):
    """
    Reads a matrix from a file
    """

    matrix = []

    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)

    return matrix

def multiMatrix(a, b):                                                  # requires (n x n) matrices
    length = len(a)                                                     # length of matrix, requires square matrix
    matrix = genMatrix(length, 0)                                       # result matrix filled with 0

    for i in range(length):                                             # rows
        for j in range(length):                                         # columns
            for k in range(length):                                     # index
                matrix[i][j] = a[i][k] * b[k][j]                        # multplication result
    return matrix                                                       #result

def multiMatrixBlocked(a, b):
    length = len(a)
    matrix = genMatrix(length, 0)
    tile_size = 16

    for kk in range(0, length, tile_size):
        for jj in range(0, length, tile_size):
            for i in range(0, length):
                j_end = jj + tile_size
                for j in range(jj, j_end):
                    k_end = kk + tile_size
                    sum = matrix[i][j]
                    for k in range(kk, k_end):
                        sum = a[i][k] * b[k][j]
                    matrix[i][j] = sum
    return matrix

def main():
    """
    Used for running as a script
    """
    size = int(input("Enter the size of the matrix to generate: "))
    if size < 10: size = 10
    valueA = int(input("Enter the value to fill the first array with: "))
    valueB = int(input("Enther the value to fill the second array with: "))

    matA = genMatrix(size, valueA)
    matB = genMatrix(size, valueB)

    start = time.monotonic()                    # time before computation
    matC = multiMatrix(matA, matB)
    elapsed = time.monotonic() - start          # time taken to complete

    start = time.monotonic()
    matC = multiMatrixBlocked(matA, matB)
    elapsed2 = time.monotonic() - start

    printSubarray(matC)
    print("Matrix multiply time: %s seconds" % elapsed)
    print("Matrix multiply blocked time: %s seconds" % elapsed2)

if __name__ == '__main__':
    # execute only if run as a script
    main()
