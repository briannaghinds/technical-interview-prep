# calcualte the water from the empty spaces in the histogram
# solution: the amount of rainwater at ANY point will = (height - lowest point)
# this problem makes use of the two pointer solution, other problems that use this is TWO SUM and REVERSING THE CHARACTERS IN A STRING

"""PSEUDOCODE
while left_pointer < right_pointer
  if the height at left_pointer <= the height at right_pointer
     - update the left_bound to be the greater value between the current left_bound and the height at left_pointer
     - increment total_water to be the difference between left_bound and the height at left_pointer
     - move left_pointer forward by one
  else
     - update the right_bound to be the greater value between the current right_bound and the height at right_pointer
     - increment total_water to be the difference between right_bound and the height at right_pointer
     - move right_pointer back by one 

return total_water
"""

def rainwater(heights):
    total_water = 0
    left_pointer = 0
    right_pointer = len(heights) - 1
    left_bound = 0
    right_bound = 0

    # while the left pointer and right pointer don't cross
    while left_pointer < right_pointer:
        # check if the heights at left pointer is less than or equal to end of list
        if heights[left_pointer] <= heights[right_pointer]:
            # set left_bound to be the max value of current left_bound OR the height at left_pointer
            left_bound = max(left_bound, heights[left_pointer])
            total_water += (left_bound - heights[left_pointer])
            left_pointer += 1
        else:
            
            right_bound = max(right_bound, heights[right_pointer])
            total_water += (right_bound - heights[right_pointer])
            right_pointer -= 1

    return total_water


histogram = [4, 2, 1, 3, 0, 1, 2]
print(rainwater(histogram))