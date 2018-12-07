import numpy as np
import csv
import math


class KNN(object):

    def __init__(self, k):
        self.k = k

    def fit(self, ):

        data = []
        y_list = list(set(y_train))

        # label = []
        correct = 0
        for i in range(0, len(x_test)):
            euclid = []
            for j in range(0, len(x_train)):
                n = 0
                # for l in range(0, len(x_test[0])):
                #     n += (float(x_test[i][l]) - float(x_train[j][l])) ** 2
                # n = math.sqrt(n)
                n = np.dot(x_test[i], x_train[j]) / (np.linalg.norm(x_test[i]) * np.linalg.norm(x_train[j]))
                euclid.append(n)
            indexSorted = sorted(range(len(euclid)), key=lambda k: euclid[k], reverse=True)
            indexValue = []
            for j in range(k):
                indexValue.append(y_train[indexSorted[j]])
            temp = [0] * len(y_list)
            for i in range(len(y_list)):
                temp[i] = indexValue.count(y_list[i])
            # print(temp)
            # print(y_list[temp.index(max(temp))])
            # label.append(y_list[temp.index(max(temp))])
            label = y_list[temp.index(max(temp))]
            if label == y_test[i]:
                correct += 1
        print(correct / len(y_test))

def loadTrain():
    data = []
    with open('Dataset Tugas 3 AI 1718/DataTrain-Table 1.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    return data


def loadTest():
    data = []
    with open('Dataset Tugas 3 AI 1718/DataTest-Table 1.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    return data


if __name__ == '__main__':

    dataTest = loadTest()
    dataTrain = loadTrain()

    k = 9

    jml = 0

    nol = 0
    satu = 0

    data = []

    label = []
    for i in range(1, len(dataTest)):
        euclid = []
        for j in range(1, len(dataTrain)):
            n = 0
            for l in range(1, 5):
                n += (float(dataTest[i][l]) - float(dataTrain[j][l])) ** 2
            n = math.sqrt(n)
            euclid.append(n)
        indexSorted = sorted(range(len(euclid)), key=lambda k: euclid[k])
        indexValue = []
        for j in range(k):
            indexValue.append(dataTrain[indexSorted[j]][5])
        satu = indexValue.count('1')
        nol = indexValue.count('0')
        # print indexValue
        if satu > nol:
            label.append('1')
        else:
            label.append('0')
    print(label)
    # correct = 0
    # for i in range(len(label)):
    #     if label[i] == dataTrain[i][5]:
    #         correct += 1
    # print(correct/(len(dataTrain)-1))

    # temp = np.array(data)
    # temp = temp.transpose()

    # np.savetxt("label.csv", temp, delimiter=",", fmt="%s")


    # for i in range(1, len(dataTest)):
    #     euclid = []
    #     for j in range(1, len(dataTrain)):
    #         n = 0
    #         for l in range(1, 5):
    #             n += (float(dataTest[i][l]) - float(dataTrain[j][l])) ** 2
    #         n = math.sqrt(n)
    #         euclid.append(n)
    #     indexSorted = sorted(range(len(euclid)), key=lambda k: euclid[k])
    #     indexValue = []
    #     for j in range(k):
    #         indexValue.append(dataTrain[indexSorted[j]+1][5])
    #     satu = indexValue.count('1')
    #     nol = indexValue.count('0')
    #     # print indexValue
    #     if satu > nol:
    #         label.append(1)
    #     else:
    #         label.append(0)

