#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if idx >= 0 or idx < len(my_list): # getting len of idx between 0 and len(my_list)
        my_list[idx] = new_element #casting the new integer into idx len number
    return my_list
