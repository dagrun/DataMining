#!/usr/bin/env python

import numpy as np
import sys

def partition(video_id, shingles):
    sigmatrix.append([])
    # iterates over the number of hashfunctions
    for i in xrange(0,numOfHash):
        minShing = ((a[i]*shingles[0])+b[i])%10000
        # iterates over all the shingles in a video
        for shingle in shingles:
            hashShingle = ((a[i]*shingle)+b[i])%10000
            if hashShingle < minShing:
                minShing = hashShingle
        # store the smalest value for that video, using this hashfunction.
        sigmatrix[video_id].append(minShing)

if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    numOfHash = 2 # number of hash functions we want to use when making signature matrixes
    debug = False
    
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        debug = True
    
    a = np.random.randint(1,10000,numOfHash) # a is used to make the hashfunction a*i+b modula 10000
    b = np.random.randint(0,10000,numOfHash) # b is used to make the hashfunction a*i+b modula 10000
    
    if debug:
        for i in xrange(len(a)): print 'h_'+ str(i) + '(x) = x*'+ str(a[i]) +' + '+ str(b[i])
    
    sigmatrix = [] # used to store our signature matrix
    
    # iterates over the videos
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)
    
    sigmatrix = np.matrix(sigmatrix, np.int32).T
    
    if debug: print sigmatrix

