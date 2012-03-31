#!/usr/bin/env python
"""
Script to calculate Mutual Information between two discrete random variables

Roberto maestre - rmaestre@gmail.com
"""
from __future__ import division
from numpy  import *
import math

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
        
    def get_mi(self, x_index, y_index, debug = False):
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
                    summation += pxy * math.log((pxy / (px*py)), 2)
                if debug:
                    print '(%d,%d) px:%f py:%f pxy:%f' % (value_x, value_y, px, py, pxy)
        if debug:
            print 'var_%d var_%d MI=%f\n\n' % (x_index, y_index, summation)
        return summation

    
    
# Define data array
data = array( [ (1,1,1,0,0,0),
                (0,0,0,1,1,1),
                (1,0,1,1,0,0)] )
                
mi = MutualInformation(data)
print mi.get_mi(0,1)
print ''
print mi.get_mi(1,2, True)
