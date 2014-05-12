#!/usr/bin/env python2.7

import sys
import numpy as np
from ast import literal_eval
from scipy.spatial.distance import cdist
from sklearn.cluster import MiniBatchKMeans

if __name__ == "__main__":
    X = np.zeros(shape=(0, 751))
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        sample = literal_eval(value)
        X = np.vstack( (X, sample) )
        
    centers_weighted = np.random.random( (200, 751) ) * 2 - 1
    
    distances = cdist(X, centers_weighted, 'euclidean')
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
        centers_weighted[assigned_center, 0:750] = centers_weighted[assigned_center, 0:750]+(X[i,0:750]*X[i,750])
        centers_weighted[assigned_center, 750] += X[i,750]
        i = i+1
    centers = []

    for center in centers_weighted:
        centers.append(center[0:750]/center[750])
    i = 0
    
    mbk = MiniBatchKMeans(n_clusters=200, init='k-means++', n_init=5)
    mbk.fit(centers)
    centers = mbk.cluster_centers_

    while i < len(centers):
        j = 0
        while j < len(centers[i]):
            if j != len(centers[i]) -1:
                sys.stdout.write(str(centers[i][j]) + ' ')
            else:
                sys.stdout.write(str(centers[i][j]) + '\n')
            
            j += 1
        i += 1 

