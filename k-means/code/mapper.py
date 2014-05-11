#!/usr/bin/env python2.7

import sys
import numpy as np
from scipy.spatial.distance import cdist

def emit(key, value):
    print('%s\t%s' % (key, value))

if __name__ == "__main__":
    X = np.zeros(shape=(0, 750))
    for line in sys.stdin:
        sample = np.fromstring(line, sep=" ")
        
        X = np.vstack( (X, sample) )
    
    np.random.seed(seed=42)
    
    init_centers = np.random.random( (200, 750) ) * 2 - 1
    
    i = 0
    centers = {}
    distances = None
    for center in init_centers:
        centers[i] = (center, 1)
        i += 1
    
    distances = cdist(X, init_centers, 'euclidean')
    i=0
    for sample in distances:
        low = sys.maxint
        assigned_center = None
        j = 0
        for center in sample:
            if center < low:
                low = center
                assigned_center = j
            j = j+1
        centers[assigned_center] = (centers[assigned_center][0]+X[i], centers[assigned_center][1]+1)
        i = i+1
    
    for i in xrange(len(centers.keys())):
        emit(i, (centers[i][0].tolist(), centers[i][1]))

