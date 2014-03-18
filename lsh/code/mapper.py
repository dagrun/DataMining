#!/usr/bin/env python

import numpy as np
import sys

def emit(key, value):
    print('%s\t%s' % (key, value))

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
    numOfHash = 256 # number of hash functions we want to use when making signature matrixes
    bands = 32
    rowsPerBand = numOfHash / bands
    verbose = False
    
    if len(sys.argv) > 1 and sys.argv[1] == '-v':
        verbose = True
    
    a = np.random.randint(1,10000,numOfHash) # a is used to make the hashfunction a*i+b modula 10000
    b = np.random.randint(0,10000,numOfHash) # b is used to make the hashfunction a*i+b modula 10000
    
    if verbose:
    	print str(numOfHash) +' hash functions'
    	print str(bands) +' bands'
    	print str(rowsPerBand) +' rows per band'
        for i in xrange(len(a)): print 'h_'+ str(i) +'(x) = x*'+ str(a[i]) +' + '+ str(b[i])
    
    sigmatrix = [] # used to store our signature matrix
    
    # iterates over the videos
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)
        # do stuff here
    
    sigmatrix = np.matrix(sigmatrix, np.int32).T
    
    if verbose:
        print 'dimensions of the signature matrix '+ str(sigmatrix.shape)
        print sigmatrix
    
    a = np.random.randint(1,10000,rowsPerBand)
    b = np.random.randint(0,10000,rowsPerBand)
    
    #print b.shape
    #b = np.tile(b, (rowsPerBand, 1))
    #print b.shape
    
    for bid in xrange(bands):
        currentBand = sigmatrix[bid*rowsPerBand:(bid+1)*rowsPerBand]
        
        buckets = a.dot(currentBand) % numOfHash
        for i in xrange():
            emit((bid, buckets.item(i)), i)

