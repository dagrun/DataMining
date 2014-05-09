#!/usr/bin/env python2.7

import sys
import numpy as np
from ast import literal_eval
from scipy.spatial.distance import cdist

if __name__ == "__main__":
    XA = XB = None
    result = None
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        sample = literal_eval(value)
        
        if XA is None:
            XA = np.asarray(sample)
        else:
            XB = np.asarray(sample)
            distances = cdist(XA, XB, 'euclidean').tolist()
            
            for i in xrange(len(distances)):
                XA[i] = (XA[i] + XB[distances[i].index(min(distances[i]))]) / float(2)
    
    i = 0
    centers = XA
    while i < len(centers):
        j = 0
        while j < len(centers[i]):
            if j != len(centers[i]) -1:
                sys.stdout.write(str(centers[i][j]) + ' ')
            else:
                sys.stdout.write(str(centers[i][j]) + '\n')
            
            j += 1
        i += 1 

