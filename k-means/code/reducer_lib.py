#!/usr/bin/env python2.7

import numpy as np
import sys
from ast import literal_eval
from sklearn.cluster import MiniBatchKMeans

num_centers = 200

if __name__ == "__main__":
    all_mappers = []
    np.random.seed(seed=42)
    
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        one_mapper = literal_eval(value)
        
        all_mappers += one_mapper
    
    all_mappers = np.asarray(all_mappers)
    
    mbk = MiniBatchKMeans(n_clusters=200, init='k-means++', n_init=5, batch_size=120)
    mbk.fit(all_mappers)
    
    i = 0
    values_list = mbk.cluster_centers_.tolist()
    while i < len(values_list):
        j = 0
        while j < len(values_list[i]):
            if j != len(values_list[i]) -1:
                sys.stdout.write(str(values_list[i][j]) + ' ')
            else:
                sys.stdout.write(str(values_list[i][j]) + '\n')
            
            j += 1
        i += 1

