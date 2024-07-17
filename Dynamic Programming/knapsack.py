"""THE PROBLEM
You will be given the total amount of weight you can carry. (weight_cap)
The weights of all the items in an array. (weights)
The values of all the items in an array. (values)
Your function should return the maximum value that you will be able to carry.
(you can only take one of each item)
"""

# i is the variable that will keep track of where we are on the list of items
# this has a run time of O(2^n) since it is recursive
def recursive_knapsack(weight_cap, weights, values, i):
    # there are 3 possibilities when we call the function
    # 1: weight_cap or i = 0, meaning that the knapsack is full or there are no more items to look at
    # 2: the weight of the item we are looking at is GREATER than the weight cap
    # 3: if neither 1 or 2 is true then we now are considering if the current item we are at should be included in the optimial solution
    
    # base condition
    if (weight_cap == 0) or (i == 0):
        return 0
    # condition 2
    elif weights[i-1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i-1)
    else:
        # remove the weight of the added item
        include_item = values[i-1] + recursive_knapsack(weight_cap-weights[i-1], weights, values, i-1)
        exclude_item = recursive_knapsack(weight_cap, weights, values, i-1)

        return max(include_item, exclude_item)

# dynamic programming is so much better for knapsack because memoization allows us to store information instead of making duplicate calls
# we will store this infomation in a 2D array that has a row for every item and weight_cap+1 number of columns (each element in the 2D array represents a subproblem)
# the element in the BOTTOM RIGHT will be the optimal solution
""" ROWS?
What do the rows represent? They represent the items we have seen.
If we are at row 4, then we have only seen the first 4 items, meaning the others haven't been considered yet.
"""
# this has a runtime of n*weight_cap
def dynamic_knapsack(weight_cap, weights, values):
    """ PSEUDOCODE
    matrix = 2D array with rows equal to number of items and empty columns
    for every number of items you can carry (index):
    fill matrix[index] with an array of length weight_cap + 1
    for every weight < weight_cap (weight):
        if index or weight == 0:
            set element at [index][weight] to 0  
        else if the weight of element at index - 1 <= weight:
            find possible values of including and excluding the item
            set element at [index][weight] to max of those values
        else:
            set element at [index][weight] to element one above
    return element at bottom right of matrix
    """
    rows = len(weights) + 1
    columns = weight_cap + 1

    matrix = [[] for i in range(rows)]
    print(matrix)

    # iterate through every row
    for index in range(rows):
        # initalize the columns in the row
        matrix[index] = [-1 for y in range(columns)]

        # iterate through every column
        for weight in range(columns):
            if (index == 0) or (weight == 0):
                matrix[index][weight] = 0
            elif weight[index-1] <= weight:
                # find the max value of the two values
                include = values[index-1] + matrix[index-1][weight-weight[index-1]]
                exclude = matrix[index-1][weight]

                matrix[index][weight] = max(include, exclude)
            else:
                # calculate value of current cell
                matrix[index][weight] = matrix[index-1][weight]

    
    # return the value of the bottom right matrix
    return matrix[rows-1][weight_cap]




# Use this to test your function:
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(dynamic_knapsack(weight_cap, weights, values))