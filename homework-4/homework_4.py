"""
SEARCH IN MATRIX
--------

You are given a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""

def search_in_matrix(matrix, target):
    for x, matrix in enumerate(matrix):
        for y, value in enumerate(matrix):
            if value == target:
                return (x, y)
            # can't get this part to work as if added they all show -1, -1 except target 1 :(
            # else:
            #     return (-1,-1)

matrix = [
[1, 4, 7, 12, 15, 1000],
[2, 5, 19, 31, 32, 1001],
[3, 8, 24, 33, 35, 1002],
[40, 41, 42, 44, 45, 1003],
[99, 100, 103, 106, 128, 1004]
]

if __name__ == '__main__':
    print(search_in_matrix(matrix, 44))  # Should print [(3, 3)]
    print(search_in_matrix(matrix, 35))  # Should print [(2, 4)]
    print(search_in_matrix(matrix, 6))  # Should print [(-1, -1)] Need to work on exception
    print(search_in_matrix(matrix, 1004))  # Should print [(4, 5)]
    print(search_in_matrix(matrix, 41))  # Should print [(3, 1)]
    print(search_in_matrix(matrix, 1))  # Should print [(0, 0)]




