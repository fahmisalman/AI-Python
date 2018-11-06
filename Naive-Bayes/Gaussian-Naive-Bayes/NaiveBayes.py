import numpy as np
import math
import os


class GaussianNB():

    def __init__(self):
        self.prior = []
        self.likelihood = []
        self.list_label = []
        os.chdir('../..')

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
        mean = []
        std = []
        for i in range(len(a)):
            temp = []
            for j in range(len(y)):
                if y[j] == a[i]:
                    temp.append(x[j])
            mean.append(self.function_mean(temp))
            std.append(self.function_standard_deviation(temp))
        return mean, std

    def function_mean(self, x):
        return sum(x)/len(x)

    def function_variance(self, x):
        m = self.function_mean(x)
        temp = 0
        for i in range(len(x)):
            temp += (x[i] - m) ** 2
        temp /= (len(x) - 1)
        return temp

    def function_standard_deviation(self, x):
        return math.sqrt(self.function_variance(x))

    def learning_phase(self, x, m, std):
        return 1 / (std * math.sqrt(2 * math.pi)) * math.exp(- (x - m) ** 2 / (2 * std) ** 2)

    def fit(self, data, label):

        self.list_label = list(set(label))

        self.prior = self.prior_probability(label, self.list_label)

        for i in range(len(data[0])):
            self.likelihood.append(self.likelihood_probability(np.array(data)[:, i], label, self.list_label))

    def predict(self, data):
        temp = [0] * len(self.list_label)
        for j in range(len(data)):
            for k in range(len(self.list_label)):
                temp[k] += math.log(self.learning_phase(data[j], self.likelihood[j][0][k], self.likelihood[j][1][k]))
        for i in range(len(self.list_label)):
            temp[i] += math.log(self.prior[i])
        return self.list_label[temp.index(max(temp))]


if __name__ == '__main__':

    clf = GaussianNB()
    data, label = clf.load_dataset('R15')

    clf.fit(data, label)

    predict = []

    for i in range(len(data)):
        predict.append(clf.predict(data[i]))

    benar = 0

    for i in range(len(data)):
        if predict[i] == label[i]:
            benar += 1
    print(benar/len(data))
