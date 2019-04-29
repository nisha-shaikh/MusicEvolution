# Chromosone

from constants import OCTAVE_IDX, NOTE_IDX, NUM_DIATONIC_REST, DEFAULT_DURATION, BEATS_PER_SECTION
import random
import collections


class chromosome:

    def __init__(self):
        '''Create a chromosone i.e melody'''
        self.melody = []

        for _ in range(BEATS_PER_SECTION):
            octave_idx = random.choice(OCTAVE_IDX)
            note_idx = random.choice(NOTE_IDX)

            # which octave * size of octave  + note in that octave
            abs_note = octave_idx * NUM_DIATONIC_REST + note_idx
            duration = DEFAULT_DURATION

            self.melody.append((note_idx, octave_idx, abs_note, duration))

        self.chromoLength = len(self.melody)
        self.fitness = self.fitnessScore()
        #self.fitness=random.randint(0,50)#for testing purpose as errors were generated

    def __repr__(self):
        #Representation of the chromosone structure
        return (str(self.melody))
    
    def genMusic(self):
        '''Uses pysynth to play the music'''
        pass

    def fitnessScore(self):
        '''Based on some characteristics of music, fitness score of the entire melody is evaluated
        Higher fitness values denote better individuals'''
        fitness = 0
        fitness += self.fitnessByOctave()
        fitness += self.fitnessByInterval()
        return fitness

    def fitnessByOctave(self):
        '''Finds the fitness of the chromosome based on octave
        Tunes with many notes in the same octave are more desirable'''
        fitness = 0
        octaves = []
        for i in range(self.chromoLength):
            octaves.append(self.melody[i][1])
        commonOctaves = collections.Counter(octaves)
        mostCommonOctave = commonOctaves.most_common(1)
        # frequency of the most repeated octave is the fitness value
        fitness += mostCommonOctave[0][1]
        return fitness

    def fitnessByInterval(self):
        '''Finds the fitness of chromosome based on intervals
        Higher fitness for tunes that have more jumps within the perfect fourth'''
        fitness = 0
        abs_note_idx = 2
        for i in range(self.chromoLength-1):
            # interval is calculated for every successive note (which is stored as abs_note in self.melody)
            interval = abs(self.melody[i][abs_note_idx] - self.melody[i+1][abs_note_idx])
            if interval <= 4:
                fitness += 1
        return fitness
