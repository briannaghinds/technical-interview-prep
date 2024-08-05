"""
Given a string reverse the output.
INPUT: "Hello World"
OUTPUT: "dlroW olleH"
**do this with and without using slicing method**
O(N) <- because how fast the method goes depends on the size of the string
"""

def reverse_custom(string:str):
    r = ""
    for i in range(len(string)-1, -1, -1):
        r += string[i]

    return r


def reverse_python(string:str):
    return string[::-1]  # start at end, end at position 0, with steps of -1


if __name__ == "__main__":
    string = "Hello World"

    print(reverse_custom(string))
    print(reverse_python(string))