#!/usr/bin/env python2.7

import numpy as np

t = 1 # round

j = -1 # chosen arm in this round

article_features = {}
mu_x = {}
n_x = {}

# Evaluator will call this function and pass the article features.
# Check evaluator.py description for details.
def set_articles(art):
    global article_features
    global mu_x
    global n_x
    
    article_features = art
    
    for k in article_features.keys():
        mu_x[k] = 0
        n_x[k] = 1

# This function will be called by the evaluator.
# Check task description for details.
def update(reward):
    global mu_x
    global n_x
    
    mu_x[j] += (reward - mu_x[j]) / n_x[j]
    n_x[j]  += 1

# This function will be called by the evaluator.
# Check task description for details.
def reccomend(timestamp, user_features, articles):
    global mu_x
    global n_x
    global t
    global j
    
    all_UCB = [ mu_x[art] + np.sqrt((2 * np.log(t)) / n_x[art]) for art in articles ]
    
    j = articles[np.argmax( all_UCB )]
    
    t += 1
    
    return j

