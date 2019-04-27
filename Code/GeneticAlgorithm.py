# Genetic Algorithm for Music Composition

from chromosome import chromosome
from constants import *
import random

#Take user inputs to allow controlling parameters 
ITER=int(input("Enter the number of iterations: "))
POP_SIZE=int(input("Enter population size: "))
MUTATION_RATE=float(input("Enter mutation rate between 0 and 1: "))

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
Survivor Selection: Truncation
'''

def Truncation(population,Sel):#Sel signifies P or S selection where P is parent and S is survivor
    if (Sel=="P"):#parent selection
        Parents=[]


        return Parents
    elif (Sel=="S"):
        Top_fit=[]

        return Top_fit
    else:
        print("Selection is not identified")


def Crossover(parent1,parent2):
    pass


def Mutate(population,rate):
    for i in range(0, len(population)):
        myRandom=round(random.uniform(0,1), 2)#rounded off to 2 dp
        if (myRandom<rate):
            pass

    return population

def Evolve():
    pass


def main():
    myMelodies=Initialise_Population(POP_SIZE)
    







main()