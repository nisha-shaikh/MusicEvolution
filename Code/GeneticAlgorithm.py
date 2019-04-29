# Genetic Algorithm for Music Composition

from chromosome import chromosome
from constants import *
import random

# Take user inputs to allow controlling parameters
'''
ITER = int(input("Enter the number of iterations: "))
POP_SIZE = int(input("Enter population size: "))
MUTATION_RATE = float(input("Enter mutation rate between 0 and 1: "))
GENERATIONS = int(input("Enter number of generations: "))
'''

#Fixed parameters
ITER = 10
POP_SIZE = 30
MUTATION_RATE = 0.5
GENERATIONS = 100

def Initialise_Population(pop_size):
    '''Initializes chromosones to construct the initial population'''
    pop = []
    for i in range(pop_size):
        new=chromosome()
        pop.append(new)
    return pop

'''
SELECTION SCHEME
As a learning outcome from Assignment 01,
we have concluded that Eliticism works best hence, the selected selection scheme for this algorithm is,
Parent Selection : Truncation
Survivor Selection: Truncation
'''
def gen_chromosone():
    octave_idx = random.choice(OCTAVE_IDX)
    note_idx = random.choice(NOTE_IDX)
    # which octave * size of octave  + note in that octave
    abs_note = octave_idx * NUM_DIATONIC_REST + note_idx
    duration = DEFAULT_DURATION
    return (note_idx, octave_idx, abs_note, duration)

# Sel signifies P or S selection where P is parent and S is survivor
def Truncation(population, Sel):
    new= population.sort(key=lambda x: x.fitness, reverse=True)#Descending order
    if (Sel == "P"):  # parent selection
        Parents = new[:2]

        return Parents
    elif (Sel == "S"):
        Top_fit = new[:POP_SIZE]
        return Top_fit
    else:
        print("Selection is not identified")


def Crossover(parent1, parent2):
    crossover_idx = random.randrange(0, len(parent1))

    first_child = parent1[0:crossover_idx] + parent2[crossover_idx:]
    second_child = parent2[0:crossover_idx] + parent1[crossover_idx:]

    Offsprings=(first_child,second_child)
    return Offsprings


def Mutate(population, rate):
    for i in range(0, len(population)):
        for j in range(0,len(population[i])):#length of chromo,each bar
            myRandom = round(random.uniform(0, 1), 2)  # rounded off to 2 dp
            if (myRandom < rate):
                population[i][j]=gen_chromosone()     
    return population


def Evolve():
    pass


def main():
    myMelodies = Initialise_Population(POP_SIZE)
    print(myMelodies)
    
    
    
main()
