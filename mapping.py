#function for mapping
def map_chromosome_to_notes_duration(chromosome, binary_sequence, note_duration_single):
    notes = []  # List to store note durations
    first_pointer = None  # Pointer for the first occurrence of 1
    second_pointer = None  # Pointer for the second occurrence of 1
    
    # Find the first occurrence of 1 in the binary sequence
    first_pointer = binary_sequence.index(1)
    
    # Find the next occurrence of 1 after the first_pointer
    try:
        second_pointer = binary_sequence.index(1, first_pointer + 1)
    except ValueError:
        # If no more occurrences of 1 are found, return an empty list
        return []
    
    # Loop until there are no more occurrences of 1 after second_pointer
    while second_pointer is not None:
        # Calculate the duration between consecutive 1s
        duration = (second_pointer - first_pointer) * note_duration_single
        # Append the duration to the notes list
        notes.append(duration)
        # Move the first_pointer to the position of the second_pointer
        first_pointer = second_pointer
        # Find the next occurrence of 1 after the second_pointer
        try:
            second_pointer = binary_sequence.index(1, first_pointer + 1)
        except ValueError:
            # If no more occurrences of 1 are found, set second_pointer to None
            second_pointer = None
    
    # If the loop ends and there's one more note after the last occurrence of 1
    if second_pointer == None:
        duration = (len(binary_sequence) - first_pointer) * note_duration_single
        notes.append(duration)
    
    return notes

def convert_chromosome_to_note_number(chromosome, note_duration):
    # Define the mapping between chromosome values and note numbers
    note_mapping = {
        (0, 0, 0, 0): 60, (0, 0, 0, 1): 61, (0, 0, 0, 2): 67, (0, 0, 0, 3): 63,
        (0, 1, 0, 0): 72, (0, 1, 0, 1): 73, (0, 1, 0, 2): 79, (0, 1, 0, 3): 75,
        (0, 2, 0, 0): 84, (0, 2, 0, 1): 85, (0, 2, 0, 2): 91, (0, 2, 0, 3): 87,
        (1, 0, 0, 0): 62, (1, 0, 0, 1): 63, (1, 0, 0, 2): 65, (1, 0, 0, 3): 65,
        (1, 1, 0, 0): 74, (1, 1, 0, 1): 75, (1, 1, 0, 2): 77, (1, 1, 0, 3): 77,
        (1, 2, 0, 0): 86, (1, 2, 0, 1): 87, (1, 2, 0, 2): 89, (1, 2, 0, 3): 89,
        (2, 0, 0, 0): 64, (2, 0, 0, 1): 68, (2, 0, 0, 2): 67, (2, 0, 0, 3): 67,
        (2, 1, 0, 0): 76, (2, 1, 0, 1): 80, (2, 1, 0, 2): 79, (2, 1, 0, 3): 79,
        (2, 2, 0, 0): 88, (2, 2, 0, 1): 92, (2, 2, 0, 2): 91, (2, 2, 0, 3): 91,
        (3, 0, 0, 0): 65, (3, 0, 0, 1): 66, (3, 0, 0, 2): 64, (3, 0, 0, 3): 64,
        (3, 1, 0, 0): 77, (3, 1, 0, 1): 78, (3, 1, 0, 2): 76, (3, 1, 0, 3): 76,
        (3, 2, 0, 0): 89, (3, 2, 0, 1): 90, (3, 2, 0, 2): 88, (3, 2, 0, 3): 88,
        (4, 0, 0, 0): 67, (4, 0, 0, 1): 68, (4, 0, 0, 2): 66, (4, 0, 0, 3): 66,
        (4, 1, 0, 0): 79, (4, 1, 0, 1): 80, (4, 1, 0, 2): 78, (4, 1, 0, 3): 78,
        (4, 2, 0, 0): 91, (4, 2, 0, 1): 92, (4, 2, 0, 2): 90, (4, 2, 0, 3): 90,
        (5, 0, 0, 0): 69, (5, 0, 0, 1): 70, (5, 0, 0, 2): 64, (5, 0, 0, 3): 64,
        (5, 1, 0, 0): 81, (5, 1, 0, 1): 82, (5, 1, 0, 2): 76, (5, 1, 0, 3): 76,
        (5, 2, 0, 0): 93, (5, 2, 0, 1): 94, (5, 2, 0, 2): 88, (5, 2, 0, 3): 88,
        (6, 0, 0, 0): 71, (6, 0, 0, 1): 67, (6, 0, 0, 2): 66, (6, 0, 0, 3): 66,
        (6, 1, 0, 0): 83, (6, 1, 0, 1): 79, (6, 1, 0, 2): 78, (6, 1, 0, 3): 78,
        (6, 2, 0, 0): 95, (6, 2, 0, 1): 91, (6, 2, 0, 2): 90, (6, 2, 0, 3): 90,
    }

    # Initialize an empty list to store the notes
    notes = []

    # Iterate through the chromosome and convert to note number and duration
    for gene in chromosome:
        note_number = note_mapping[gene]
        notes.append(note_number)

    return notes