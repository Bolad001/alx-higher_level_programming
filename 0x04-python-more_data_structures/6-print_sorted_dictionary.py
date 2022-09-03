#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for my_keys in sorted(a_dictionary):
        print("{:s}: {}".format(my_keys, a_dictionary[key]))
