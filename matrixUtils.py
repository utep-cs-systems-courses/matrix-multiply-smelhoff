# Seth Melhoff
import pymp
import argparse
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

def multiMatrix(a, b):                              # requires (n x n) matrices
    rowsA = len(a)      # Rows in matrix a
    rowsB = len(b)      # Rows in matrix b
    colsA = len(a[0])   # Cols in matrix a
    colsB = len(b[0])   # Cols in matrix b
    
    # For dot product colsA must equal rowsB,
    # and the result matrix will be (rowsA x colsB),
    # but we are only using square matrices,
    # so checking isn't that important.
    if colsA != rowsB:
        return None
    
    matrix = genMatrix(rowsA, 0)                    # result matrix filled with 0

    for i in range(rowsA):                          # rows
        for j in range(colsB):                      # columns
            for k in range(colsA):                  # index
                matrix[i][j] += a[i][k] * b[k][j]   # multplication result
    return matrix                                   #result

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
                        sum = sum + a[i][k] * b[k][j]
                    matrix[i][j] = sum
    return matrix

def multiMatrixBlockedParallel(a, b):
    length = len(a)
    matrix = pymp.shared.array((length, length), dtype=int)
    tile_size = 16

    with pymp.Parallel() as p:
        print(f'Matrix multiply blocked on thread: {p.thread_num} of {p.num_threads}')
        for kk in p.range(0, length, tile_size):
            for jj in range(0, length, tile_size):
                for i in range(0, length):
                    j_end = jj + tile_size
                    for j in range(jj, j_end):
                        k_end = kk + tile_size
                        sum = matrix[i][j]
                        for k in range(kk, k_end):
                            sum = sum + a[i][k] * b[k][j]
                        matrix[i][j] = sum
    return matrix

def multiMatrixParallel(a, b):
    rowsA = len(a)      # Rows in matrix a
    rowsB = len(b)      # Rows in matrix b
    colsA = len(a[0])   # Cols in matrix a
    colsB = len(b[0])   # Cols in matrix b
    
    # For dot product colsA must equal rowsB,
    # and the result matrix will be (rowsA x colsB),
    # but we are only using square matrices,
    # so checking isn't that important.
    if colsA != rowsB:
        return None
    
    matrix = pymp.shared.array((rowsA, colsB), dtype=int)
    
    with pymp.Parallel() as p:
        print(f'Matrix multiply on thread: {p.thread_num} of {p.num_threads}')
        for i in p.range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    matrix[i][j] += a[i][k] * b[k][j]
    return matrix;

def main():
    """
    Used for running as a script
    """
    parser = argparse.ArgumentParser(description=
    'Generate a 2d matrix of size s filled with value v,'
    'Creates another matrix of size s filled with value v*2,'
    'Multiply both matrices in either serial or parallel,'
    'Serial uses two different algorithms, specified by blocked')
    parser.add_argument('-s', '--size', default=256, type=int,
    help='Size of the 2d matrix to generate')
    parser.add_argument('-v', '--value', default=1, type=int,
    help='The value with which to fill the array with')
    parser.add_argument('-b', '--blocked', action='store_true',
    help = 'Indicates the use of the blocked algorithm.')
    parser.add_argument('-p', '--parallel', action='store_true',
    help = 'Indicates the use of the parallel algorithm.')

    args = parser.parse_args()
    
    mat = genMatrix(args.size, args.value)              # generate 2d matrix
    mat2 = genMatrix(args.size, args.value * 2)         # generate 2nd matrix
    mat3 = None

    start = time.monotonic()                                # time before computation
    if args.parallel:
        if args.blocked:
            mat3 = multiMatrixBlockedParallel(mat, mat2)
        else:
            mat3 = multiMatrixParallel(mat, mat2)
    else:
        if args.blocked:
            mat3 = multiMatrixBlocked(mat, mat2)
        else:
            mat3 = multiMatrix(mat, mat2)
    elapsed = time.monotonic() - start                      # computation time
    
    #mat3 = np.matmul(mat, mat2) # Used for testing
        
    if mat3 is None:
        print("Error: incompatible matrices.")
    else:
        print("Matrix 1:")
        printSubarray(mat)
        print("Matrix 2:")
        printSubarray(mat2)
        print("Matrix 3 (result):")
        printSubarray(mat3)
        if args.parallel:
            if args.blocked:
                print("Matrix multiply blocked (parallel) time: %.4f seconds" % elapsed)
            else:
                print("Matrix multiply (parallel) time: %.4f seconds" % elapsed)
        else:
            if args.blocked:
                print("Matrix multiply blocked (serial) time: %.4f seconds" % elapsed)
            else:
                print("Matrix multiply (serial) time: %.4f seconds" % elapsed)

if __name__ == '__main__':
    # execute only if run as a script
    main()