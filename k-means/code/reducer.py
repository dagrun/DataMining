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
        result = sample
        
#        if XA is None:
#            XA = np.asarray(sample)
#        else:
#            XB = np.asarray(sample)
#            distances = cdist(XA, XB, 'euclidean')
#            
#            max_value = 10000
#            result = []
#            while(distances.min() < max_value):
#                distances_as_list = list(np.array(distances).reshape(-1,))
#                mins = sorted([x for x in distances_as_list if x < max_value])
#                
#                for x in xrange(distances.shape[0]):
#                    for y in xrange(distances.shape[1]):
#                    
#                        if distances[x][y] == mins[0]:
#                            result.append((XA[x] + XB[y])/float(2))
#                            distances[x,:] = max_value
#                            distances[:,y] = max_value
    
    i = 0
    centers = result
    while i < len(centers):
        j = 0
        while j < len(centers[i]):
            if j != len(centers[i]) -1:
                sys.stdout.write(str(centers[i][j]) + ' ')
            else:
                sys.stdout.write(str(centers[i][j]) + '\n')
            
            j += 1
        i += 1 

