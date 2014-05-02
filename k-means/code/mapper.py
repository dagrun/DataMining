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
    
    mbk = MiniBatchKMeans(init='k-means++', n_clusters=200)
    mbk.fit(X)
#    mbk_means_labels = mbk.labels_
    mbk_means_cluster_centers = mbk.cluster_centers_
    
#    mbk_means_labels_unique = np.unique(mbk_means_labels)
    
    emit(1, mbk_means_cluster_centers.tolist())

