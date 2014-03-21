#!/usr/bin/env python2.7

import numpy as np
import sys

def emit(key, value):
    print('%s\t%s' % (key, value))

def partition(video_id, shingles):
    sigcol = []
    # iterates over the number of hashfunctions
    for i in xrange(0,numOfHash):
        minShing = ((a[i]*shingles[0])+b[i])%10000
        # iterates over all the shingles in a video
        for shingle in shingles:
            hashShingle = ((a[i]*shingle)+b[i])%10000
            if hashShingle < minShing:
                minShing = hashShingle
        # store the smalest value for that video, using this hashfunction.
        sigcol.append(minShing)
    return sigcol

verbose = False
numOfHash = 256 # number of hash functions we want to use when making signature matrixes
bands = 16
rowsPerBand = numOfHash / bands

if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    
    
    if len(sys.argv) > 1 and sys.argv[1] == '-v':
        verbose = True
    
    a = np.random.randint(1,10000,numOfHash) # a is used to make the hashfunction a*i+b modula 10000
    b = np.random.randint(0,10000,numOfHash) # b is used to make the hashfunction a*i+b modula 10000
    
    if verbose:
    	print str(numOfHash) +' hash functions'
    	print str(bands) +' bands'
    	print str(rowsPerBand) +' rows per band'
        for i in xrange(len(a)): print 'h_'+ str(i) +'(x) = x*'+ str(a[i]) +' + '+ str(b[i])
    
    aBand = np.random.randint(1,10000,rowsPerBand).T
    bBand = np.random.randint(0,10000,1)
    
    if verbose:
    	print '-------------------------------'
    	print str(rowsPerBand) +' hash functions'
        for i in xrange(len(aBand)): print 'h_'+ str(i) +'(x) = x*'+ str(aBand[i]) +' + '+ str(bBand[0])
    
    # iterates over the videos
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], np.int32, sep=" ")
        
        sigcol = partition(video_id, shingles)
        sigcol = np.array(sigcol, np.int32)
        
        for bid in xrange(bands):
            currentBand = sigcol[bid*rowsPerBand:(bid+1)*rowsPerBand]
            
            hashValue = (aBand.dot(currentBand) + bBand).item(0)
            
            if verbose:
                print str(currentBand) +' mapped into '+ str(hashValue)
            
            emit((bid, hashValue), (video_id, shingles.tolist()))

