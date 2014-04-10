#!/usr/bin/env python2.7

import sys
import uuid
import numpy as np
from sklearn import svm

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x_original):
    return x_original

def emit(key, value):
    print('%s\t%s' % (key, value))

if __name__ == "__main__":
    X = np.zeros(shape=(0, 400))
    y = []
    for line in sys.stdin:
        all_data = np.fromstring(line, sep=" ")
        
        y.append(all_data.item(0))
        X = np.vstack( (X, all_data[1:]) )
    
    y = np.array(y)
    
    clf = svm.SVC(kernel='linear', gamma=0.001, C=100., verbose=True, max_iter=2)
    clf.fit(X, y)
#    print clf.coef_
    
#    emit(uuid.uuid4(), )

