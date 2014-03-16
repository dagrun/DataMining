#!/usr/bin/env python

import numpy as np
import sys


def partition(video_id, shingles):
    for i in range(0,2):
        minShing = ((a[i]*shingles[0])+b[i])%1000
        for shingle in shingles:
            hashShingle = ((a[i]*shingle)+b[i])%1000
            if hashSingle < minShing:
                minShing = hashShingle
        sigmatrix[i,video_id] = minShing

if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    a = np.random.randint(1,1000,2)
    b = np.random.randint(0,1000,2)
    sigmatrix = np.array([], ndmin=2)
    
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)

