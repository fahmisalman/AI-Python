import numpy as np


class PSO(object):

    def __init__(self):
        self.cognition = 0
        self.social = 0
        self.nparticle = 0
        self.iteration = 0
        self.vmax = 0
        self.gbest = []
        self.min = 0

    def f(self, x, y):
        return -(abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - (np.sqrt((x ** 2) + (y ** 2))) / np.pi))))

    def fitnesscalculate(self, x1, x2):
        return 1 / self.f(x1, x2)

    def randuniform(self, a, b):
        return np.random.uniform(a, b)

    def initialization(self, a, b):
        return self.randuniform(a, b), self.randuniform(a, b)

    def velocity(self, v, p, x, pg):
        r = np.random.random()
        vc = []
        for d in range(len(v)):
            tmp = v[d] + self.cognition * r * np.subtract(p[d], x[d]) + self.social * r * np.subtract(pg[d], x[d])
            vc.append(tmp if (-self.vmax <= tmp <= self.vmax) else (tmp / abs(tmp)) * self.vmax)
        return vc

    def fit(self, cognition=0.5, social=0.3, n_particle=20, iteration=100, vmax=2):
        X = []
        P = []
        V = []
        x_fitness = []
        p_fitness = []

        self.iteration = iteration
        self.vmax = vmax
        self.cognition = cognition
        self.social = social
        self.nparticle = n_particle

        for i in range(self.nparticle):
            X.append(self.initialization(-10, 10))
            P.append(X[-1][:])
            V.append(self.initialization(-self.vmax, self.vmax))
            x_fitness.append([self.fitnesscalculate(X[-1][0], X[-1][1]), i])
            p_fitness.append(x_fitness[-1][:])

        for i in range(self.iteration):
            for j in range(self.nparticle):
                x_fitness[j][0] = self.fitnesscalculate(X[j][0], X[j][1])
                if x_fitness[j] > p_fitness[j]:
                    P[j] = X[j][:]
                    p_fitness[j] = x_fitness[j][:]
            self.gbest = P[max(p_fitness)[1]]
            for j in range(self.nparticle):
                V[j] = self.velocity(V[j], P[j], X[j], self.gbest)
                X[j] = np.add(X[j], V[j])
                for k in range(len(X[j])):
                    while X[j][k] > 10 or X[j][k] < -10:
                        X[j][k] = self.randuniform(-10, 10)

        self.min = self.f(self.gbest[0], self.gbest[1])
