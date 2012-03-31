#!/usr/bin/env python
"""
Script to calculate Mutual Information between two discrete random variables

Roberto maestre - rmaestre@gmail.com
"""
from __future__ import division
from numpy  import *
import math

# Define data array
data = array( [ (1,1,1,0,0,0),
                (0,0,0,1,1,1)] )

# Check if all rows have the same length
assert (len(data.shape) == 2)

# Get basic info for loops
print data.shape
n_rows = data.shape[0]
n_cols = data.shape[1]

# Perform summation
x_index = 0
while x_index < n_rows :
    y_index = x_index + 1
    while y_index < n_rows:
        # Final summation
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        values_y = set(data[y_index])
        print 'MI between'
        print data[x_index]
        print data[y_index]
        # For each random
        for value_x in values_x:
            for value_y in values_y:
                px = shape(where(data[x_index]==value_x))[1] / n_cols
                py =shape(where(data[y_index]==value_y))[1] / n_cols
                pxy = len(where(in1d(where(data[x_index]==value_x)[0], where(data[y_index]==value_y)[0])==True)[0]) / n_cols
                if pxy > 0.0:
                    summation += pxy * math.log((pxy / (px*py)), 2)
                print '(%d,%d) px:%f py:%f pxy:%f' % (value_x, value_y, px, py, pxy)
        print 'var_%d var_%d MI=%f\n\n' % (x_index, y_index, summation)
        y_index += 1
    x_index += 1