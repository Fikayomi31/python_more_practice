#!/usr/bin/python3
print_matrix = __import__('6-print_matrix').print_matrix

matrix = [
        [9, 8, 7, 6],
        [5, 4, 3, 2],
        [1, 0, 0, 1],
        [2, 3, 4, 5],
        [6, 7, 8, 9]
]

print_matrix(matrix)
print("--")
print_matrix()
