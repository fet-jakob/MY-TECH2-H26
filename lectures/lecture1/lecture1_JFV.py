"""
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().

"""

# This code does defines the fuction argmax wuthout importing it

import numpy as np


def argmax(values):
    """
    Return index pf the maximum value in a collect.

    Parameters
    ---------
    Values
        Sequnce of values

    Return
    -------
    imax : int
        Index maximum
    """

    N = len(values)

    if N == 0:
        print("")

    imax = None 
    # Set the vmax to the lowest possible value
    vmax = -np.inf

    for i in range(N):
        # First itteration: value = 2
        value = values[i]
        # Check whether this value is larger than than any previous
        if value > vmax:
            # update the index and the vmax
            imax = i
            vmax = value

    return imax


values = [2, 3, -1, 7, 4]
imax = argmax(values)

print(f'The maximum is located at {imax}')


#Compare to numpys argmax 
j = np.argmax(values)
print(f'The maximum is located at {imax}')

#if __name__ == '__main__':
    # Run the main script if this script is executed
    #main()





