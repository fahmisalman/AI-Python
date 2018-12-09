import numpy as np
import os


class KNN(object):

    def __init__(self, kneighbors):
        self.k = kneighbors
        self.x_train = []
        self.y_train = []
        self.y_list = []
        os.chdir('..')

    def load_dataset(self, data):
        temp = np.loadtxt(open("%s/Sample-Datasets/%s.csv" % (os.path.abspath(os.curdir), data), "r"),
                          delimiter=",")
        return temp[:, 0:2], temp[:, 2]

    def fit(self, x, y):

        self.x_train = x
        self.y_train = y
        self.y_list = list(set(self.y_train))

    def predict(self, x):

        res = []

        for i in range(0, len(x)):
            euclid = []
            for j in range(0, len(self.x_train)):
                euclid.append(np.dot(x[i], self.x_train[j]) / (np.linalg.norm(x[i]) * np.linalg.norm(self.x_train[j])))
            index_sorted = sorted(range(len(euclid)), key=lambda k: euclid[k], reverse=True)
            index_value = []
            for j in range(self.k):
                index_value.append(self.y_train[index_sorted[j]])
            temp = [0] * len(self.y_list)
            for k in range(len(self.y_list)):
                temp[k] = index_value.count(self.y_list[k])
            res.append(self.y_list[temp.index(max(temp))])
        return res

    def score(self, x, y):
        sc = 0
        res = self.predict(x)
        for i in range(len(res)):
            if res[i] == y[i]:
                sc += 1
        sc /= len(res)
        return sc
