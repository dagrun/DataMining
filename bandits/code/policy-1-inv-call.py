#!/usr/bin/env python2.7

import numpy as np

d = 6
alpha = 0.001

x_t = -1 # recommended article in this round
z_t = [] # user features in this round 6x1 vector

article_features = {}
M_x = {}
b_x = {}

# Evaluator will call this function and pass the article features.
# Check evaluator.py description for details.
def set_articles(art):
    global article_features
    global M_x
    global b_x
    
    article_features = art
    
    I = np.identity(d)
    Z = np.zeros((d, 1))
    for k in article_features.keys():
        M_x[k] = np.copy(I)
        b_x[k] = np.copy(Z)

# This function will be called by the evaluator.
# Check task description for details.
def update(reward):
    global M_x
    global b_x
    
    M_x[x_t] += np.dot(z_t, z_t.T)
    b_x[x_t] += reward * z_t

# This function will be called by the evaluator.
# Check task description for details.
def reccomend(timestamp, user_features, articles):
    global x_t
    global z_t
    
    UCB_x = []
    
    z_t = np.matrix(user_features).T
    
    all_M_x = [ M_x[art] for art in articles ]
    all_M_x_inverse = np.linalg.inv(all_M_x)
    
    all_b_x = [ b_x[art] for art in articles ]
    
    for i in xrange(len(articles)):
        predicted_w_x = np.dot(all_M_x_inverse[i], all_b_x[i])
        
        aux = np.dot(predicted_w_x.T, z_t)
        UCB_x.append( aux + alpha * np.sqrt( np.dot(z_t.T, np.dot(all_M_x_inverse[i], z_t)) ) )
    
    x_t = articles[np.argmax( UCB_x )]
    
    return x_t

