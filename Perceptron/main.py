from Perceptron import perceptron
import numpy as np

n = 0.5
b = 0
threshold = -1
x = np.array([[1, 0], [0,1]])
w = np.array([1, 2])
d = np.array([1, 0])

perceptron.printPerceptron(n, b, x, w, d, threshold)

n = 0.2
b = -0.7
threshold = 0
x = np.array([[0, 0, 1]])
w = np.array([0.2, 0.7, 0.9])
d = np.array([0])

perceptron.printPerceptron(n, b, x, w, d, threshold)

n = 0.1
b = 0
threshold = 0
x = np.array([[0, 1, 0], [0, 0, 1], [0, 1, 1]])
w = np.array([0, 0, 0])
d = np.array([1, 1, 0])

perceptron.printPerceptron(n, b, x, w, d, threshold)

n = 0.5
b = 0
threshold = 0
x = np.array([[2, 0, 1], [0, 2, 1]])
w = np.array([1, 0, -1])
d = np.array([0, 1])

perceptron.printPerceptron(n, b, x, w, d, threshold)