#for a given alpha numeric string, find first recurring character in string
#if no recurring character, return none/null
#e.g. string = 'abcdab' ; return a
#e.g. string = 'abcdba' ; return b
#e.g. string = 'abcd'   ; return None

import time

def first_recurring(string):
    appearances = {}
    for char in string:
        if char in appearances:
            break
        elif char not in appearances:
            appearances[char] = 1
            if char == string[-1]:
                char = None
    return char

start = time.time()
result = first_recurring('abcda')
stop = time.time()

total_time = stop - start
print total_time, result       