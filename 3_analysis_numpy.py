# NUMPY

### From NumPy official documentation:
# NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the
# same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes.

import numpy as np
from utils.tutorial_navigation import step

# Numpy comes with a lot of functions implemented to calculate the basic statistical characteristics.
# Note that, since Numpy works with multidimensional arrays usually you have to specify an axis such that Numpy knows
# which dimension you are interested in.
# Basic Numpy functions, like np.mean() or np.sum(), are sensitive to missing values. Also a typical None must actually
# be parsed to the same datatype as the other values inside the array. Luckily Numpy offers also robust methods to deal
# with missing values, e.g. np.nanmean() for means, np.nanstd() and np.nansum() for standard deviations and sum
# respectively

# Define a 1D numpy array containg the values reported in ./utils/constants->example_list



if step == 1:
    pass
    # print the array


if step >= 2:
    pass
    # Define a 2D numpy array containing example_list and then copies of example_list increased by 1 element-wise and
    # multiplied by 2 respectively


    # Remove missing values and repeat



    # Define a 2D numpy array where each column is a copy of example_list without nans increased element-wise by values
    # extracted from a gaussian distribution with increasing standard deviation for each column


# We can easily compute some statistics using numpy
if step == 3:
    pass
    # compute the mean values along axis 1 for the last defined array

if step == 4:
    pass
    # compute correlation between the 3 1D arrays composing our 2D matrix

