# Chromosone

from constants import OCTAVE_IDX, NOTE_IDX, NUM_DIATONIC_REST, DEFAULT_DURATION, BEATS_PER_SECTION, DIATONIC_REST, OCTAVES
import random
import collections
import pysynth_b


class chromosome:

    def __init__(self, newMelody):  # R for random, else new melody
        '''Create a chromosone i.e. melody'''

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
        # self.fitness=random.randint(0,50)#for testing purpose as errors were generated

    def __repr__(self):
        # Representation of the chromosone structure
        return (str(self.melody))

    def gen_note(self):
        octave_idx = random.choice(OCTAVE_IDX)
        note_idx = random.choice(NOTE_IDX)
        abs_note = octave_idx * NUM_DIATONIC_REST + note_idx
        duration = DEFAULT_DURATION

        return (note_idx, octave_idx, abs_note, duration)

    def crossover(self, chromo1):
        #print("Crossover is working")

        crossover_idx = random.randrange(0, self.chromoLength)

        first_child = self.melody[0:crossover_idx] + \
            chromo1.melody[crossover_idx:]
        second_child = chromo1.melody[0:crossover_idx] + \
            self.melody[crossover_idx:]

        offsprings = (first_child, second_child)

        return offsprings

    def mutate(self, rate):
        #print("Mutate in chromo is working")
        for j in range(0, self.chromoLength):  # all beats in the melody
            myRandom = round(random.uniform(0, 1), 2)  # rounded off to 2 dp
            if (myRandom < rate):
                self.melody[j] = self.gen_note()
        self.fitness = self.fitnessScore()

    def fitnessScore(self):
        '''Based on some characteristics of music, fitness score of the entire melody is evaluated
        Higher fitness values denote better individuals'''
        fitness = 0
        fitness += 3*self.fitnessByOctave()
        fitness += 2*self.fitnessByInterval()
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
            interval = abs(self.melody[i][abs_note_idx] -
                           self.melody[i+1][abs_note_idx])
            if interval <= 4:
                fitness += 1
        return fitness

    def genMusic(self, filename):
        '''Uses pysynth to play the music'''
        tune = self.chromoToTune()
        # newTune = self.joinSameNotes(tune)
        pysynth_b.make_wav(tune, fn='{}.wav'.format(
            filename), leg_stac=0.7, bpm=180)
        # pysynth_b.make_wav(newTune, fn='{}.wav'.format(filename), leg_stac=0.7, bpm=180)
        # if filename == 'Final':
        #     pysynth_b.make_wav(tune, fn='{}_orig.wav'.format(
        #         filename), leg_stac=0.7, bpm=180)

    def chromoToTune(self):
        '''Converts chromosome in a better representaiton of music that PySynth can recognize'''
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

    # def joinSameNotes(self, origTune):
    #     '''Joins successive same notes'''
    #     newTune = []
    #     skip = False
    #     for i in range(0, len(origTune) - 1):
    #         if skip:
    #             skip = False
    #             continue
    #         c_note = origTune[i][0]
    #         n_note = origTune[i+1][0]
    #         c_duration = origTune[i][1]
    #         if c_note == n_note:
    #             dur = 2 if c_duration > 2 else 1
    #             newTune.append((c_note, dur))
    #             skip = True
    #         else:
    #             newTune.append((c_note,c_duration))

    #     return tuple(newTune)
