import numpy as np
import math
import random


class MinimumFunction(object):

    def __init__(self):
        self.temperature = 0
        self.coolingrate = 0
        self.bestsolution = 0
        self.bestevaluation = 0

    def initialization(self):
        return np.random.uniform(-10, 10)

    def function(self, x, y):
        return -(abs(math.sin(x)*math.cos(y)*math.exp(abs(1 - (math.sqrt((x ** 2) + (y ** 2))) / math.pi))))

    def modification(self, x):
        value = np.random.uniform(-1, 1)
        while (x + value) < -10 or (x + value) > 10:
            value = np.random.uniform(-1, 1)
        x += value
        return x

    def fit(self, temperature=10000, coolingrate=0.999):
        self.temperature = temperature
        self.coolingrate = coolingrate

        x = self.initialization()
        y = self.initialization()

        self.bestsolution = [x, y]
        self.bestevaluation = self.function(self.bestsolution[0], self.bestsolution[1])
        current_solution = self.bestsolution[:]

        while temperature > 1:

            x = self.modification(current_solution[0])
            y = self.modification(current_solution[1])
            new_solution = [x, y]
            current_evaluation = self.function(current_solution[0], current_solution[1])
            new_evaluation = self.function(new_solution[0], new_solution[1])

            if new_evaluation < current_evaluation:
                current_solution = new_solution
                self.bestevaluation = self.function(self.bestsolution[0], self.bestsolution[1])
                if current_evaluation < self.bestevaluation:
                    self.bestsolution = current_solution[:]
            else:
                delta = new_evaluation - current_evaluation
                if math.exp(-delta / temperature) > random.random():
                    current_solution = new_solution

            self.temperature *= self.coolingrate
