import numpy as np
import math


class KMeans(object):

    def __init__(self):
        self.centroid = []
        self.error = []
        self.index = []
        np.random.seed(seed=1)

    def initialize_centroid(self, k, minx, miny, rangex, rangey):
        centroid = []
        for i in range(k):
            centroid.append([np.random.uniform(minx, rangex), np.random.uniform(miny, rangey)])
        return centroid

    def new_centroid(self, k, x, lab):
        for i in range(len(k)):
            a = 0
            b = 0
            n = 0
            for j in range(len(x)):
                if lab[j] == i:
                    a += x[j][0]
                    b += x[j][1]
                    n += 1
            if n > 0:
                a /= n
                b /= n
                k[i] = [a, b]
        return k

    def sse(self, k, x, lab):
        er = 0
        for i in range(len(k)):
            for j in range(len(x)):
                if lab[j] == i:
                    a = (k[i][0] - x[j][0]) ** 2
                    b = (k[i][1] - x[j][1]) ** 2
                    er += (a + b)
        return er

    def sum_centroid(self, k):
        temp = 0
        for i in range(len(k)):
            temp += sum(k[i])
        return temp

    def fit(self, data, cluster):
        centroid = np.array(self.initialize_centroid(cluster,
                                                     np.amin(np.array(data)[:, 0]),
                                                     np.amin(np.array(data)[:, 1]),
                                                     np.amax(np.array(data)[:, 0]),
                                                     np.amax(np.array(data)[:, 1])))

        stop = self.sum_centroid(self.centroid)
        start = 0

        while start != stop:

            start = stop
            self.index = []
            for i in range(len(data)):
                distance = []
                for j in range(len(centroid)):
                    distance.append(math.sqrt(sum([(a - b) ** 2 for a, b in zip(data[i],
                                                                                centroid[j])])))
                self.index.append(distance.index(min(distance)))

            self.centroid = self.new_centroid(self.centroid, data, self.index)
            self.error = self.sse(self.centroid, data, self.index)
            stop = self.sum_centroid(self.centroid)
