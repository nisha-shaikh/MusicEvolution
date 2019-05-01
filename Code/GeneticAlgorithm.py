# Genetic Algorithm for Music Composition

from chromosome import chromosome
from constants import GENERATIONS, MUTATION_RATE, POP_SIZE
import random

# Take user inputs to allow controlling parameters--TESTING PURPOSE ONLY.
# The fixed parameters in constants.py

# ITER = int(input("Enter the number of iterations: "))
# POP_SIZE = int(input("Enter population size: "))
# MUTATION_RATE = float(input("Enter mutation rate between 0 and 1: "))
# GENERATIONS = int(input("Enter number of generations: "))



def Initialise_Population(pop_size):
    '''Initializes chromosones to construct the initial population'''
    pop = []
    for _ in range(pop_size):
        new = chromosome("R")
        pop.append(new)
    return pop



# SELECTION SCHEME
# As a learning outcome from Assignment 01,
# we have concluded that Eliticism works best hence, the selected selection scheme for this algorithm is,
# Parent Selection : Truncation
# Survivor Selection: Truncation

# Sel signifies P or S selection where P is parent and S is survivor
def Truncation(population, Sel):
    new = sorted(population, key=lambda x: x.fitness,
                 reverse=True)  # Descending order
    if (Sel == "P"):  # parent selection
        Parents = new[:2]
        return Parents
    elif (Sel == "S"):
        Top_fit = new[:POP_SIZE]
        return Top_fit
    else:
        print("Selection is not identified")


def BinaryTournament(population, sel):
    '''
    Select the fittest chromosome between 2 randomly selected chromosomes
    '''
    orig = population[:]
    kill = False    # kill off least fit individuals if population is greater than POP_SIZE
    fittest = []
    if sel == 'S':
        kill = True
        loop = len(population) - POP_SIZE
    elif sel == 'P':
        loop = 2
    for _ in range(loop) :
        chosen = random.sample(orig, 2)
        if not kill:
            if chosen[0].fitness < chosen[1].fitness:
                fittest.append(chosen[1])
            else:
                fittest.append(chosen[0])
        else:
            if chosen[0].fitness < chosen[1].fitness:
                fittest.append(chosen[0])
            else:
                fittest.append(chosen[1])
    return fittest


def Mutate(population, rate):
    for i in range(0, len(population)):
        population[i].mutate(rate)
    return population


def Evolve(population):
    for gen in range(0, GENERATIONS):
        print("Generation: ", gen)

        if (gen % 20 == 0):
            # To record the best melody after every 20 gen
            new = sorted(population, key=lambda x: x.fitness, reverse=True)
            best_melody = new[0]
            best_melody.genMusic("gen{}".format(gen))

        # parents = Truncation(population, "P")
        parents = BinaryTournament(population, 'P')

        offsprings = parents[0].crossover(parents[1])

        population.append(chromosome(offsprings[0]))
        population.append(chromosome(offsprings[1]))

        newpop = Mutate(population, MUTATION_RATE)
        next_gen = Truncation(newpop, "S")
        population = next_gen
    return population


def main():
    myMelodies = Initialise_Population(POP_SIZE)
    myMelodies = Evolve(myMelodies)
    new = sorted(myMelodies, key=lambda x: x.fitness, reverse=True)
    best_melody = new[0]
    best_melody.genMusic("Final")


main()
