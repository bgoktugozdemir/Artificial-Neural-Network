import numpy as np
import math


def net(w1, w2, i1, i2, b):
    return w1 * i1 + w2 * i2 + b


def out_with_neth(nethval):
    return 1 / (1 + math.exp(-nethval))


def out(w1, w2, i1, i2, b1):
    return out_with_neth(-net(w1, w2, i1, i2, b1))


def etotal(targetval, outval):
    return 0.5 * pow((targetval - outval), 2)


def sumetotal(target1, target2, out1, out2):
    return etotal(target1, out1) + etotal(target2, out2)


def integral_etotal_w(targetval, outval):
    return (-(targetval - outval)) * (outval * (1 - outval)) * outval


def new_w(integralval, w, n):
    return w - n * integralval


def new_w_short(o1, outo1, w, n):
    return new_w(integral_etotal_w(o1, outo1), w, n)


def calculatebackpropagation(n, i1, i2, w1, w2, w3, w4, w5, w6, w7, w8, o1, o2, b1, b2):
    neth1 = net(w1, w2, i1, i2, b1)
    outh1 = out_with_neth(neth1)

    neth2 = net(w3, w4, i1, i2, b1)
    outh2 = out_with_neth(neth2)

    neto1 = net(w5, w6, outh1, outh2, b2)
    outo1 = out_with_neth(neto1)

    neto2 = net(w7, w8, outh2, outh2, b2)
    outo2 = out_with_neth(neto2)

    sumetotalval = sumetotal(o1, o2, outo1, outo2)

    neww5 = new_w_short(o1, outo1, w5, n)

    print("ΣEtotal = {}".format(sumetotalval))
    print("w5' = {}".format(neww5))
