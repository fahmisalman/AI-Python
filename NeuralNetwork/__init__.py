import numpy as np


class Backpropagation(object):

    def __init__(self):
        self.syn0 = 0
        self.syn1 = 1
        self.X = []
        self.y = []
        self.lr = 0
        self.epoch = 0
        self.error = []

    def forward(self):
        l1 = 1 / (1 + np.exp(-(np.dot(self.X, self.syn0))))  # A1
        l2 = 1 / (1 + np.exp(-(np.dot(l1, self.syn1))))  # A2
        return l1, l2

    def backward(self, l1, l2):
        l2_delta = (self.y - l2) * (l2 * (1 - l2))  # D2
        l1_delta = l2_delta.dot(self.syn1.T) * (l1 * (1 - l1))  # D1
        self.syn1 += np.dot(l1.T, l2_delta * self.lr)
        self.syn0 += np.dot(self.X.T, l1_delta * self.lr)

    def err(self, l2):
        self.error.append(sum((self.y - l2) ** 2))

    def fit(self, x_train, y_train, lr=0.01, epoch=100):

        self.X = x_train
        self.y = y_train

        n_input = len(self.X[0])
        n_hidden = 1
        n_output = len(self.y[0])

        self.lr = lr
        self.epoch = epoch
        self.syn0 = 2 * np.random.random((n_input, n_hidden)) - 1  # W1
        self.syn1 = 2 * np.random.random((n_hidden, n_output)) - 1  # W2

        for i in range(self.epoch):

            l1, l2 = self.forward()
            self.err(l2)
            self.backward(l1, l2)

        print(self.error)


if __name__ == '__main__':

    X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    y = np.array([[0, 1, 1, 1]]).T

    clf = Backpropagation()
    clf.fit(X, y)
