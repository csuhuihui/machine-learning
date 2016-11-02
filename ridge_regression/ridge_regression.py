# coding:utf-8
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math

Y = []
X=  [[0 for col in range(8)] for row in range(25)]

for i in range(25):
        x = random.random()
        for j in range(8):
            X[i][j] = pow(x,j)
        y = math.sin(2 * math.pi * x) + np.random.normal(loc=0.0, scale=0.1, size=None)
        Y.append(y)


def ridgeRegres(Xmat,Ymat,lam):
    denom = Xmat.T*Xmat + lam*eye(shape(Xmat)[1])  # w = (XT)
    if linalg.det(denom) == 0:
        print "error"
        return
    w = denom.I*(Xmat.T*Ymat)
    return w

Xmat,Ymat = mat(X),mat(Y).T  #将Y转置成25行1列的矩阵，与X对应
ws = ridgeRegres(Xmat,Ymat,lam= 0.0001)
print ws
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(Xmat[:,1].flatten().A[0],Ymat[:,0].flatten().A[0])
xHat = Xmat.copy()
xHat.sort(0)
yHat = xHat * ws
ax.plot(xHat[:,1],yHat)
plt.show()