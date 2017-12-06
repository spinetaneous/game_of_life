"""
game_of_life.py

this isn't gonna be pretty because i'm only writing this so that
i can trasnlate to assembly later xd
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
            
            #lol this part makes me so sad
            # these are 0 if we can't check, 1 if we can
            top_ok = 0
            left_ok = 0
            right_ok = 0
            bottom_ok = 0
            
            if i != 0: top_ok = 1
            if i != (rows - 1): bottom_ok = 1
            if j != 0: left_ok = 1
            if j != (cols - 1): right_ok = 1
            
            # check top 
            # alive += _check_top(gen1, i, j, cols, rows)
            if top_ok:
                if gen[(i-1) * cols  + j]: alive += 1 # cell directly above
            
            # check left
            if left_ok:
                if gen[i * cols + (j - 1)]: alive += 1 # cell directly to left
            
            # check right
            if right_ok:
                if gen[i * cols + (j + 1)]: alive += 1 # cell directly to right
                
            # check bottom
            if top_ok:
                if gen[(i + 1) * cols  + j]: alive += 1 # cell directly below
                
                
                
            # determine if cell should be alive or dead
            if gen1[i * cols + j]: # cell is alive   
                pass
            else: # cell is dead
                if alive == 3: # with 3 neighbors... 
                    gen2[i * cols + j] = 1 # ...cell comes to life
            pass
    return gen2
            
def _check_top(gen, i, j, cols, rows):
    """ checks the 3 spots on top of cell gen[i][j]/gen[i * cols + j] and returns # of alive cells"""
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