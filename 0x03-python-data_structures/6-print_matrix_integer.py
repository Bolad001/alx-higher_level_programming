#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for i in range(len(matrix[row])):
            print("{:d}".format(matrix[row][j]), end=" ")
        print()
