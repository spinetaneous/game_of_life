"""
game_of_life.py
"""

gen1 = [0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 0, 0, 0, 0,
     0, 0, 0, 1, 0, 0, 0,
     0, 1, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0]
    
gen2 = [0 for x in range(len(gen1))]

def make_gen(gen1, rows, cols):
    """
    makes a new generation
    """

def print_gen(gen, rows, cols):
    """
    prints a new generation
    """
    for i in range(rows):
        for j in range(cols):
            print(gen[i * cols + j]),
        print

print_gen(gen1, 6, 7)
print
print_gen(gen2, 6, 7)