#!/usr/bin/python3
def uniq_add(my_list=[]):
    Total = 0
    for uniqueInt in set(my_list):
        Total += uniqueInt
    return Total
