import random


class Knapsack(object):

    def __init__(self, weight, value, max, nGen, pCross, pmutasi, nPop):
        self.nGen = 0
        self.weight = weight
        self.value = value
        self.pCross = 0
        self.pmutasi = 0
        self.nPop = 0
        self.max = max
        self.result = 0
        self.fitness = []
        self.nkrom = 0
        self.npop = 0
        self.pop = []

    def genpop(self, npop, nkrom):
        pop = [[int(round(random.random())) for i in range(nkrom)] for j in range(npop)]
        return pop

    def hitungFitness(self, krom, weight, value, max):
        w = 0
        v = 0
        for i in range(len(krom)):
            if krom[i] == 1:
                w += weight[i]
                v += value[i]
        if w > max:
            fitness = 0
        else:
            fitness = v
        return fitness

    def randomparent(self, npop):
        return int(round(random.uniform(0, npop)))

    def crossover(self, a1, a2):
        rand = random.random()
        titik = int(round(random.uniform(1, self.nkrom - 1)))
        if rand <= self.pCross:
            for k in range(titik):
                a1[k], a2[k] = a2[k], a1[k]

    def mutation(self, a):
        rand = random.random()
        titik = int(round(random.uniform(0, self.nkrom - 1)))
        if rand <= self.pmutasi:
            if a[titik] == 0:
                a[titik] = 1
            else:
                a[titik] = 0

    def sort_fitness(self):
        return sorted(range(len(self.fitness)), key=lambda k: self.fitness[k], reverse=True)

    def fit(self, nGen=100, pCross=0.8, pmutasi=0.2, nPop=20):

        self.nGen = nGen
        self.pCross = pCross
        self.pmutasi = pmutasi
        self.nPop = nPop

        self.nkrom = len(self.weight)
        self.pop = self.genpop(self.nPop, self.nkrom)
        
        for i in range(self.nGen):

            self.fitness = []
            anak = []

            for j in range(self.nPop // 2):

                parent1 = self.randomparent(self.nPop - 1)
                parent2 = self.randomparent(self.nPop - 1)

                anak1 = self.pop[parent1][:]
                anak2 = self.pop[parent2][:]

                self.crossover(anak1, anak2)
                self.mutation(anak1)
                self.mutation(anak2)

                anak.append(anak1)
                anak.append(anak2)

            gab = self.pop + anak
            for f in range(len(gab)):
                self.fitness.append(self.hitungFitness(gab[f], self.weight, self.value, self.max))
            steadystate = self.sort_fitness()
            self.pop = []
            for j in range(self.nPop):
                self.pop.append(gab[steadystate[j]])

        self.result = self.pop[0]
        self.fitness = self.fitness[0]
