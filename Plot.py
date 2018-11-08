import matplotlib.pyplot as plt
import numpy as np


def load_dataset(data):
    temp = np.loadtxt(open("Sample-Datasets/%s" % data, "r"), delimiter=",")
    return temp[:, 0:2], temp[:, 2]


def scatter_plot2d(x, y):
    plt.scatter(x[:, 0], x[:, 1], s=30, c=y[:], alpha=0.2)
    plt.show()
