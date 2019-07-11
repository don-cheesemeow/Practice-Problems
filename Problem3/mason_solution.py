#this solution uses the sorted function
#so there may be a more elegant solution
#that does not use a built in sorting function 
#still works though 8)

import time

example = [3,7,5,6,9]
def find_window_to_sort(int_list):
    
    zipped_list = zip(int_list, sorted(int_list))
    left = None
    right = None
    
    for pair in zipped_list:
        if pair[0] != pair[1]:
            left = zipped_list.index(pair)   
	    break
    for pair in reversed(zipped_list):
        if pair[0] != pair[1]:
             right = zipped_list.index(pair)
	     break
            
    sort_range = tuple((left,right))    
    return sort_range

start = time.time()
result = find_window_to_sort(example)
end = time.time()
total = end-start
print 'Result:', result,'|', 'time taken:', total
