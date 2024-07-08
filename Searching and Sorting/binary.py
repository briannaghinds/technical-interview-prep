"""BINARY SEARCH
O(log n)
- can be called recursively (base case, recursive case)
- everytime we search, we half the list 
- the list used HAS to be SORTED
- instead of halking the list everytime (O(n/2)) we can instead use pointers to the start and end of the list
"""
# return both the value and the index
def binary_search(arr, left_pointer, right_pointer, n):
    # base case 1: list is empty
    if left_pointer >= right_pointer:
        return "List is empty"

    middle = (right_pointer + left_pointer) // 2  # floor division (give us an integer)
    # base case 2: n is the middle value
    if arr[middle] == n:
        return middle

    # recursive call
    """
    if middle point is LARGER, n is in the LEFT HALF
    if middle point is SMALLER, n is in the RIGHT HALF
    the left and right halves will be "new lists" created via list slicing
    """
    # middle is larger
    if arr[middle] > n:
        # since we are looking at the LEFT HALF our new right pointer = the middle of the list
        return binary_search(arr, left_pointer, middle, n)
    if arr[middle] < n:
        # RIGHT HALF, our new left pointer will be the middle+1
        return binary_search(arr, middle+1, right_pointer, n)
 
  
  
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    n = 5
    print(f"{n} is in index {binary_search(arr, 0, len(arr)-1, n)}")