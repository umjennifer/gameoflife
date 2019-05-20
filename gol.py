import random

# Corner cell's non-existent neighbors
    #A1 : (x-1,y+1) and (x-1,y) and (x-1,y-1) and (x,y-1) and (x+1,y-1)
    #A4 : (x-1,y-1) and (x,y-1) and (x+1,y-1) and (x+1,y) and (x+1,y+1)
    #D1 : (x-1,y-1) and (x-1,y) and (x-1,y+1) and (x,y+1) and (x+1,y+1) 
    #D4 : (x-1,y+1) and (x,y+1) and (x+1,y+1) and (x+1,y) and (x+1,y-1)

# Edge cell's non existent  neighbors
    #TE : (x-1,y-1) and (x,y-1) and (x+1,y-1)
    #LE : (x-1,y-1) and (x-1,y) and (x-1,y+1)
    #RE : (x+1,y-1) and (x+1,y) and (x+1,y+1) 
    #BE : (x-1,y+1) and (x,y+1) and (x+1,y+1):

class Grid:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.state = self.random_state()

    #random state maker, not setter; setting is done explicitly
    def random_state(self):
        state =[]
        for i in range(self.width):
            width_list = []
            for j in range(self.height):
                random_number = random.random()
                if random_number <= .5000:
                    current_cell_value = 0
                else:
                    current_cell_value = 1
                width_list.append(current_cell_value)
            state.append(width_list)
        return state
    
    def render(self):
        print("- " * self.width *3 )
        #print each list on a line
        for y in range(self.height):
            for x in range(self.width):
                print(str(self.state[x][y]), end="     ")
            print("")
        #print bottom border
        print("- " * self.width * 3)

    #Does NOT return a new board; mutates the existing board
    #can't edit list while iterating through it
    def next_state(self):
        newest_board_state = []
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                #count cell's # of neighbors alive
                neighbors_alive = self.count_neighbors_alive(x,y)
                #based on count, decide if the cell is either dead("0") or alive("1")
                #append the cell to "row"; start of building the board
                row.append(self.set_dead_alive(x,y,neighbors_alive))
            newest_board_state.append(row)
                #add the updated cells to newest_board_state list
        return newest_board_state        

    def set_dead_alive(self,neighbors_alive):
        pass
    
    def count_neighbors_alive(self,x,y):
        alive_neighbors = 0
        if self.is_corner(x,y) == True:
            alive_neighbors += self.corner_neighbors_alive_count(x,y)
        #elif edge
        elif self.is_edge(x,y) == True:
            alive_neighbors += self.edge_neighbors_alive_count(x,y)

        #else
    
   
   
    def is_corner(self,x,y):
        coord = (x, y)

        if coord == (0, 0) or coord == (0,self.height-1) or coord == (self.width-1,self.height-1) or coord == (self.width-1, 0):
            return True
        else:
            return False

    def corner_neighbors_alive_count(self,x,y):
        coord = (x,y)
        alive_neighbors = 0
        if coord == (0,0):
            if self.state[x+1][y] == 1:
                alive_neighbors += 1
            if self.state[x+1][y+1] == 1:
                alive_neighbors += 1
            if self.state[x][y+1] == 1:
                alive_neighbors +=1
            return alive_neighbors

        #elif TR
        if coord == (self.width-1,0):
            if self.state[x-1][y] == 1:
                alive_neighbors += 1
            if self.state[x-1][y+1] == 1:
                alive_neighbors += 1
            if self.state[x][y+1] == 1:
                alive_neighbors +=1
            return alive_neighbors

        #elif BL
        if coord == (0,self.height-1):
            if self.state[x][y-1] == 1:
                alive_neighbors += 1
            if self.state[x+1][y-1] == 1:
                alive_neighbors += 1
            if self.state[x+1][y] == 1:
                alive_neighbors +=1
            return alive_neighbors           
            
        #elif Br
        if coord == (self.width-1,self.height-1):
            if self.state[x][y-1] == 1:
                alive_neighbors += 1
            if self.state[x-1][y-1] == 1:
                alive_neighbors += 1
            if self.state[x-1][y] == 1:
                alive_neighbors +=1
            return alive_neighbors

    def is_edge(self,x,y):
        if not self.is_corner(x,y):
            if x in [0, self.width-1] or y in [0, self.height-1]:
                return True
        return False
                
    def edge_neighbors_alive_count(self,x,y):
        pass


        
        

#width = input("What is the width of the grid? \nAnswer: ")
#height = input("What is the height of the grid? \nAnswer: ")
width = 7
height = 7
my_grid = Grid(width,height)

my_grid.render()

#test corners and number of neighbors alive
#print("neighbors alive of TL: " + str(my_grid.corner_neighbors_alive_count(0,0)))
#print("neighbors alive of TR: " + str(my_grid.corner_neighbors_alive_count(width-1,0)))
#print("neighbors alive of BL: " + str(my_grid.corner_neighbors_alive_count(0,height-1)))
#print("neighbors alive of BR: " + str(my_grid.corner_neighbors_alive_count(width-1,height-1)))

####test edge and number of neighbors alive
#actually corners, should not work
#print("neighbors alive of TL: " + str(my_grid.edge_neighbors_alive_count(0,0)))
#print("neighbors alive of TR: " + str(my_grid.edge_neighbors_alive_count(width-1,0)))
#print("neighbors alive of BL: " + str(my_grid.edge_neighbors_alive_count(0,height-1)))
#print("neighbors alive of BR: " + str(my_grid.edge_neighbors_alive_count(width-1,height-1)))

#edges, should work
#print("neighbors alive of TE: " + str(my_grid.edge_neighbors_alive_count(5,0)))
#print("neighbors alive of LE: " + str(my_grid.edge_neighbors_alive_count(0,5)))
#print("neighbors alive of BE: " + str(my_grid.edge_neighbors_alive_count(5,height-1)))
#print("neighbors alive of RE: " + str(my_grid.edge_neighbors_alive_count(width-1,5)))









