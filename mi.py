#!/usr/bin/env python
"""
Script to calculate Mutual Information between two discrete random variables

Roberto maestre - rmaestre@gmail.com
"""
from __future__ import division
from numpy  import *
import math
import time

class MutualInformation:
    
    def __init__(self, data):
        """
        """
        # Check if all rows have the same length
        assert (len(data.shape) == 2)
        # Save data
        self.data = data
        self.n_rows = data.shape[0]
        self.n_cols = data.shape[1]
        
    def get_mi(self, x_index, y_index, log_base, debug = False):
        """
        Calculate and return Mutual information between two random variables
        """
        # Check if index are into the bounds
        assert (x_index >= 0 and x_index <= self.n_rows)
        assert (y_index >= 0 and y_index <= self.n_rows)
        # Variable to return MI
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        values_y = set(data[y_index])
        if debug:
            print 'MI between'
            print data[x_index]
            print data[y_index]
        # For each random
        for value_x in values_x:
            for value_y in values_y:
                px = shape(where(data[x_index]==value_x))[1] / self.n_cols
                py =shape(where(data[y_index]==value_y))[1] / self.n_cols
                pxy = len(where(in1d(where(data[x_index]==value_x)[0], where(data[y_index]==value_y)[0])==True)[0]) / self.n_cols
                if pxy > 0.0:
                    summation += pxy * math.log((pxy / (px*py)), log_base)
                if debug:
                    print '(%d,%d) px:%f py:%f pxy:%f' % (value_x, value_y, px, py, pxy)
        if debug:
            print 'var_%d var_%d MI=%f\n\n' % (x_index, y_index, summation)
        return summation

# Define data array
data = array( [ (0,0,1,1,0,1,1,2,2,2),
                (3,4,5,5,3,2,2,6,6,1),
                (7,2,1,3,2,8,9,1,2,0),
                (7,7,7,7,7,7,7,7,7,7)] )
                
# Create object
mi = MutualInformation(data)

# Print mutual information between var_0 (0,0,1,1,0,1,1,2,2,2) and var_1 (3,4,5,5,3,2,2,6,6,1)
t_start = time.time()
print 'MI: %f' % mi.get_mi(0,1,10)
print 'Elapsed time: %f\n' % (time.time() - t_start)


# Print mutual information between var_1 (3,4,5,5,3,2,2,6,6,1) and var_2 (7,2,1,3,2,8,9,1,2,0)
t_start = time.time()
print 'MI: %f' % mi.get_mi(1,2,10)
print 'Elapsed time: %f\n' % (time.time() - t_start)
