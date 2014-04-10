#!/usr/bin/env python2.7

import numpy as np
import sys
from ast import literal_eval

values = []

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        value = np.asarray(literal_eval(value))
        
        values.append(value)
    
    result = np.zeros_like(values[0])
    for v in values:
        result = np.add(result, v)
    
    print ' '.join(map(str, (v / float(len(values))).tolist() ) )

