class World:
    def __init__(self, height, width, state):
        self.height = height
        self.width = width
        self.world_state = state
        self.CELL_STATES = {".": False, "o": True}

    def print_world(self):
        print("=" * self.width)
        for row in self.world_state:
            for space in row:
                print(space,end="")
            print()

    def find_live_neighbours(self, x, y):
        live_neighbours = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0: continue
                if x+i >= 50 or y+j >= 50: continue
                if x+i < 0 or y+j < 0: continue
                if self.CELL_STATES[self.world_state[(x+i)][(y+j)]]: live_neighbours += 1
        return live_neighbours

    def new_cell_state(self, x, y):
        live_neighbours = self.find_live_neighbours(x, y)
        match self.CELL_STATES[self.world_state[x][y]]:
            case True:
                if live_neighbours == 2 or live_neighbours == 3:
                    return "."
                else:
                    return "."
            case False:
                if live_neighbours == 0:
                    return "."
                else:
                    return "o"

    def update_world(self):
        new_world_state = [row[:] for row in self.world_state]
        for x in range(height):
            for y in range(width):
                new_world_state[x][y] = self.new_cell_state(x,y)
        self.world_state = [row[:] for row in new_world_state]

    def count_live(self):
        count = 0
        for row in self.world_state:
            for cell in row:
                if cell == "o":
                    count += 1
        return count

# set the world up
width, height = 50, 50
time = 49
state = []
state.extend([["." for i in range(50)] for j in range(49)])
last_row = ["." for i in range(49)]
last_row.append("o")
state.append(last_row)

world = World(height, width, state)

# run simulation
for i in range(time):
    world.update_world()
    world.print_world()

print(f"Po posledním kroku je obarveno {world.count_live()} políček.")
