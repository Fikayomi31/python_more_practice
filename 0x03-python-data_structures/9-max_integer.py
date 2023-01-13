#!/usr/bin/python3
def max_integer(my_list=[]):
    ma = my_list[0] #casting highest as 0 into ma
    if not my_list: #if the list is empty
        return None
    for i in my_list[1:]: #Looping through my_list from 1: to the end
        if i > ma: #Looping for the highest
            ma = i #Casting highest into ma
    return ma

    

