import random
import math

# Function to calculate beat parameters based on time signature
def calculate_beat_parameters(time_signature):
    top_number, bottom_number = map(int, time_signature.split('/'))
    Bt = top_number  # Beats per bar
    V = bottom_number  # Beat value
    B = 8  # Number of bars
    
    # Calculate beat duration and total number of beats
    min_val = math.log2(2/V)
    max_val = math.log2(16/V)
    n = random.randint(math.ceil(min_val), math.floor(max_val))
    print("n:", n)

    note_duration = 1 / ((2 ** n) * V)
    print("Note duration: ", 1/note_duration)
    total_beats = (2 ** n) * (B * Bt)
    
    return total_beats, note_duration

# Function to generate binary sequence using Bresenham's line algorithm
def bresenhams_line_algorithm(x1, y1, x2, y2):
    number_of_notes = 0
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * (dy - dx)
    binary_sequence = []

    while x < x2:
        if d < 0:
            d += 2 * dy
            binary_sequence.append(0)
        else:
            d += 2 * (dy - dx)
            y += 1
            binary_sequence.append(1)
            number_of_notes += 1
        x += 1

    return binary_sequence, number_of_notes