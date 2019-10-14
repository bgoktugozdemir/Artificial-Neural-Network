import numpy as np


def printPerceptron(n, b,  x, w, d, threshold=0):
    print('X = '+str(x)+'\nW = '+str(w))
    perceptron(n, b, x, w, d, threshold)
    print()


def perceptron(n, b,  x, w, d, threshold=0):
    for i in range(0, len(x), 1):
        fNetVal = fnet(net(b, x[i], w), threshold)
        if fNetVal != d[i]:
            w = difW(n, error(d[i], fNetVal), x[i], w)
        print('W'+str(i+1)+' = '+str(w))
    return w


def net(b, x, w):
    return b + np.dot(x, w)


def fnet(net, threshold=0):
    if net > threshold:
        return 1
    return 0


def error(d, y):
    return d-y


def difW(n, e, x, w):
    return w + n * e * x