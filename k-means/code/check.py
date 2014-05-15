#!/usr/bin/env python2.7
import sys
import numpy as np
import random

"""testing code"""

import warnings

import scipy.sparse as sp

from sklearn.metrics.pairwise import euclidean_distances
#from sklearn.utils.sparsefuncs import assign_rows_csr, mean_variance_axis0
from sklearn.utils import check_arrays
from sklearn.utils import check_random_state
from sklearn.utils import atleast2d_or_csr
from sklearn.utils import as_float_array
from sklearn.externals.joblib import Parallel
from sklearn.externals.joblib import delayed

from sklearn.cluster import _k_means

def calculate_inertia(X, x_squared_norms, centers):
    n_samples = X.shape[0]
    k = centers.shape[0]
    distances = euclidean_distances(centers, X, x_squared_norms,
                                    squared=True)
    labels = np.empty(n_samples, dtype=np.int32)
    labels.fill(-1)
    mindist = np.empty(n_samples)
    mindist.fill(np.infty)
    for center_id in range(k):
        dist = distances[center_id]
        #if for entry i, dist < mindist, replace that entry with center_id
        labels[dist < mindist] = center_id
        mindist = np.minimum(dist, mindist)
    inertia = mindist.sum()
    #inertia = weightdist.sum()
    return labels, inertia

def squared_norms(X):
    """Compute the squared euclidean norms of the rows of X"""
    if sp.issparse(X):
        return _k_means.csr_row_norm_l2(X, squared=True)
    else:
        # TODO: implement a cython version to avoid the memory copy of the
        # input data
        return (X ** 2).sum(axis=1)

if __name__ == "__main__":
	D = []
	for line in sys.stdin:
		S = line.split(' ')
		S = map(float, S)
		D.append(S)
	D = np.array(D)

	print "now loading data"
	# Load CSV file
	all_data = np.loadtxt(sys.argv[1])
	print "finished loading data"

	inertia = calculate_inertia(all_data, squared_norms(all_data), D)
	print "INERTIA: "
	print inertia[1]
