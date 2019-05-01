from constants import *
import random
import collections
import pysynth_b


class chromosome:

    def __init__(self, newMelody):  # R for random, else new melody
        '''
        Create a chromosone i.e. melody
        '''

        self.melody = []

        if (newMelody == "R"):
            for _ in range(BEATS_PER_SECTION):
                octave_idx = random.choice(OCTAVE_IDX)
                note_idx = random.choice(NOTE_IDX)

                # which octave (from C2 to C7) * amount of notes per octave + note in that octave
                abs_note = octave_idx * NUM_DIATONIC_REST + note_idx
                duration = DEFAULT_DURATION

                self.melody.append((note_idx, octave_idx, abs_note, duration))
        else:
            self.melody = newMelody

        self.chromoLength = len(self.melody)
        self.fitness = self.fitnessScore()

    def __repr__(self):
        '''
        Representation of the chromosone structure
        '''
        return (str(self.melody))

    def gen_note(self):
        octave_idx = random.choice(OCTAVE_IDX)
        note_idx = random.choice(NOTE_IDX)
        abs_note = octave_idx * NUM_DIATONIC_REST + note_idx
        duration = DEFAULT_DURATION

        return (note_idx, octave_idx, abs_note, duration)

    def fitnessScore(self):
        '''
        Based on some characteristics of music, fitness score of the entire melody is evaluated
        Higher fitness values denote better individuals
        '''
        fitness = 0
        fitness += 3*self.fitnessByOctave()
        fitness += 2*self.fitnessByInterval()
        fitness += 2*self.fitnessByVariation()
        fitness += self.fitnessByDownBeat()
        # fitness += self.fitnessByBackbeat()
        return fitness

    def fitnessByOctave(self):
        '''
        Finds the fitness of the chromosome based on octave
        Tunes with many notes in the same octave are more desirable
        '''
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
        '''
        Finds the fitness of chromosome based on intervals
        Higher fitness for tunes that have more intervals within the perfect fourth
        '''
        fitness = 0
        abs_note_idx = 2
        for i in range(self.chromoLength-1):
            # interval is calculated for every successive note
            interval = abs(self.melody[i][abs_note_idx] -
                           self.melody[i+1][abs_note_idx])
            if interval <= 4:
                fitness += 1
        return fitness

    def fitnessByVariation(self):
        '''
        Higher fitness if three successive notes all rise or all fall to give a sense of continuity
        '''
        fitness = 0
        for i in range(self.chromoLength - 2):
            succNotes = self.melody[i:i+3]
            inc = all(x <= y for x, y in zip(succNotes, succNotes[1:]))
            dec = all(x >= y for x, y in zip(succNotes, succNotes[1:]))
            if inc or dec:
                fitness += 1
        return fitness

    def fitnessByDownBeat(self):
        '''
        Higher fitness if more bars start with the C major triad notes (C, E, or G)
        '''
        fitness = 0
        for i in range(0, BEATS_PER_SECTION, BARS_PER_SECTION):
            note_idx = self.melody[i][0]
            note = DIATONIC_REST[note_idx]
            if note in CHORD_NOTES:
                fitness += BEATS_PER_BAR
        return fitness

    def fitnessByBackbeat(self):
        '''
        Higher fitness if the second and fourth notes are siginificant (C, E or G)
        '''
        fitness = 0
        for i in range(1, BEATS_PER_SECTION, 2):
            note_idx = self.melody[i][0]
            note = DIATONIC_REST[note_idx]
            if note in CHORD_NOTES:
                fitness += BEATS_PER_BAR
        return fitness

    def crossover(self, chromo1):
        crossover_idx = random.randrange(0, self.chromoLength)

        first_child = self.melody[0:crossover_idx] + \
            chromo1.melody[crossover_idx:]
        second_child = chromo1.melody[0:crossover_idx] + \
            self.melody[crossover_idx:]

        offsprings = (first_child, second_child)

        return offsprings

    def mutate(self, rate):
        for j in range(0, self.chromoLength):  # all beats in the melody
            myRandom = round(random.uniform(0, 1), 2)  # rounded off to 2 dp
            if (myRandom < rate):
                self.melody[j] = self.gen_note()
        self.fitness = self.fitnessScore()

    def genMusic(self, filename):
        '''
        Uses pysynth to play the music
        '''
        tune = self.chromoToTune()
        pysynth_b.make_wav(tune, fn='{}.wav'.format(
            filename), leg_stac=0.7, bpm=180)

    def chromoToTune(self):
        '''
        Converts chromosome in a better representaiton of music that PySynth can recognize
        '''
        convertedTune = []
        for i in range(self.chromoLength):
            # gives the note ('cdefgabr') referenced by note_idx
            letter = DIATONIC_REST[self.melody[i][0]]
            # gives the octave of the note referenced by octave_idx
            octave = OCTAVES[self.melody[i][1]]
            if letter == 'r':
                octave = ''
            # PySynth reads note and its octave together
            note = str(letter) + str(octave)
            duration = self.melody[i][3]
            # PySynth makes music by reading a tuple of note and its durationa
            convertedTune.append((note, duration))
        return tuple(convertedTune)
