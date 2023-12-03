#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    for i in range(len(my_String)):
        if(my_String[i] != 'c' and my_String[i] != 'C'):
            ret += my_String[i] 
            return ret
