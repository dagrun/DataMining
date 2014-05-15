#!/usr/bin/env python2.7

import numpy as np
import sys
from ast import literal_eval

num_centers = 200

if __name__ == "__main__":
    all_mappers = []
    np.random.seed()
    
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        one_mapper = literal_eval(value)
        
        all_mappers += one_mapper
    
    center_positions = np.random.randint(0, len(all_mappers), num_centers)
    new_center_positions = []
    for center_pos in center_positions:
        while center_pos in new_center_positions:
            center_pos = (center_pos + 1) % len(all_mappers)
        new_center_positions.append(center_pos)
    
    centers = [ all_mappers[i] for i in new_center_positions ]
    
    i = 0
    values_list = centers
    while i < len(values_list):
        j = 0
        while j < len(values_list[i]):
            if j != len(values_list[i]) -1:
                sys.stdout.write(str(values_list[i][j]) + ' ')
            else:
                sys.stdout.write(str(values_list[i][j]) + '\n')
            
            j += 1
        i += 1

