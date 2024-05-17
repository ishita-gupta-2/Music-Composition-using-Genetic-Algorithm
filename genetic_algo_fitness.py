import random

# Function to generate initial population for genetic algorithm
def generate_initial_population(number_of_notes, num_chromosomes, scale, range_, user_motif):
    population = []
    for _ in range(num_chromosomes):
        chromosome = []
        for _ in range(number_of_notes):
            # Randomly initialize each tuple in the chromosome
            note_index = random.randint(0, len(scale) - 1)
            octave_index = random.randint(0, len(range_) - 1)
            binary_bit = user_motif
            chord_index = random.randint(0, 3)
            chromosome.append((note_index, octave_index, binary_bit, chord_index))
        population.append(chromosome)
    return population

# Function to calculate Octave Note Fitness (ON)
def octave_note_fitness(chromosome):
    octave_counts = {}
    for note_tuple in chromosome:
        octave_index = note_tuple[1]  # Octave index is the second element in the tuple
        if octave_index in octave_counts:
            octave_counts[octave_index] += 1
        else:
            octave_counts[octave_index] = 1
    return max(octave_counts.values(), default=1)

# Function to calculate Triad Fitness (TF)
def triad_fitness(chromosome, scale):
    tf = 2
    for i in range(len(chromosome) - 2):
        abi = abs(chromosome[i][1] * len(scale) + chromosome[i][0])  # Absolute value of note index
        abi_plus_1 = abs(chromosome[i + 1][1] * len(scale) + chromosome[i + 1][0])
        abi_plus_2 = abs(chromosome[i + 2][1] * len(scale) + chromosome[i + 2][0])
        if (abi < abi_plus_1 < abi_plus_2) or (abi > abi_plus_1 > abi_plus_2):
            tf += 1
    return tf

# Function to calculate No Jump Fitness (NJ)
def no_jump_fitness(chromosome, scale):
    nj = 1
    for i in range(len(chromosome) - 1):
        abi = abs(chromosome[i][1] * len(scale) + chromosome[i][0])  # Absolute value of note index
        abi_plus_1 = abs(chromosome[i + 1][1] * len(scale) + chromosome[i + 1][0])
        abii = abs(abi - abi_plus_1)
        if abii < 4:  # Considering perfect fourth interval
            nj += 1
    return nj

# Function to calculate Repeat Note Fitness (RN)
def repeat_note_fitness(chromosome):
    max_consecutive_repeats = 0
    consecutive_repeats = 0
    for i in range(len(chromosome) - 1):
        if chromosome[i][0] == chromosome[i+1][0]:
            consecutive_repeats += 1
            max_consecutive_repeats = max(max_consecutive_repeats, consecutive_repeats)
        else:
            consecutive_repeats = 1
    return max_consecutive_repeats

# Function to calculate Harmony Fitness (HF)
def harmony_fitness(chromosome):
    chord_indices = [0, 0, 1, 1, 2, 2, 3, 3]  # Chord indices mapped to note indices
    hf = 0
    for note_tuple in chromosome:
        note_index = note_tuple[0]
        mapped_chord_index = chord_indices[note_index]
        if note_tuple[3] == mapped_chord_index:
            hf += 1
    return hf

# Function to calculate Chord Progression (CP)
def chord_progression_fitness(chromosome):
    cp = 0
    for i in range(len(chromosome) - 1):
        if abs(chromosome[i][3] - chromosome[i+1][3]) <= 1:
            cp += 1
    return cp

# Function to calculate overall fitness using given weights
def calculate_overall_fitness(chromosome, scale, weights):
    on_fitness = octave_note_fitness(chromosome)
    tf_fitness = triad_fitness(chromosome, scale)
    nj_fitness = no_jump_fitness(chromosome, scale)
    rn_fitness = repeat_note_fitness(chromosome)
    hf_fitness = harmony_fitness(chromosome)
    cp_fitness = chord_progression_fitness(chromosome)

    overall_fitness = ((weights[0] * on_fitness) + (weights[1] * tf_fitness) + (weights[2] * nj_fitness)
                     + (weights[3] * rn_fitness) + (weights[4] * hf_fitness) + (weights[5] * cp_fitness))
    return overall_fitness