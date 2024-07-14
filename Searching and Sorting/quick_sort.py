# QUICK SORT: a divide and conquer algorithm that breaks the arrays into sub-array containing at most 1 element
# a single PIVOT is used, and the element is compared with the pivot splitting the list into three groups
# (1) a sub-array that has elements SMALLER than the pivot
# (2) the picot value itself
# (3) a sub-array that has elements GREATER then the picot
# animation: https://visualgo.net/en/sorting

"""TIME COMPLEXITY
- O(n log n)
- Why? 
"""

# because quick sort uses recursion, we will make us of a base case and an inductive step that takes us CLOSER to the base case
# we will also be "sorting in place", meaning that we will need to keep track of sublists (using pointers and swap variables)
from random import randrange, shuffle

def quicksort(list, start, end):
    # base case: this portion of list has been sorted
    # using pointers we are checking if the portion of the list between start and end contains one or less elements
    if start >= end:
        return
    
    print("Running quicksort on {0}".format(list[start: end + 1]))
    # select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    print("Selected pivot {0}".format(pivot_element))
    # swap random element with last element in sub-lists
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start
  
    for i in range(start, end):
        # we found an element out of place
        if list[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            print("Swapping {0} with {1}".format(list[i], list[less_than_pointer]))
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            # tally that we have one more lesser element
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements (aka put the pivot element into its correct place on in the list)
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    print("{0} successfully partitioned".format(list[start: end + 1]))
    # recursively sort left and right sub-lists
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)



## TEST  
list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)
