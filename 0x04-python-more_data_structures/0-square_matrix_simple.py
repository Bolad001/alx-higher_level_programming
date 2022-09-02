#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        return [list(map((lambda x: x * x), i))]
