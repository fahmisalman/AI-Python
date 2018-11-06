import numpy as np
import math
import os

os.chdir('../..')


class MultinomialNB():

    def __init__(self):
        self.prior = []
        self.likelihood = []
        self.list_label = []

    def load_dataset(self, data):
        temp = np.loadtxt(open("%s/Sample-Datasets/%s.csv" % (os.path.abspath(os.curdir), data), "r"), delimiter=",")
        return temp[:, 0:2], temp[:, 2]

    def prior_probability(self, y, a):
        prior = []
        for i in range(len(a)):
            temp = 0
            for j in range(len(y)):
                if a[i] == y[j]:
                    temp += 1
            temp += 1
            prior.append(temp)
        for i in range(len(prior)):
            prior[i] /= len(y)
        return y

    def likelihood_probability(self, x, y, a):
        l = []
        for i in range(len(a)):
            temp = []
            for j in range(len(y)):
                if y[j] == a[i]:
                    temp.append(x[j])
            l.append(sum(temp) + 1)
        return l

    def fit(self, data, label):

        self.list_label = list(set(label))

        self.prior = self.prior_probability(label, self.list_label)

        for i in range(len(data[0])):
            self.likelihood.append(self.likelihood_probability(np.array(data)[:, i], label, self.list_label))

        self.likelihood = np.array(self.likelihood)

        total = []
        for i in range(len(self.likelihood[0])):
            total.append(sum(self.likelihood[:, i]))

        for i in range(len(self.likelihood)):
            for j in range(len(self.likelihood[i])):
                self.likelihood[i][j] /= total[j]
        print(self.likelihood)

    def predict(self, data):
        temp = [0] * len(self.list_label)
        for j in range(len(data)):
            for k in range(len(self.list_label)):
                temp[k] += math.log(self.likelihood[j][k] ** data[j])
        for i in range(len(self.list_label)):
            temp[i] += math.log(self.prior[i])
        return self.list_label[temp.index(max(temp))]
