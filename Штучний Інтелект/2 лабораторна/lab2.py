import operator
import math
import random
import numpy as np
from deap import algorithms, base, creator, tools, gp
from functools import partial


def division_operator(numenator, denumenator):
    return numenator / denumenator if denumenator != 0 else 1

def eval_func(individual):
    x, y, z = individual
    mse = 1 / (1 + (x - 2)**2 + (y + 1)**2 + (z - 1)**2)

    return mse,

def create_toolbox():
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, -10, 10)  # Діапазон для x, y, z
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", eval_func)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox

if __name__ == "__main__":
    random.seed(7)
    toolbox = create_toolbox()

    population = toolbox.population(n=2)
    algorithms.eaMuPlusLambda(population, toolbox, mu=10, lambda_=40, cxpb=0.7, mutpb=0.2, ngen=50, stats=None,
                              halloffame=None, verbose=True)

    best_individual = tools.selBest(population, k=1)[0]
    best_values = best_individual.fitness.values

    print("Знайдений максимум:", 1 / best_values[0])
    print("Параметри x, y, z:", best_individual)