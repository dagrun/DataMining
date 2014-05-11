#!/usr/bin/env python2.7

import sys
import numpy as np
from ast import literal_eval
from scipy.spatial.distance import cdist

if __name__ == "__main__":
    result = None
    last_key = None
    centers = np.zeros(shape=(0, 750))
    center = None
    prev_weight = None
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        sample, weight = literal_eval(value)
        sample = np.asarray(sample)
        
        if last_key is None:
            center = sample
            prev_weight = weight
            last_key = key

        if key == last_key:
            prev_weight += weight
            center += sample
        else:
            center = center / float(prev_weight)
            centers = np.vstack( (centers, center) )
            center = sample
            prev_weight = weight
            last_key = key
    
    center = center / float(prev_weight)
    centers = np.vstack( (centers, center) )
    
    i = 0
    centers = centers.tolist()
    while i < len(centers):
        j = 0
        while j < len(centers[i]):
            if j != len(centers[i]) -1:
                sys.stdout.write(str(centers[i][j]) + ' ')
            else:
                sys.stdout.write(str(centers[i][j]) + '\n')
            
            j += 1
        i += 1 

