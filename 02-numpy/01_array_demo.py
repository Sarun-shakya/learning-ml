## Numpy array and basics

import numpy as np


# Creating array from list
arr = np.array([3, 4, 5, 6, 7])

print("1D array: ", arr)

arr_2d = np.array([[1, 2, 3],[4, 5, 6]])
print("2D array: ", arr_2d)

# List vs numpy array

py_list = [1, 2, 3]
print("Python list multiplication: ", py_list * 2)

np_arr = np.array([3, 5, 7]) # element wise multiplication
print("Numpy array multiplication: " , np_arr * 2)

# Time module
import time;
start = time.time()
py_list = [i*2 for i in range(10000)]
print("\n List Operation time: ", time.time() - start)

start = time.time()
np_array = np.arange(10000) * 2;
print("\n Numpy Operation time: ", time.time() - start)

#Creating array from scratch

# Zeros
zeros = np.zeros((3, 4))
print("Zeros array: \n", zeros)

# Ones
ones = np.ones((3, 4))
print("Zeros array: \n", ones)

# full
full = np.full([2, 3], 5)
print("Full array: \n", full)

# Random number
random = np.random.random((3,4))
print("Random array: \n", random)

#Sequence Array
sequence = np.arange(0, 11)
print("Sequwnce array: \n", sequence)





