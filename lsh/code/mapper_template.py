#!/usr/bin/env python

import numpy as np
import sys

def partition(video_id, shingles):
    sigmatrix.append([])
    for i in range(0,numOfHash):
        minShing = ((a[i]*shingles[0])+b[i])%10000
        for shingle in shingles:
            hashShingle = ((a[i]*shingle)+b[i])%10000
            if hashShingle < minShing:
                minShing = hashShingle
        sigmatrix[video_id].append(minShing)

if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    numOfHash = 2
    
    a = np.random.randint(1,10000,numOfHash)
    b = np.random.randint(0,10000,numOfHash)
    sigmatrix = []
    
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)
    
    sigmatrix = np.matrix(sigmatrix, np.int32)
    print sigmatrix.T

