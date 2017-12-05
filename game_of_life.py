"""
game_of_life.py
"""

gen1 = [0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 0, 0, 0, 0,
     0, 0, 0, 1, 0, 0, 0,
     0, 1, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0]

def make_gen(gen1, rows, cols):
    """
    makes a new generation
    this function assumes that the cells outside the border (off the grid)
    are dead i.e. 0s
    
    @param gen1: original generation
    @param gen2: the grid to be altered and will contain the new generation
    @param rows: number of rows
    @param cols: number of cols
    @return gen2: array of new generation
    """
    gen2 = [0 for x in range(len(gen1))]
    
    for i in range(rows):
        for j in range(cols):
            alive = 0 # keeps track of how many surrounding cells are alive
            # check top
            
            # check left
            
            # check right
            
            # check bottom
            
            # determine if cell should be alive or dead
            if gen1[i * cols + j]: # cell is alive   
                pass
            else: # cell is dead
                if alive == 3: # with 3 neighbors... 
                    gen2[i * cols + j] = 1 # ...cell comes to life
            pass
    return gen2
            
def _check_top(gen, row, col):
    """ checks the 3 spots on top of cell gen[row][col]/gen[i * cols + j] and returns # of alive cells"""
    alive = 0
    if gen[(i-1) * cols  + (j - 1)]: alive += 1 # upper left cell
    if gen[(i-1) * cols  + j]: alive += 1       # cell directly above
    if gen[(i-1) * cols  + (j + 1)]: alive += 1 # upper right cell
    return alive
        
def print_gen(gen, rows, cols):
    """
    prints a new generation
    """
    for i in range(rows):
        for j in range(cols):
            print(gen[i * cols + j]),
        print
    return
        
print_gen(gen1, 6, 7)
print
print_gen(make_gen(gen1, 6, 7), 6, 7)