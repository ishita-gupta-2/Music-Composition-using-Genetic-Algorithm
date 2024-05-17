import random

def calculate_melodic_interval(parent1, parent2):
    melodic_intervals = []
    for i in range(len(parent1)):
        Ab1_k = abs(parent1[i][1] * 8 + parent1[i][0])
        Ab2_k_plus_1 = abs(parent2[(i + 1) % len(parent2)][1] * 8 + parent2[(i + 1) % len(parent2)][0])
        Ab2_k = abs(parent2[i][1] * 8 + parent2[i][0])
        Ab1_k_plus_1 = abs(parent1[(i + 1) % len(parent1)][1] * 8 + parent1[(i + 1) % len(parent1)][0])
        melodic_interval = max(abs(Ab1_k - Ab2_k_plus_1), abs(Ab2_k - Ab1_k_plus_1))
        melodic_intervals.append(melodic_interval)
    return melodic_intervals

def crossover(parent1, parent2):
    melodic_intervals = calculate_melodic_interval(parent1, parent2)
    min_interval_index = melodic_intervals.index(min(melodic_intervals))
    child1 = parent1[:min_interval_index] + parent2[min_interval_index:]
    child2 = parent2[:min_interval_index] + parent1[min_interval_index:]
    return child1, child2, melodic_intervals[min_interval_index], melodic_intervals

#function for mutation
def note_based_mutation(chromosome):
    mutated_chromosome = chromosome[:]  # Make a copy of the chromosome
    
    for i in range(len(mutated_chromosome)):
        # Get the current note tuple
        current_note = mutated_chromosome[i]
        current_note_number = current_note[0]  # Calculate the note number
        
        # Check the neighboring notes if their difference is greater than 4
        if i > 0:
            # Calculate the note number of the previous note
            previous_note = mutated_chromosome[i - 1]
            previous_note_number = previous_note[0]
            if abs(current_note_number - previous_note_number) > 4:
                # If the difference is greater than 4, replace the note with a new note
                new_note_index = random.randint(max(0, previous_note_number - 4), min(7, previous_note_number + 4))
                mutated_chromosome[i] = (new_note_index, current_note[1], current_note[2], current_note[3])

        if i < len(mutated_chromosome) - 1:
            # Calculate the note number of the next note
            next_note = mutated_chromosome[i + 1]
            next_note_number = next_note[0]
            if abs(current_note_number - next_note_number) > 4:
                # If the difference is greater than 4, replace the note with a new note
                new_note_index = random.randint(max(0, next_note_number - 4), min(7, next_note_number + 4))
                mutated_chromosome[i] = (new_note_index, current_note[1], current_note[2], current_note[3])
    
    return mutated_chromosome