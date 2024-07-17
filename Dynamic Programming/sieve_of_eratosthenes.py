# sieve of eratosthenes is one of the oldest-known algorithms that is useful in deriving prime numbers (up to a given limit)

"""ALGORITHM
The sieve works by assuming all numbers from 2 to n are prime and successively marking them as NOT prime.
1: Create a list of all integers 2 to n.
2: Start with the smallest number in the list.
3: Mark all muliples of that number up to n as NON PRIME.
4: Move to the next non-marked number and repeat this process until the list is covered.
"""

def sieve_of_eratos(n):
    true_indices = []

    # handle edge cases
    if (n <= 1):
        return true_indices

    # STEP 1: create array
    # create a list of size n (we want to ignore "values" 0 and 1 (aka index 0 and 1))
    # fill the values 2-n to True since we are assuming prime initally
    output = [True] * (n+1)  # we do n+1 because we want to INCLUDE n
    output[0] = False
    output[1] = False

    # STEP 2: iterate
    # for range index 2 to n+1, check if each index has been marked as NON-PRIME (aka False)
    for i in range(2, n):
        if output[i] == True:
            j = i*2  # initializing with multiples of i
            while j <= n:
                output[j] = False
                j += i  # visit each mulitple by adding the OG number to the current multiple

    # STEP 3: return the values
    # remove non-prime numbers
    output_with_indices = list(enumerate(output))
    true_indices = [index for (index,value) in output_with_indices if value == True]
    return true_indices


primes = sieve_of_eratos(13)
print(primes) # should return [2, 3, 5, 7, 11, 13)