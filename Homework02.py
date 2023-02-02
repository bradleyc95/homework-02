# Bradley Cox, Homework 02

import sys

# nested try except first attempts to assign 2 input arguments to 2 variables string1 and string2
try:
    string1 = sys.argv[1]
    string2 = sys.argv[2]
except IndexError:
    # if program encounters an index error attempting to assign either argument to variable, move to nested try except
    # attempt to assign 1 input argument to 1 variable string1, otherwise throw error
    try:
        string1 = sys.argv[1]
        string2 = ''
    except IndexError:
        string1 = 'please enter extra input arguments'
        string2 = ''

# print resulting combination of string1 and string2
print(string1 + ' ' + string2)

