import random
import pdb
import time

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
        print("- " * (self.width *3 - 2))
        #print each list on a line
        for y in range(self.height):
            for x in range(self.width):
                print(str(self.state[x][y]), end="     ")
            print("")
        #print bottom border
        print("- " * (self.width *3 - 2))

    #Does NOT return a new board; mutates the existing board
    #can't edit list while iterating through it
    def next_state(self):
        newest_board_state = []
        for x in range(self.width):
            row = []
            for y in range(0, self.height):
                #count cell's # of neighbors alive
                neighbors_alive = self.count_neighbors_alive(x,y)
                #based on count, decide if the cell is either dead("0") or alive("1")
                #append the cell to "row"; start of building the board
                row.append(self.get_dead_alive(x,y,neighbors_alive))
            newest_board_state.append(row)
                #add the updated cells to newest_board_state list
        return newest_board_state        

    def get_dead_alive(self,x,y,neighbors_alive):
        current_cell_value = self.state[x][y]
        #if current cell is alive
        if current_cell_value == 1:
            if neighbors_alive <=1:
               return 0
            elif neighbors_alive <= 3:
                return 1
            else:
                return 0 

        #if dead cell
        else:
            if neighbors_alive == 3:
                return 1
            else:
                return 0
    
    def count_neighbors_alive(self,x,y):
        neighbors_alive = 0
        if self.is_corner(x,y) == True:
            neighbors_alive += self.corner_neighbors_alive_count(x,y)
        #elif edge
        elif self.is_edge(x,y) == True:
            neighbors_alive += self.edge_neighbors_alive_count(x,y)
        else:
            neighbors_alive += self.normal_neighbors_alive_count(x,y)
        return neighbors_alive
   
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
            
        #elif BR
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
        coord = (x,y)
        alive_neighbors = 0
        if not self.is_corner(x,y):
                    #if LE
            if coord == (0,y):
                if self.state[x][y-1] == 1:
                    alive_neighbors += 1
                if self.state[x+1][y-1] == 1:
                    alive_neighbors += 1
                if self.state[x+1][y] == 1:
                    alive_neighbors += 1
                if self.state[x+1][y+1] == 1:
                    alive_neighbors += 1
                if self.state[x][y+1] == 1:
                    alive_neighbors += 1    
                return alive_neighbors    
            #if RE
            if coord == (self.width-1,y):
                if self.state[x][y-1] == 1:
                    alive_neighbors += 1
                if self.state[x-1][y-1] == 1:
                    alive_neighbors += 1
                if self.state[x-1][y] == 1:
                    alive_neighbors += 1
                if self.state[x-1][y+1] == 1:
                    alive_neighbors += 1
                if self.state[x][y+1] == 1:
                    alive_neighbors += 1    
                return alive_neighbors 
            #if TE
            if coord == (x,0):
                if self.state[x-1][y] == 1:
                    alive_neighbors += 1
                if self.state[x-1][y+1] == 1:
                    alive_neighbors += 1
                if self.state[x][y+1] == 1:
                    alive_neighbors += 1
                if self.state[x+1][y+1] == 1:
                    alive_neighbors += 1
                if self.state[x+1][y] == 1:
                    alive_neighbors += 1    
                return alive_neighbors                         
            #if BE
            if coord == (x,self.height-1):
                #pdb.set_trace()
                if self.state[x-1][y] == 1:
                    alive_neighbors += 1
                if self.state[x-1][y-1] == 1:
                    alive_neighbors += 1
                if self.state[x][y-1] == 1:
                    alive_neighbors += 1
                if self.state[x+1][y-1] == 1:
                    alive_neighbors += 1
                if self.state[x+1][y] == 1:
                    alive_neighbors += 1    
                return alive_neighbors 
            
    def normal_neighbors_alive_count(self,x,y):
        coord = (x,y)
        alive_neighbors = 0
        if self.state[x-1][y-1] == 1:
            alive_neighbors += 1
        if self.state[x][y-1] == 1:
            alive_neighbors += 1
        if self.state[x+1][y-1] == 1:
            alive_neighbors += 1
        if self.state[x+1][y] == 1:
            alive_neighbors += 1
        if self.state[x+1][y+1] == 1:
            alive_neighbors += 1
        if self.state[x][y+1] == 1:
            alive_neighbors += 1
        if self.state[x-1][y+1] == 1:
            alive_neighbors += 1
        if self.state[x-1][y] == 1:
            alive_neighbors += 1      
        return alive_neighbors  
    
    def main(self):
        x = 0
        while x < 6:
            self.state = self.next_state()
            self.render()
            x= x+1
            time.sleep(3)
            

width = input("What is the width of the grid? \nAnswer: ")
height = input("What is the height of the grid? \nAnswer: ")
#width = 7
#height = 7
my_grid = Grid(int(width),int(height))
my_grid.main()

# my_grid.render()
# print("corner TL: " + str(my_grid.count_neighbors_alive(0,0)))
# print("corner TR: " + str(my_grid.count_neighbors_alive(width-1,0)))
# print("corner BL: " + str(my_grid.count_neighbors_alive(0,height-1)))
# print("corner BR: " + str(my_grid.count_neighbors_alive(width-1,height-1)))
# print("edge TE (5,0): " + str(my_grid.count_neighbors_alive(5,0)))
# print("edge (0,5): " + str(my_grid.count_neighbors_alive(0,5)))
# print("edge (5,height-l): " + str(my_grid.count_neighbors_alive(5,height-1)))
# print("edge (width-1, 5): " + str(my_grid.count_neighbors_alive(width-1,5)))
# print("inner 5,5: " + str(my_grid.count_neighbors_alive(5,5)))
# print("inner 2,4: " + str(my_grid.count_neighbors_alive(2,4)))
# print("inner 3,1: " + str(my_grid.count_neighbors_alive(3,1)))


##########corner_neighbors_alive_count test
#print("neighbors alive of TL: " + str(my_grid.corner_neighbors_alive_count(0,0)))
#print("neighbors alive of TR: " + str(my_grid.corner_neighbors_alive_count(width-1,0)))
#print("neighbors alive of BL: " + str(my_grid.corner_neighbors_alive_count(0,height-1)))
#print("neighbors alive of BR: " + str(my_grid.corner_neighbors_alive_count(width-1,height-1)))


##########edge_neighbors_alive_count test
#actually corners, should not work
# print("not edge TL: " + str(my_grid.edge_neighbors_alive_count(0,0)))
# print("not edge TR: " + str(my_grid.edge_neighbors_alive_count(width-1,0)))
# print("not edge BL: " + str(my_grid.edge_neighbors_alive_count(0,height-1)))
# print("not edge BR: " + str(my_grid.edge_neighbors_alive_count(width-1,height-1)))
# #edges, should work
# print("neighbors alive of TE (5,0): " + str(my_grid.edge_neighbors_alive_count(5,0)))
# print("neighbors alive of LE (0,5): " + str(my_grid.edge_neighbors_alive_count(0,5)))
# print("neighbors alive of BE (5,height-l): " + str(my_grid.edge_neighbors_alive_count(5,height-1)))
# print("neighbors alive of RE (width-1, 5): " + str(my_grid.edge_neighbors_alive_count(width-1,5)))









