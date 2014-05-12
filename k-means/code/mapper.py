#!/usr/bin/env python2.7

import sys
import numpy as np
from sklearn.cluster import MiniBatchKMeans

def emit(key, value):
    print('%s\t%s' % (key, value))

if __name__ == "__main__":
    X = np.zeros(shape=(0, 750))
    for line in sys.stdin:
        sample = np.fromstring(line, sep=" ")
        
        X = np.vstack( (X, sample) )
    
    
    mbk = MiniBatchKMeans(n_clusters=200, init='k-means++', n_init=5)

    mbk.fit(X)
    centers_weighted = mbk.cluster_centers_
    closest_center = mbk.fit_predict(X)
    centers_weighted = np.hstack((centers_weighted, np.zeros(shape=(200,1)))) 
    for center in closest_center:
        centers_weighted[center][750]=centers_weighted[center][750]+1
    i = 0
    for elem in centers_weighted:
        if elem[750]<0.1337 :
            centers_weighted = np.delete(centers_weighted,i,0)
        else:
            i+=1
    emit(1, centers_weighted.tolist())

