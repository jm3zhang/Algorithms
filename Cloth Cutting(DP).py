#!/usr/bin/env python3
"""
Dynamic Programming
"""

def cut_cloth(values, L):
    """
    Input: a list values[0 ... L], where value[i] contains value of a
    piece of length i, and values[0] = 0.  An integer L giving
    the total length of cloth.
    Output: a list pieces[0 ... L] and an integer K, where pieces[i]
    gives number of pieces of length i used in the solution, and K
    is the total value obtained.
    """
    K = [0] * (L + 1)  # initialize list of subproblems
    new_piece = [0] * (L + 1) # initialize pointers

    for length in range(0, L + 1):
        for k in range(0, length + 1):
            if K[length] < K[length - k] + values[k]:
                K[length] = K[length - k] + values[k]
                new_piece[length] = k

    # we just need to use the new_piece pointers to determine the
    # size of each piece of cloth we made
    pieces = [0] * (L + 1)
    length_remaining = L
    while length_remaining > 0:
        length_new = new_piece[length_remaining]
        pieces[length_new] += 1
        length_remaining -= length_new

    return pieces, K[L]


def main():
    """
    Testing the cut_cloth function
    """
    # example in question where we use one piece of length 1
    # and one of length 3.
    if cut_cloth([0, 2, 3, 7, 7], 4) == ([0, 1, 0, 1, 0], 9):
        print("your output is correct for the example in the question")
    else:
        print("Something is wrong in your output format or algorithm")
    # second input example
    print(cut_cloth([0, 0.5, 2, 3, 3, 3, 8, 2, 9, 5, 10], 10))


if __name__ == '__main__':
    main()
