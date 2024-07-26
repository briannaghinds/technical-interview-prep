"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""

def diag_diff(arr):
    print(len(arr))
    left_right = 0
    right_left = 0

    # time complexity of O(N)
    for i in range(0, len(arr)):
        # get left to right values: 00 -> 11 -> 22
        """
        The values at i and j are the same value so we just want to pull one since i = j
        """
        left_right += arr[i][i]
        print(f"value at [{i}][{i}]: {arr[i][i]} adding to left_right")

        # get right to left values (ij): 20 -> 11 -> 02, we can find the row by taking the absolute value of i-len(arr)-1
        right_left += arr[abs(i-(len(arr)-1))][i]
        print(f"value at [{abs(i-(len(arr)-1))}][{i}]: {arr[abs(i-(len(arr)-1))][i]} adding to right_left")


    return abs(left_right-right_left)


if __name__ == "__main__":
    arr = [[1, 2, 3], 
           [4, 5, 6], 
           [9, 8, 9]]  # output should be: 2 = |(1+5+9)-(3+5+9)|
    print(diag_diff(arr))