# coding:utf-8
import os
import sys
import types
from numpy import *

lam = 1   #步长

# 加载数据集
def loadDataSet():
    data = []
    label = []
    fp = open(r'F:\Python_data\perseptron_original_data.txt')
    for line in fp.readlines():
        lineArr = line.split()  # 分割
        data.append([float(lineArr[0]), float(lineArr[1])])
        label.append([int(lineArr[2])])

    return data, label

# 更新w，b
def update(w,b,data,label):
    global lam
    w = w + lam * label * data
    b = b + lam * label
    return w,b

#判断有无误分类点
def discuss(w,b,dataMat,labelMat):
    for i in range(shape(dataMat)[0]):
        if (labelMat[i, 0] * (w * dataMat[i, :].T + b) <= 0):
            return True
    return False

#获取误分类点坐标
def get(w,b,dataMat,labelMat):
    for i in range(shape(dataMat)[0]):
        if (labelMat[i, 0] * (w * dataMat[i, :].T + b) <= 0):
            return dataMat[i,:],labelMat[i,0]

#画图
def plot(w,b,dataMat,labelMat):
    import matplotlib.pyplot as plt
    x1 = [];y1 = []
    x2 = [];y2 = []
    for i in range(shape(dataMat)[0]):
        if (labelMat[i,0] == 1):
            x1.append(dataMat[i,0])
            y1.append(dataMat[i,1])
        else:
            x2.append(dataMat[i,0])
            y2.append(dataMat[i,1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x1, y1, s=30, c='red', marker='s')
    ax.scatter(x2, y2, s=30, c="green")
    x = arange(-5, 5, 0.1)
    y = (-b - w[0, 0] * x) / w[0, 1]
    ax.plot(x, y)
    plt.xlabel("x1")  # X轴的标签
    plt.ylabel("x2")  # Y轴的标签
    plt.show()

if __name__ == "__main__":
    data,label = loadDataSet()
    dataMat = mat(data)
    labelMat = mat(label)
    w = zeros([1,2])
    b = 0
    flag = discuss(w, b, dataMat, labelMat)
    while(flag):
        data,label = get(w,b,dataMat,labelMat)
        w,b = update(w,b,data,label)
        flag = discuss(w, b, dataMat, labelMat)
    print w,b
    plot(w, b, dataMat, labelMat)





