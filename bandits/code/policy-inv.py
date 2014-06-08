#!/usr/bin/env python2.7

import numpy as np

d = 6
alpha = 0.2

x_t = -1 # recommended article in this round
z_t = [] # user features in this round 6x1 vector

article_features = {}
M_x = {}
M_x_inv = {}
b_x = {}

# Evaluator will call this function and pass the article features.
# Check evaluator.py description for details.
def set_articles(art):
    pass

# This function will be called by the evaluator.
# Check task description for details.
def update(reward):
    global M_x
    global M_x_inv
    global b_x
    
    if reward >= 0:
        M_x[x_t] += np.dot(z_t, z_t.T)
        M_x_inv[x_t] = np.linalg.inv(M_x[x_t])
        b_x[x_t] += reward * z_t

# This function will be called by the evaluator.
# Check task description for details.
def reccomend(timestamp, user_features, articles):
    global M_x
    global M_x_inv
    global b_x
    global x_t
    global z_t
    
    UCB_x = []
    
    z_t = np.matrix(user_features).T
    z_tT = z_t.T
    
    for art in articles:
        if art not in M_x:
            M_x[art] = np.identity(d)
            b_x[art] = np.zeros((d, 1))
            M_x_inv[art] = np.copy(M_x[art])

        M_x_inverse = M_x_inv[art]

        UCB_x.append(np.dot(np.dot(M_x_inverse, b_x[art]).T, z_t) + alpha * np.sqrt( np.dot(z_tT, np.dot(M_x_inverse, z_t)) ))

    x_t = articles[np.argmax(UCB_x)]

    return x_t

