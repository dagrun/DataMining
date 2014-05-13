#!/usr/bin/env python2.7

import sys
import numpy as np
import random
import matplotlib.pyplot as plt

points = []
for x in xrange(30):
    points.append([random.random(),random.random()])
    points.append([random.random(),random.random()])
    points.append([random.random(),random.random()])
    points.append([random.random(),5+random.random()])
    points.append([5+random.random(),5+random.random()])
    
print(points)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
trans = zip(*points)
x = trans[0]
y = trans[1]
ax.scatter(x, y)

fig.show()
plt.savefig('out.png')
