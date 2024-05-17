import random
from bresenhams_line_algo import calculate_beat_parameters, bresenhams_line_algorithm
from genetic_algo_fitness import generate_initial_population, octave_note_fitness, triad_fitness, no_jump_fitness, repeat_note_fitness, harmony_fitness, chord_progression_fitness, calculate_overall_fitness
from selection import roulette_wheel_selection
from crossover_and_mutation import calculate_melodic_interval, crossover, note_based_mutation
from mapping import map_chromosome_to_notes_duration, convert_chromosome_to_note_number
from midi_generation import notes_to_midi

def main():
    # Parameters
    time_signature = '1/4'
    scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    range_ = list(range(3, 5))  # Octaves
    num_chromosomes = 50
    user_motif = 0
    weights = [1, 1, 1, -1, 1, 1]

    # Step 1: Calculate beat parameters
    total_beats, note_duration = calculate_beat_parameters(time_signature)

    # Step 2: Initialize endpoints for Bresenham's algorithm
    x1, y1 = 0, 0
    x2 = total_beats
    y2 = random.randint(0, total_beats)  # Randomize y2 within the range of total beats
    
    # Step 3: Perform Bresenham's line algorithm
    binary_sequence, number_of_notes = bresenhams_line_algorithm(x1, y1, x2, y2)

    # Step 4: Initialize population for genetic algorithm
    population = generate_initial_population(number_of_notes, num_chromosomes, scale, range_, user_motif)

    # Step 5: Calculate fitness of each chromosome in the population
    fitness_values = []
    for chromosome in population:
        fitness = calculate_overall_fitness(chromosome, scale, weights)
        fitness_values.append(fitness)
    
    # Step 6: Perform roulette wheel selection to select top 2 parents
    selected_parents, selected_parents_fitness = roulette_wheel_selection(population, fitness_values)

    # Step 7: Apply crossover and mutation to both the childs obtained
    child1, child2, melodic_interval, melodic_intervals_array = crossover(selected_parents[0], selected_parents[1])
    mutated_child1 = note_based_mutation(child1)
    mutated_child2 = note_based_mutation(child2)

    mutated_child1_iterated = mutated_child1
    mutated_child2_iterated = mutated_child2

    #iteration
    for _ in range(6):
        child1_iterated, child2_iterated, melodic_interval, melodic_intervals_array = crossover(mutated_child1_iterated, mutated_child2_iterated)
        mutated_child1_iterated = note_based_mutation(child1_iterated)
        mutated_child2_iterated = note_based_mutation(child2_iterated)

    mutated_child1 = mutated_child1_iterated
    mutated_child2 = mutated_child2_iterated

    # Step 8: Mapping to convert chromosomes into (note_number, note_duration) format
    note_duration_mapped1 = map_chromosome_to_notes_duration(mutated_child1, binary_sequence, note_duration)
    note_number_mapped1 = convert_chromosome_to_note_number(mutated_child1, note_duration)
    notes_array1 = list(zip(note_number_mapped1, note_duration_mapped1))
    note_duration_mapped2 = map_chromosome_to_notes_duration(mutated_child2, binary_sequence, note_duration)
    note_number_mapped2 = convert_chromosome_to_note_number(mutated_child2, note_duration)
    notes_array2 = list(zip(note_number_mapped2, note_duration_mapped2))
    final_array = notes_array1 + notes_array1 
    final_array += notes_array2
    final_array += notes_array1

    # Step 9: Midi generation
    notes_to_midi(final_array, 'Final/output.mid')

    print("Binary Sequence: ", binary_sequence)
    print("Number of notes: ", number_of_notes)
    print("Note duration: ", note_duration)
    print("Initial Population:", population)
    print("Fitness values:", fitness_values)
    print("Selected Parents:", selected_parents)
    print("Fitness values of selected parents:", selected_parents_fitness)
    print("Crossover Point:", melodic_interval)
    print("Melodic Interval Array:", melodic_intervals_array)
    print("Parent 1 before crossover:", selected_parents[0])
    print("Parent 2 before crossover:", selected_parents[1])
    print("Child 1 after crossover:", child1)
    print("Child 2 after crossover:", child2)
    print("Child 1 after mutation:", mutated_child1)
    print("Child 2 after mutation:", mutated_child2)
    print("Final Notes Array:", final_array)

if __name__ == "__main__":
    main()