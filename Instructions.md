## Matrix Multiply

This program employs two different algorithms for multiplying (n x n) matrices.  
User input is required for the size of the matrix and the values to fill each matrix with.  
Each computation is timed, and the results are displayed in the output.  

## How to use

Python 3.9.7 is the version I used.  
Run 'matrixUtils.py' with the arguments -s and -v.  
Argument 's' is the size of the 2d matrix to generate. Must be evenly divisible by 16 (16,32,...,256,512,1024,...etc).  
Argument 'v' is the value with which to fill the array with.  

## Example

python matrixUtils.py -s 256 -v 2

## Extra info

The program takes the input via arguments and generates two matrices.  
The first matrix is of size 's' and filled with the value 'v'.  
The second matrix is of size 's' and filled with the value 'v' * 2.  

In the output you will see the corresponding sub-array of each matrix.  
They are displayed in the following order: Matrix 1, Matrix 2, and Matrix 3.  
The third matrix is the result of multiplying Matrix 1 and Matrix 2.  
Finally, you will see the time it took to compute the multiplication using two different algorithms.  

## Conclusion

After testing out multiple different sizes of matrices, the blocked algorithm computes faster.

-s 256  
Matrix multiply time: 1.1250 seconds  
Matrix multiply blocked time: 0.9380 seconds  

-s 512  
Matrix multiply time: 9.5160 seconds  
Matrix multiply blocked time: 8.3750 seconds  

-s 1024  
Matrix multiply time: 78.3440 seconds  
Matrix multiply blocked time: 66.9680 seconds  