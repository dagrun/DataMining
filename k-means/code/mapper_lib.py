#!/usr/bin/env python2.7

import sys
import numpy as np
from sklearn.cluster import MiniBatchKMeans

store = False

def emit(key, value):
    print('%s\t%s' % (key, value))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-s':
        store = True

    X = np.zeros(shape=(0, 750))
    for line in sys.stdin:
        sample = np.fromstring(line, sep=" ")
        
        X = np.vstack( (X, sample) )
    
    mbk = MiniBatchKMeans(n_clusters=250, init='k-means++', n_init=7, batch_size=150)
    mbk.fit(X)
    
    if store:
        import pickle
        pickle.dump(mbk, open('mbk.pickle', 'wb'))
    
    emit(1, mbk.cluster_centers_.tolist())

