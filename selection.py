def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    normalized_probabilities = [fitness / total_fitness for fitness in fitness_values]
    
    # Sort the normalized probabilities and zip them with the population
    sorted_probabilities_and_population = sorted(zip(normalized_probabilities, population, fitness_values), reverse=True)
    
    # Select the top 2 parents
    selected_parents = [chromosome for probability, chromosome, fitness in sorted_probabilities_and_population[:2]]
    selected_fitness_values = [fitness for probability, chromosome, fitness in sorted_probabilities_and_population[:2]]

    return selected_parents, selected_fitness_values