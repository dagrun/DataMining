#!/usr/bin/env python2.7

import sys
import numpy as np
from sklearn import svm
from sklearn import linear_model
from sklearn import preprocessing

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
        X = np.vstack( (X, transform(all_data[1:])) )
    
    y = np.array(y)
    
#    clf = svm.SVC(C=10.0, kernel='linear', probability=True)
    clf = svm.LinearSVC(C=10.0, loss='l2', penalty='l1', dual=False)
#    clf = linear_model.SGDClassifier(alpha=0.0000003, loss='modified_huber', penalty='l2', n_iter=25, shuffle=False)
    clf.fit(X, y)
    
    emit(1, clf.coef_[0].tolist())

