#!/usr/bin/env python2.7

import numpy as np
import sys
from ast import literal_eval

def compare_shingles(id1, id2):
    shingle1 = set(shingles[id1])
    shingle2 = set(shingles[id2])
    return len(shingle1.intersection(shingle2)) / float(len(shingle1.union(shingle2)))

def print_duplicates(videos):
    unique = np.unique(videos)
    for i in xrange(len(unique)):
        for j in xrange(i + 1, len(unique)):
            if compare_shingles(unique[i], unique[j]) >= 0.85:
                print "%d\t%d" % (min(unique[i], unique[j]),
                              max(unique[i], unique[j]))
    
last_key = None
key_count = 0
duplicates = []
shingles = {}

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    value = literal_eval(value)
    video_id = value[0]
    shingle = value[1]
    
    shingles[video_id] = shingle

    if last_key is None:
        last_key = key

    if key == last_key:
        duplicates.append(int(video_id))
    else:
        # Key changed (previous line was k=x, this line is k=y)
        print_duplicates(duplicates)
        duplicates = [int(video_id)]
        last_key = key

if len(duplicates) > 0:
    print_duplicates(duplicates)
