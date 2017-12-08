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
            
            # alive += _check_top(gen1, i, j, cols, rows)
            if top_ok and left_ok:
                if gen1[(i - 1) * cols + (j - 1)]: alive += 1 # upper left cell
                
            if top_ok:
                if gen1[(i - 1) * cols  + j]: alive += 1 # cell directly above
                
            if top_ok and right_ok:
                if gen1[(i - 1) * cols + (j + 1)]: alive += 1 # upper right cell
            
            if left_ok:
                if gen1[i * cols + (j - 1)]: alive += 1 # cell directly to left
            
            if right_ok:
                if gen1[i * cols + (j + 1)]: alive += 1 # cell directly to right
                
            if bottom_ok and left_ok:
                if gen1[(i + 1) * cols + (j - 1)]: alive += 1 # lower left cell
                
            if bottom_ok:
                if gen1[(i + 1) * cols  + j]: alive += 1 # cell directly below

            if bottom_ok and right_ok:
                if gen1[(i + 1) * cols + (j + 1)]: alive += 1 # lower right cell
                
            # determine if cell should be alive or dead
            if gen1[i * cols + j]: # cell is alive   
                if alive == 2 or alive == 3:
                    gen2[i * cols + j] = 1 # stasis
                else: # this isn't necessary here but it will be for cusp
                    gen2[i * cols + j] = 0 # under/overpopulation
            else: # cell is dead
                if alive == 3:
                    gen2[i * cols + j] = 1 # repopulation
            pass
    return gen2
            
        
def print_gen(gen, rows, cols):
    """ prints a new generation  """
    for i in range(rows):
        for j in range(cols):
            print(gen[i * cols + j]),
        print
    return
        
def print_num_gens(gen1, rows, cols, num_gens):
    """ prints out a number of generations """
    curr_gen = 0
    prev_gen = gen1
    print("Generation: {}".format(curr_gen))
    curr_gen += 1
    print_gen(gen1, rows, cols)
    print
    for gen in range(num_gens-1):
        new_gen = make_gen(prev_gen, rows, cols)
        
        print("Generation: {}".format(curr_gen))
        print_gen(new_gen, rows, cols)
        print
        prev_gen = new_gen
        curr_gen += 1

print_num_gens(gen1, 6, 7, 10)