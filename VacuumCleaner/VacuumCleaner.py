CLEAN = 'C'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'
MOVE_DOWN = 'D'

MOVES = {
    MOVE_LEFT: (0, -1),
    MOVE_RIGHT: (0, 1),
    MOVE_UP: (-1, 0),
    MOVE_DOWN: (1, 0)
}

class VacuumCleaner:
    def __init__(self, grid, start_pos):
        self.grid = grid
        self.pos = start_pos
        self.cleaned = set()
        self.actions = []
        self.visited = set()

    def clean(self):
        x, y = self.pos
        if self.grid[x][y] == 1:
            print(f"Cleaning room at {x}, {y}")
            self.grid[x][y] = 0
            self.cleaned.add(self.pos)
            self.actions.append(f"Clean at ({x}, {y})")

    def move(self, direction):
        dx, dy = MOVES[direction]
        x, y = self.pos
        new_pos = (x + dx, y + dy)
        if 0 <= new_pos[0] < 2 and 0 <= new_pos[1] < 2:
            self.pos = new_pos
            print(f"Move {direction} to {self.pos}")
            self.actions.append(f"Move {direction} to {self.pos}")
            return True
        return False

    def all_cleaned(self):
        return len(self.cleaned) == 4

    def dfs(self):
        self.visited.add(self.pos)
        self.clean()
        for direction in [MOVE_LEFT, MOVE_RIGHT, MOVE_UP, MOVE_DOWN]:
            dx, dy = MOVES[direction]
            new_pos = (self.pos[0] + dx, self.pos[1] + dy)
            if 0 <= new_pos[0] < 2 and 0 <= new_pos[1] < 2 and new_pos not in self.visited:
                self.move(direction)
                self.dfs()

    def move_back(self, direction):
        reverse_moves = {
            MOVE_LEFT: MOVE_RIGHT,
            MOVE_RIGHT: MOVE_LEFT,
            MOVE_UP: MOVE_DOWN,
            MOVE_DOWN: MOVE_UP
        }
        self.move(reverse_moves[direction])


grid = [
    [1, 1],
    [1, 1]
]

start_pos = (0, 0)
vacuum = VacuumCleaner(grid, start_pos)

print("Starting DFS for cleaning rooms...\n")
vacuum.dfs()

print("\nAll rooms are cleaned!")
print(f"Total actions taken: {len(vacuum.actions)}")
print("Action sequence:")
for act in vacuum.actions:
    print("-", act)
