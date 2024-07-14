# MERGE SORT: divide-and-conquer, breaks the list to be sorted into smaller parts
# Two steps to merge sort: (1) splitting the data into "runs" or smaller components
                        #  (2) re-combining those runs into sorted lists
# animation: https://visualgo.net/en/sorting

"""TIME COMPLEXITY
- O(n log n)
- Why?
"""

def merge_sort(items):
    # base case: list size is less than or equal to 1
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]  # for left include everything EXCEPT middle
    right_split = items[middle_index:]  # for right include middle to the end

    # recursive call for merge sort
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)

# helper function for merge sort
# IMPORTANT: arguments to merge WILL ALWAYS be sorted lists
def merge(left, right):
    # this is the sorted list that will hold the ordered values
    result = []

    # while there are still elements in left and right array
    while (left and right):
        # if element at first index in left is less than right then add left first
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            # otherwise add right first
            result.append(right[0])
            right.pop(0)

    # after iterating if there are still elements in the left and right, just tack it on to the result array
    if left:
        result += left
    if right:
        result += right

    return result


## TEST
unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1)
print(ordered_list2)
print(ordered_list3)
