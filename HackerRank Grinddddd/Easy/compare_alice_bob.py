"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, 
awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for 
Bob's challenge is the triplet b = (b[0], b[1], b[2]).

if a[i] > b[i], a gets a point
if a[i] < b[i], b gets a point
else either get a point

you are outputing an array of alice's score and bob's score
"""

# given a = [5, 6, 7] and b = [3, 6, 10], the output should be [1, 1]

def compareTriplets(a, b):
    alice = 0
    bob = 0
    pointer = 0

    while pointer < len(a):
        if a[pointer] > b[pointer]:
            alice += 1
        elif a[pointer] < b[pointer]:
            bob += 1

        pointer += 1

    
    scores = [alice, bob]
    return scores

if __name__ == "__main__":
    a = [5, 6, 7]
    b = [3, 6, 10]