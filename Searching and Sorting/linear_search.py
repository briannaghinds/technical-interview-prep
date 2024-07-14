"""PROPERTIES
- O(n)
- Best Case: O(1) = we find the element in first index
- Worst Case: O(n) =  either the element is the last one or it doesn't exist
- Average Case: O(n/2) = simplifies to O(n) = middle value
"""
def linear_search(arr, val):
    # given the array iterate through the list until the val is found
    # return the index
    for i in range(len(arr)):
        if arr[i] == val:
            return i  
        else: 
            print("Value not found in array.")


# finding the max value's index (using linear search)
def finding_max(arr):
    # set the "max" to be the first index
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


if __name__ == "__main__":
    # linear search
    arr_lin = [2, 4, 6, 4, 6, 2, 3, 4, 6, 9, 3, 1]
    print(f"Linear Search, Finding 11's index: {linear_search(arr_lin, 11)}")

    # finding the max value (using same array from linear search)
    print(f"Finding Max Value in Array: {finding_max(arr_lin)}")