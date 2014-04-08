#!/usr/bin/env python2.7

import sys
import numpy as np
from sklearn import svm

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x_original):
    return x_original

if __name__ == "__main__":
    x = np.zeros(shape=(0, 400))
    y = []
    for line in sys.stdin:
        all_data = np.fromstring(line, sep=" ")
        
        y.append(all_data.item(0))
        x = np.vstack( (x, all_data[1:]) )
        

