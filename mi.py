#!/usr/bin/env python
"""
Script to calculate Mutual Information between two discrete random variables

Roberto maestre - rmaestre@gmail.com
Bojan Mihaljevic - boki.mihaljevic@gmail.com
"""
from __future__ import division
from numpy  import array, shape, where, in1d
import math
import time
import nose

class InformationTheoryTool:
    
    def __init__(self, data):
        """
        """
        # Check if all rows have the same length
        assert (len(data.shape) == 2)
        # Save data
        self.data = data
        self.n_rows = data.shape[0]
        self.n_cols = data.shape[1]
        
        
    def single_entropy(self, x_index, log_base, debug = False):
        """
        Calculate the entropy of a random variable
        """
        # Check if index are into the bounds
        assert (x_index >= 0 and x_index <= self.n_rows)
        # Variable to return entropy
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        # Print debug info
        if debug:
            print 'Entropy of'
            print data[x_index]
        # For each random
        for value_x in values_x:
            px = shape(where(data[x_index]==value_x))[1] / self.n_cols
            if px > 0.0:
                summation += px * math.log(px, log_base)
            if debug:
                print '(%d) px:%f' % (value_x, px)
        if summation == 0.0:
            return summation
        else:
            return - summation
        
        
    def entropy(self, x_index, y_index, log_base, debug = False):
        """
        Calculate the entropy between two random variable
        """
        assert (x_index >= 0 and x_index <= self.n_rows)
        assert (y_index >= 0 and y_index <= self.n_rows)
        # Variable to return MI
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        values_y = set(data[y_index])
        # Print debug info
        if debug:
            print 'Entropy between'
            print data[x_index]
            print data[y_index]
        # For each random
        for value_x in values_x:
            for value_y in values_y:
                pxy = len(where(in1d(where(data[x_index]==value_x)[0], 
                                where(data[y_index]==value_y)[0])==True)[0]) / self.n_cols
                if pxy > 0.0:
                    summation += pxy * math.log(pxy, log_base)
                if debug:
                    print '(%d,%d) pxy:%f' % (value_x, value_y, pxy)
        if summation == 0.0:
            return summation
        else:
            return - summation
        
        
        
    def mutual_information(self, x_index, y_index, log_base, debug = False):
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
        # Print debug info
        if debug:
            print 'MI between'
            print data[x_index]
            print data[y_index]
        # For each random
        for value_x in values_x:
            for value_y in values_y:
                px = shape(where(data[x_index]==value_x))[1] / self.n_cols
                py = shape(where(data[y_index]==value_y))[1] / self.n_cols
                pxy = len(where(in1d(where(data[x_index]==value_x)[0], 
                                where(data[y_index]==value_y)[0])==True)[0]) / self.n_cols
                if pxy > 0.0:
                    summation += pxy * math.log((pxy / (px*py)), log_base)
                if debug:
                    print '(%d,%d) px:%f py:%f pxy:%f' % (value_x, value_y, px, py, pxy)
        return summation



# Define data array
data = array( [ (0, 0, 1, 1, 0, 1, 1, 2, 2, 2),
                (3, 4, 5, 5, 3, 2, 2, 6, 6, 1),
                (7, 2, 1, 3, 2, 8, 9, 1, 2, 0),
                (7, 7, 7, 7, 7, 7, 7, 7, 7, 7),
                (0, 1, 2, 3, 4, 5, 6, 7, 1, 1)])
# Create object
it_tool = InformationTheoryTool(data)


# --- Checking single random var entropy

# entropy of  X_1 (3, 4, 5, 5, 3, 2, 2, 6, 6, 1)
t_start = time.time()
print 'Entropy(X_1): %f' % it_tool.single_entropy(1, 10, False)
print 'Elapsed time: %f\n' % (time.time() - t_start)

# entropy of  X_3 (7, 7, 7, 7, 7, 7, 7, 7, 7, 7)
t_start = time.time()
print 'Entropy(X_3): %f' % it_tool.single_entropy(3, 10)
print 'Elapsed time: %f\n' % (time.time() - t_start)

# entropy of  X_4 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
t_start = time.time()
print 'Entropy(X_4): %f' % it_tool.single_entropy(4, 10)
print 'Elapsed time: %f\n' % (time.time() - t_start)



# --- Checking entropy between two random variables

# entropy of  X_0 (0, 0, 1, 1, 0, 1, 1, 2, 2, 2) and X_1 (3, 4, 5, 5, 3, 2, 2, 6, 6, 1)
t_start = time.time()
print 'Entropy(X_0, X_1): %f' % it_tool.entropy(0, 1, 10)
print 'Elapsed time: %f\n' % (time.time() - t_start)

# entropy of  X_3 (7, 7, 7, 7, 7, 7, 7, 7, 7, 7) and X_3 (7, 7, 7, 7, 7, 7, 7, 7, 7, 7)
t_start = time.time()
print 'Entropy(X_3, X_3): %f' % it_tool.entropy(3, 3, 10)
print 'Elapsed time: %f\n' % (time.time() - t_start)



# ---Checking Mutual Information between two random variables

# Print mutual information between X_0 (0,0,1,1,0,1,1,2,2,2) and X_1 (3,4,5,5,3,2,2,6,6,1)
t_start = time.time()
print 'MI(X_0, X_1): %f' % it_tool.mutual_information(0, 1, 10)
print 'Elapsed time: %f\n' % (time.time() - t_start)

# Print mutual information between X_1 (3,4,5,5,3,2,2,6,6,1) and X_2 (7,2,1,3,2,8,9,1,2,0)
t_start = time.time()
print 'MI(X_1, X_2): %f' % it_tool.mutual_information(1, 2, 10)
print 'Elapsed time: %f\n' % (time.time() - t_start)



# --- Checking results

# Checking entropy results
for i in range(1,data.shape[0]):
    assert(it_tool.entropy(1, 1, 10) == it_tool.single_entropy(1, 10))

# Checking mutual information results 
# MI(X,Y) = H(X) + H(Y) - H(X,Y) 
n_rows = data.shape[0]
i = 0
while i < n_rows:
    j = 0
    while j < n_rows:
        if j != i:
            nose.tools.assert_almost_equal(it_tool.mutual_information(i, j, 10), 
                        it_tool.single_entropy(i, 10)+it_tool.single_entropy(j, 10)-it_tool.entropy(i, j, 10))
        j += 1
    i += 1





