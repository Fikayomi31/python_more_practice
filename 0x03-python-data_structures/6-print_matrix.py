#!/usr/bin/python3
def print_matrix(matrix=[[]]):
    for row in matrix: #Lopping through each row
        for col in row: #Looping through the row to print each digit
            print("{}".format(col), end=' ')
        print()
