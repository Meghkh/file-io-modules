""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.
    fruit_file_1 = open(filename)
    fruit_file_1_string = fruit_file_1.read()
    fruit_file_1_string = fruit_file_1_string.strip()
    fruit_file_1_list = fruit_file_1_string.split("\n")
    fruit_file_1.close()

    #print fruit_file_1_list

    return fruit_file_1_list


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """
    lst_3 = []
    for item_1 in lst1:
        if item_1 in lst2:
            lst_3.append(item_1)
    return lst_3

# Call your functions at the bottom, after they've been defined.
fruits_1 = open_and_read_file("fruits_1.txt")
fruits_2 = open_and_read_file("fruits_2.txt")
fruits_3 = compare(fruits_1, fruits_2)

print fruits_3
