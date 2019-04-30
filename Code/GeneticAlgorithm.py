# Genetic Algorithm for Music Composition

from chromosome import chromosome
from constants import *
import random

# Take user inputs to allow controlling parameters--TESTING PURPOSE ONLY. 
# The fixed parameters in constants.py
'''
ITER = int(input("Enter the number of iterations: "))
POP_SIZE = int(input("Enter population size: "))
MUTATION_RATE = float(input("Enter mutation rate between 0 and 1: "))
GENERATIONS = int(input("Enter number of generations: "))
'''

def Initialise_Population(pop_size):
    '''Initializes chromosones to construct the initial population'''
    pop = []
    for i in range(pop_size):
        new=chromosome("R")
        pop.append(new)
    return pop

'''
SELECTION SCHEME
As a learning outcome from Assignment 01,
we have concluded that Eliticism works best hence, the selected selection scheme for this algorithm is,
Parent Selection : Truncation
Survivor Selection: Truncation
'''


# Sel signifies P or S selection where P is parent and S is survivor
def Truncation(population, Sel):
    #print("Truncation is working")
    
    new= sorted(population, key=lambda x: x.fitness, reverse=True)#Descending order
    if (Sel == "P"):  # parent selection
        Parents = new[:2]
        return Parents
    elif (Sel == "S"):
        Top_fit = new[:POP_SIZE]
        return Top_fit
    else:
        print("Selection is not identified")    
    

def Mutate(population, rate):
    for i in range(0, len(population)):
        population[i].mutate(rate)
    #print("Mutation is working")
    return population


def Evolve(population):
    for gen in range (0,GENERATIONS):
        #print("Generation", gen)

        if (gen%20==0):
            #To record the best melody after every 10 gen
            new= sorted(population, key=lambda x: x.fitness, reverse=True)
            best_melody=new[0]
            best_melody.genMusic("gen")
       
        
        parents=Truncation(population,"P")
        
        offsprings=parents[0].Crossover(parents[1])        

        population.append(chromosome(offsprings[0]))
        population.append(chromosome(offsprings[1]))
        
        #print(population[0].chromoLength)
        
        newpop=Mutate(population,MUTATION_RATE)
        next_gen=Truncation(newpop,"S")
        population=next_gen
    return population


def main():
    myMelodies = Initialise_Population(POP_SIZE)   
    for iterations in range (0,ITER):
        myMelodies=Evolve(myMelodies)
        print("Iteration",iterations,"\nPopulation",myMelodies)
    #print(len(myMelodies))
    new= sorted(myMelodies, key=lambda x: x.fitness, reverse=True)
    best_melody=new[0]
    best_melody.genMusic("Final")
    
    
main()
