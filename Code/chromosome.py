# Chromosone

from constants import OCTAVE_IDX, NOTE_IDX, NUM_DIATONIC_REST, DEFAULT_DURATION
import random


class chromosome:

    def __init__(self):
        '''Create a chromosone i.e melody'''
        self.octave_idx = random.choice(OCTAVE_IDX)
        self.note_idx = random.choice(NOTE_IDX)

        # which octave * size of octave  + note in that octave
        self.abs_note = self.octave_idx * NUM_DIATONIC_REST + self.note_idx
        self.duration = DEFAULT_DURATION

    def __repr__(self):
        '''Representation of the chromosone structure'''
        return ([self.note_idx, self.octave_idx, self.abs_note, self.duration])
