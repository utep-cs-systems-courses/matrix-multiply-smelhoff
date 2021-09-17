## Matrix Multiply Assignment 1 part 2 by Seth Melhoff

This program employs two different algorithms for multiplying (n x n) matrices.  
User input is required for the size of the matrix and the value to fill the matrix with.  
Another matrix will be generated with the same size and filled with the specified value * 2.  
Part 2 adds the ability to run the non-blocked algorithm in serial or parallel.  
Each computation is timed, and the results are displayed in the output.  
> Use -b to specify the blocked algorithm and -p to specify in parallel.   
> This corresponds to after the commit '9849f5d'.
<br>
<br>

## How to use

Tested and verified working on Python 3.6.10  
Run 'matrixUtils.py' with the arguments '-s' , '-v' , '-b' , '-p'. Arguments b and p are optional. 

    -s is the size of the 2d matrix to generate. Must be evenly divisible by 16 (16,32,...,256,512,1024,...etc).
    -v is the value with which to fill the array with.  
    -b specifies the use of the blocked algorithm.  
    -p specifies running in parallel.  
    use OMP_NUM_THREADS=# to specify how many threads to use in parallel.
<br>
<br>

## Example

```python
Non-blocked serial:
    python3 matrixUtils.py -s 256 -v 2

blocked serial:
    python3 matrixUtils.py -s 256 -v 2 -b

Non-blocked parallel:
    python3 matrixUtils.py -s 256 -v 2 -p

blocked parallel:
    python3 matrixUtils.py -s 256 -v 2 -p -b

Non-blocked parallel with 4 threads:
    OMP_NUM_THREADS=4 python3 matrixUtils.py -s 256 -v 2 -p
```
<br>
<br>

## Extra info

The program takes the input via arguments and generates two matrices.  
The first matrix is of size 's' and filled with the value 'v'.  
The second matrix is of size 's' and filled with the value 'v' * 2.  
In the output you will see the corresponding sub-array of each matrix.  
They are displayed in the following order: Matrix 1, Matrix 2, and Matrix 3.  
The third matrix is the result of multiplying Matrix 1 and Matrix 2.  
Finally, you will see the time it took to compute the multiplication using two different algorithms.  
<br>
<br>

## Performance

The following are results generated using the different methods, the average time of 3 runs.  

**Non-blocked serial**:  
```python
python3 matrixUtils.py -s 256 -v 2  
    Matrix multiply (serial) time: 6.5876 seconds  

python3 matrixUtils.py -s 512 -v 2  
    Matrix multiply (serial) time: 55.1618 seconds    

python3 matrixUtils.py -s 1024 -v 2  
    Matrix multiply (serial) time: 454.0925 seconds  
```

**blocked serial**:  
```python
python3 matrixUtils.py -s 256 -v 2 -b  
    Matrix multiply blocked (serial) time: 5.5050 seconds  

python3 matrixUtils.py -s 512 -v 2 -b  
    Matrix multiply blocked (serial) time: 45.1808 seconds    

python3 matrixUtils.py -s 1024 -v 2 -b  
    Matrix multiply blocked (serial) time: 368.8801 seconds  
```

**Non-blocked parallel**:  
```python
python3 matrixUtils.py -s 256 -v 2 -p  
    Matrix multiply (parallel) time: 17.7833 seconds (OMP_NUM_THREADS=1)  
    Matrix multiply (parallel) time: 9.0525 seconds (OMP_NUM_THREADS=2)  
    Matrix multiply (parallel) time: 4.5583 seconds (OMP_NUM_THREADS=4)  
    Matrix multiply (parallel) time: 2.1184 seconds (OMP_NUM_THREADS=8)  
    Matrix multiply (parallel) time: 1.2650 seconds (OMP_NUM_THREADS=16)  
    Matrix multiply (parallel) time: 1.1836 seconds (OMP_NUM_THREADS=20)    

python3 matrixUtils.py -s 512 -v 2 -p  
    Matrix multiply (parallel) time: 146.1765 seconds (OMP_NUM_THREADS=1)  
    Matrix multiply (parallel) time: 69.2711 seconds (OMP_NUM_THREADS=2)  
    Matrix multiply (parallel) time: 34.9658 seconds (OMP_NUM_THREADS=4)  
    Matrix multiply (parallel) time: 14.1067 seconds (OMP_NUM_THREADS=8)  
    Matrix multiply (parallel) time: 11.2253 seconds (OMP_NUM_THREADS=16)  
    Matrix multiply (parallel) time: 10.9270 seconds (OMP_NUM_THREADS=20)   
```

**blocked parallel**:  
```python
python3 matrixUtils.py -s 256 -v 2 -p -b  
    Matrix multiply blocked (parallel) time: 11.7214 seconds (OMP_NUM_THREADS=1)  
    Matrix multiply blocked (parallel) time: 5.6837 seconds (OMP_NUM_THREADS=2)  
    Matrix multiply blocked (parallel) time: 2.5037 seconds (OMP_NUM_THREADS=4)  
    Matrix multiply blocked (parallel) time: 1.4878 seconds (OMP_NUM_THREADS=8)  
    Matrix multiply blocked (parallel) time: 0.8807 seconds (OMP_NUM_THREADS=16)  
    Matrix multiply blocked (parallel) time: 0.6547 seconds (OMP_NUM_THREADS=20)  

python3 matrixUtils.py -s 512 -v 2 -p -b  
    Matrix multiply blocked (parallel) time: 94.0867 seconds (OMP_NUM_THREADS=1)  
    Matrix multiply blocked (parallel) time: 46.5673 seconds (OMP_NUM_THREADS=2)  
    Matrix multiply blocked (parallel) time: 23.8779 seconds (OMP_NUM_THREADS=4)  
    Matrix multiply blocked (parallel) time: 6.4276 seconds (OMP_NUM_THREADS=8)  
    Matrix multiply blocked (parallel) time: 6.1866 seconds (OMP_NUM_THREADS=16)  
    Matrix multiply blocked (parallel) time: 5.9936 seconds (OMP_NUM_THREADS=20)  
```
<br>
<br>

## Issues

One of the big issues I ran into was trying to get PyMP working in a windows environment.  
I was unable to figure it out, so I ended up using the provided virtual machine.  
Implementing the algorithms wasn't very difficult. I was able to do that pretty quick.  
I ended up reverting my original push, which used scan to take the user input for part 1.  
I decided to do this because implementing the parallel portion was simpler using arguments.    
<br>
<br>

## Conclusion

After running all the tests, I realized that doubling the number of threads reduces the computation time by almost 50%.  
This seemed to be the case all the way up to 8 threads. After that, the performance increase got smaller with each added thread.  
I believe the program behaves this way because it is splitting up the work into multiple threads.  
At some point, no matter how many threads there are, you can only speed up the execution so far.  
You can clearly see the advantage of parallel computing just by looking at the data.  
This assignment took me around 2 days, off and on, to complete.  
<br>
<br>

## CPUINFO

    model name	: AMD Ryzen 9 5900X 12-Core Processor            
        24     216    1464