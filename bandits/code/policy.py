#!/usr/bin/env python2.7

import numpy.random
from scipy.spatial.distance import cdist

previous = []
artWithUser = []
epsilon = 1

# Evaluator will call this function and pass the article features.
# Check evaluator.py description for details.
def set_articles(art):
    pass


# This function will be called by the evaluator.
# Check task description for details.
def update(reward):
    global epsilon
    epsilon = epsilon * 0.9
    if reward ==1:
        artWithUser.append(previous)

# This function will be called by the evaluator.
# Check task description for det    ails.
def reccomend(timestamp, user_features, articles):
    previous = []
    if len(previous) > 0 and random.random() > epsilon:
        prevUsers = artWithUser[:,:6]
        distances = cdist(user_features, prevUsers, 'euclidean')
        userIndex = distances.index(min(distances))
        prevArticle = artWithUser[userIndex]
        prevArticle = prevArticle[6:]
        distances = cdist(prevArticle, articles, 'euclidean')
        articleIndex = distances.index(min(distances))
        toReturn = articles[articleIndex]
        previous.append(user_features)
        previous.append(toReturn[1:])
        return toReturn
    toReturn = numpy.random.choice(articles, size=1)
    previous.append(user_features)
    previous.append(toReturn[1:])
    return toReturn
