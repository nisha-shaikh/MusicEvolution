# Genetic Algorithm fpr Music Composition

from chromosome import chromosome
from constants import *


def Initialise_Population(pop_size):
    '''Initializes chromosones to construct the initial population'''
    pop = []
    for i in range(pop_size):
        pop.append(chromosome())
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


def Crossover():
    pass


def Mutate():
    pass


def Evolve():
    pass


def main():
    Initialise_Population(POPULATION)
