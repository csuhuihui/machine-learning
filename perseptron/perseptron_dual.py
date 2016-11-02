# coding:utf-8
from numpy import *
import numpy

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

#判断有无误分类点
def discuss(gramMat,a,b,dataMat,labelMat):
    for i in range(shape(dataMat)[0]):
        sum = 0
        for j in range(shape(dataMat)[0]):
            sum += a[0,j]*labelMat[j,0]*(gramMat[i,j])
        if(labelMat[i,0]*(sum+b) <= 0):
            return True
    return False

#获取误分类点坐标
def get(gramMat,a,b,dataMat,labelMat):
    for i in range(shape(dataMat)[0]):
        sum = 0
        for j in range(shape(dataMat)[0]):
            sum += a[0, j] * labelMat[j, 0] * (gramMat[i, j])
        if (labelMat[i, 0] * (sum + b) <= 0):
            #print labelMat[i, 0] * (sum + b)
            #print gramMat[i]
            return i,labelMat[i,0]

# 更新a，b
def update(a,b,i,label):
    global lam
    a[0,i] += 1
    b = b + lam * label
    return a,b

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
    x = arange(-3, 3, 0.1)
    y = (-b - w[0, 0] * x) / w[0, 1]
    ax.plot(x, y)
    plt.xlabel("x1")  # X轴的标签
    plt.ylabel("x2")  # Y轴的标签
    plt.show()

if __name__ == "__main__":
    data,label = loadDataSet()
    dataMat = mat(data)
    labelMat = mat(label)
    gramMat = dataMat*dataMat.T
    a = mat([0,0,0])
    b = 0
    flag = discuss(gramMat,a,b,dataMat,labelMat)
    while(flag):
        i,label = get(gramMat,a,b,dataMat,labelMat)
        a,b = update(a,b,i,label)
        flag = discuss(gramMat, a,b, dataMat,labelMat)
    print a,b
    w1 = zeros([1,2])
    for i in range(shape(dataMat)[0]):
        w1 += dataMat[i]*labelMat[i,0]*a[0,i]
    print w1, b
    plot(w1, b, dataMat, labelMat)