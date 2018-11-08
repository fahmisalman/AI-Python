import matplotlib.pyplot as plt
import random
import numpy as np
import math


class TSP(object):

    def __init__(self, node, nGen, nPop, pCross, pMutasi):
        self.nGen = nGen
        self.nPop = nPop
        self.node = node
        self.pCross = pCross
        self.pMutasi = pMutasi
        self.pop = []
        self.fitness = 0
        self.jarak = 0
        self.jalur = []
        self.koordinat = []

    def plot(self):
        x = []
        y = []
        for i in range(len(self.pop[0])):
            x.append(self.node[self.pop[0][i]][0])
            y.append(self.node[self.pop[0][i]][1])
        x.append(self.node[self.pop[0][0]][0])
        y.append(self.node[self.pop[0][0]][1])
        plt.plot(x, y, linestyle='--', color='b', label='City')
        for i in range(len(x)):
            plt.scatter(x[i], y[i], marker='x', s=30, c='black', alpha=1)
        plt.plot(self.node[self.pop[0][0]][0], self.node[self.pop[0][0]][1], linestyle='--', color='b', label='Start')
        plt.show()

    def genpop(self, npop, nkrom):
        pop = []
        for i in range(npop):
            pop.append(np.random.permutation(nkrom))
        return pop

    def hitungfitness(self, krom):
        jarak = 0
        for i in range(len(krom) - 1):
            jarak += math.sqrt(sum((a - b) ** 2 for a, b in zip(self.node[krom[i]], self.node[krom[i + 1]])))
        jarak += math.sqrt(sum((a - b) ** 2 for a, b in zip(self.node[krom[i + 1]], self.node[krom[0]])))
        fitness = 1 / (jarak + 0.01)
        return fitness, jarak

    def randomparent(self, nPop):
        return int(round(random.uniform(0, nPop)))

    def crossover(self, krom1, krom2):
        rand = random.random()
        if rand <= self.pCross:
            titik1 = int(round(random.uniform(0, len(krom1) - 1)))
            titik2 = int(round(random.uniform(0, len(krom1) - 1)))
            if titik2 < titik1:
                titik1, titik2 = titik2, titik1
            tmp1 = []
            tmp2 = []
            for i in range(titik1, titik2 + 1):
                tmp1.append(krom1[i])
                tmp2.append(krom2[i])
                krom1[i], krom2[i] = krom2[i], krom1[i]
            j = 0
            for i in range(len(krom1)):
                if i < titik1 or i > titik2:
                    if krom1[i] in tmp2:
                        while j < len(tmp1) and tmp1[j] in tmp2:
                            j += 1
                        krom1[i] = tmp1[j]
                        j += 1
            j = 0
            for i in range(len(krom2)):
                if i < titik1 or i > titik2:
                    if krom2[i] in tmp1:
                        while j < len(tmp2) and tmp2[j] in tmp1:
                            j += 1
                        krom2[i] = tmp2[j]
                        j += 1
            status = True
        else:
            status = False
        return status, krom1, krom2

    def mutasi(self, krom):
        rand = random.random()
        if rand <= self.pMutasi:
            titik1 = int(round(random.uniform(0, len(krom) - 1)))
            titik2 = int(round(random.uniform(0, len(krom) - 1)))
            krom[titik1], krom[titik2] = krom[titik2], krom[titik1]
        return krom

    def fit(self):

        self.pop = self.genpop(self.nPop, len(self.node))

        steadystate = []
        fitness = []

        for i in range(self.nGen):

            fitness = []
            anak = []

            for j in range(int(self.nPop/2)):

                parent1 = self.randomparent(self.nPop-1)
                parent2 = self.randomparent(self.nPop-1)

                anak1 = np.copy(self.pop[parent1])
                anak2 = np.copy(self.pop[parent2])

                status, anak1, anak2 = self.crossover(anak1, anak2)

                if status:
                    anak1 = self.mutasi(anak1)
                    anak2 = self.mutasi(anak2)

                    anak.append(anak1)
                    anak.append(anak2)

            gab = self.pop + anak
            for f in range(len(gab)):
                fitness.append(self.hitungfitness(gab[f]))
            steadystate = sorted(range(len(fitness)), key=lambda k: fitness[k], reverse=True)
            self.pop = []
            for j in range(self.nPop):
                self.pop.append(gab[steadystate[j]])

        self.fitness = fitness[steadystate[0]][0]
        self.jarak = fitness[steadystate[0]][1]
        self.jalur.append(0)
        for i in range(len(self.pop[0])):
            self.jalur.append(self.pop[0][i]+1)
        self.jalur.append(0)
        for i in range(len(self.pop[0])):
            self.koordinat.append(self.node[self.pop[0][i]])
