# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix arr is shown below:

# 1 2 3
# 4 5 6
# 9 8 9

# The left-to-right diagonal = 1+5+9 = 15 . The right to left diagonal = 3+5+9 = 17. Their absolute difference is [15 -17] =2.

# Function description

# Complete the diagonalDifference function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference
# Input Format

# The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j] .

def diagonalDifference(arr):
    counter = 0
    counter2 = len(arr) - 1

    leftdiag = []
    rightdiag = []
    for i in range(len(arr)):
        leftdiag.append((arr[counter][counter]))
        counter += 1
    print(leftdiag)

    counter = 0

    for i in range(len(arr)):
        rightdiag.append((arr[counter][counter2]))
        counter += 1
        counter2 -= 1
    print(rightdiag)

    return abs(sum(leftdiag) - sum(rightdiag))
