# GeneticAlgorithm
from chromosome import chromosome
from constants import *


def Initialise_Population(pop_size):
    '''Initializes chromosones to construct the initial population'''
    pop = []
    for i in range(pop_size):
        individual = []
        for j in range(BEATS_PER_SECTION):
            individual.append(chromosome())
        pop.append(individual)
    return pop


'''
SELECTION SCHEME
As a learning outcome from Assignment 01,
we have concluded that Eliticism works best hence, the selected selection scheme for this algorithm is,
Parent Selection : Truncation
Survuval Selection: Truncation
'''

def Truncation():
    pass


def total_fitness(individual):
    '''
    Sums up fitness of every bar
    '''
    for _ in range(BARS_PER_SECTION):
        pass

def fitness():
    '''
    Calculates fitness of one bar
    '''
    pass

def Crossover():
    pass


def Mutate():
    pass


def Evolve():
    pass


def main():
    Initialise_Population(POPULATION)
