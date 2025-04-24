


class Battlegrid:
    def __init__(self, N):
        self.N = N
        self.grid = [[0 for _ in range(N)] for _ in range(N)]
        

    def set_cell(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))