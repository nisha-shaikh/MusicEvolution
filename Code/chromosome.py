# Chromosone

from constants import OCTAVE_IDX, NOTE_IDX, NUM_DIATONIC_REST, DEFAULT_DURATION, BEATS_PER_SECTION
import random


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

            self.melody.append((octave_idx, note_idx, abs_note, duration))

        self.fitness=calculateFitness()
            
    def __repr__(self):
        '''Representation of the chromosone structure'''
        return (self.melody)

    def genMusic(self):
        '''Uses pysynth to play the music'''
        pass


    def calculateFitness(self):
        '''Finds the fitness of the chromosome based on some music qualities'''
        self.fitness=20

        
        
