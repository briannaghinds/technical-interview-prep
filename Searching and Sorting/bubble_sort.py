# BUBBLE SORT: iterates through a list and compares pairings of adjacent elements
# animation: https://visualgo.net/en/sorting

"""TIME COMPLEXITY
- O(n^2) <- quadratic
- Why? The inner loop does n-1 comparisons for each element in the list (this gets
simplified to just n). And the outer loop goes through the list n times to make sure
it is properly sorted.
"""

nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
    temp = arr[index_1]  # put that value at index_1 into a temporary variable
    arr[index_1] = arr[index_2]  # give index_1 that value at index_2
    arr[index_2] = temp  # give index_2 the SAVED value from the temp variable

# define bubble_sort(): (this version of bubble sort isn't as optimized)
def bubble_sort(arr):
    for j in arr:  # iterate through the WHOLE LIST (n) -> after a single pass the LARGEST element is moved to the back of the list
        for i in range(len(arr)-1):  # iterate throught the list-1 (n)
            if arr[i] > arr[i+1]:  # if a value is greater than the one it is next two, swap the two
                swap(arr, i, i+1)

# bubble sort: more optimized version
def bubble_sort_optim(arr):
    iteration_count = 0
    for i in range(len(arr)):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


##### test statements
print(f"Pre-Sort: {nums}")      
bubble_sort(nums)
print(f"Post-Sort: {nums}")
