#!/usr/bin/env python2.7

import numpy.random
from scipy.spatial.distance import cdist

previos = []
artWithUser = []
epsilon = 1

# Evaluator will call this function and pass the article features.
# Check evaluator.py description for details.
def set_articles(art):
    pass


# This function will be called by the evaluator.
# Check task description for details.
def update(reward):
    if reward ==1
    artWithUser.append(previos)

# This function will be called by the evaluator.
# Check task description for det    ails.
def reccomend(timestamp, user_features, articles):
    previos = []
    if previsoly.length > 0 && random.random() > epsilon:
        prevUsers = artWithUser[:,:6]
        distances = cdist(user_features, artWithUser, 'euclidean')
        userIndex = distances.index(min(distances))
        prevArticle = artWithUser[userIndex]
        prevArticle = prevArticle[6:]
        distances = cdist(prevArticle, articles, 'euclidean')
        articleIndex = distances.index(min(distances))
        toReturn = articles[articleIndex]
        previos.append(user_features)
        previos.append(toReturn)
        return
    toReturn = numpy.random.choice(articles, size=1)
    previos.append(user_features)
    previos.append(toReturn)
    return toReturn
