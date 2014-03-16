#!/usr/bin/env python

import numpy as np
import sys


def partition(video_id, shingles):
    minShing = ((a[0]*shingles[0])+b[0])%1000
    for shingle in shingles:
        hashShingle = ((a[0]*shingle)+b[0])%1000
        if hashSingle < minShing:
            minShing = hashShingle
    sigmatrix[0,video_id] = minShing

if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    a = np.random.randint(1,1000,20)
    b = np.random.randint(0,1000,20)
    sigmatrix = np.array([], ndmin=2)
    
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)
