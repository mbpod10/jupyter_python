import numpy as np

# Create an array of 10 zeros
arr = np.zeros(10)

# Create an array of 10 ones
arr = np.ones(10)

# Create an array from 0 to 10 skipping 2 each
arr = np.arange(0, 11, 2)

# Create an array of 10 fives
arr = np.zeros(10) + 5

# Create an array of the integers from 10 to 50
arr = np.arange(10, 51)

# Create an array of all the even integers from 10 to 50
arr = np.arange(10, 51, 2)

# Create a 3x3 matrix with values ranging from 0 to 8
arr = np.arange(0, 9).reshape(3, 3)

# Create a 3x3 identity matrix
arr = np.eye(3)

# Use NumPy to generate a random number between 0 and 1
arr = np.random.rand(1)

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
arr = np.random.randn(25)

# Create 10 x 10 matrix from 0.01 to 1 incrementing 0.1
arr = np.arange(.01, 1.01, .01)

# Create an array of 20 linearly spaced points between 0 and 1:
arr = np.linspace(0, 1, 20)

# ///////////////////////////////////////////////////////////////////////////
mat = np.arange(1, 26).reshape(5, 5)


# Get the sum of all the values in mat
arr = np.sum(mat)

# Get the sum of all the columns in mat
arr = np.sum(mat, matrix=0)


print(arr)
