from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def load_dataset(data):
    temp = np.loadtxt(open("Sample-Datasets/%s" % data, "r"), delimiter=",")
    return temp[:, 0:2], temp[:, 2]


def scatter_plot2d(x, y):
    plt.scatter(x[:, 0], x[:, 1], s=30, c=y[:], alpha=0.2)
    plt.show()


def scatter_plot3d(x, y):
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    plt.scatter(x[:, 0], x[:, 1], x[:, 2], s=30, c=y[:], alpha=0.2)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
