import random

width = 5
height = 5


def dead_state(width,height):
    width_list = []
    grid = []
    for elem in range(width):
        width_list.append(0)
    for elem in range(height):
        grid.append(width_list)
    return grid

def random_state(width, height):
    state =[]
    for i in range(height):
        width_list = []
        for j in range(width):
            random_number = random.random()
            print(random_number)
            if random_number <= .5000:
                current_cell_value = 0
            else:
                current_cell_value = 1
            width_list.append(current_cell_value)
        state.append(width_list)
    return state

def render(state):
    #print top border
    print("- "*width*2)
    #print each list on a line
    for list in state:
        print(list)
    #print bottom border
    print("- "*width*2)

def next_board_state(initial_state):
    new_state = random_state(width,height)

    for x in range(0, height):
        for y in range(0, width):
            current_cell_value = initial_state[x][y]
            neighbors_alive = alive_neighbors(x,y,initial_state)   
            #if alive cell
            if current_cell_value  == 1:
                if neighbors_alive <=1:
                    new_state[x][y] = 0
                elif neighbors_alive <= 3:
                    new_state[x][y] = 1
                else:
                    new_state[x][y] = 0 

            #if dead cell
            else:
                if neighbors_alive == 3:
                    new_state[x][y] = 1
                else:
                    new_state[x][y] = 0
    return(new_state)
    

#get num of neighbors alive
def alive_neighbors(x,y,initial_state):
    neighbors_alive = 0

    #above left
    if initial_state[x-1][y-1] == 0:
        neighbors_alive += 0
    else:
        neighbors_alive += 1
    #print("current neihbors alive =" + str(neighbors_alive))
    
    #above center
    if initial_state[x][y-1] == 0:
        neighbors_alive += 0
    else:
        neighbors_alive += 1
    #above right
    if initial_state[x+1][y-1] == 0:
        neighbors_alive += 0
    else:
        neighbors_alive += 1
    #same line left
    if initial_state[x-1][y] == 0:
        neighbors_alive += 0
    else:
        neighbors_alive += 1
    #same line right
    if initial_state[x+1][y] == 0:
        neighbors_alive += 0
    else:
        neighbors_alive += 1
    #below left
    if initial_state[x-1][y+1] == 0:
        neighbors_alive += 0
    else:
        neighbors_alive += 1
    #below center   
    if initial_state[x][y-1] == 0:
        neighbors_alive += 0
    else:
        neighbors_alive += 1
    #below right  
    if initial_state[x+1][y+1] == 0:
        neighbors_alive += 0
    else:
        neighbors_alive += 1
    return neighbors_alive

#induced = random_state(width,height)
#print(induced)
#render(induced)
#initial_state = random_state(width,height)
print(next_board_state(initial_state))
