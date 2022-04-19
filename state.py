from utils import move_valid
from random import randrange


class State:
    def __init__(self, grid=None, score=0, sz=4, p2=0.9, p4=0.1):
        if grid is None:
            self.grid = [0 for _ in range(sz ** 2)]
        else:
            self.grid = grid
        self.score = score
        self.sz = sz
        self.p2 = p2
        self.p4 = p4

    def new_index(self):
        empty_indices = [i for i in range(self.sz ** 2) if self.grid[i] == 0]
        index = empty_indices[randrange(len(empty_indices))]
        return index

    def new_number(self):
        number_space = [1 for _ in range(int(self.p2 * 20))]
        for i in range(int(self.p4 * 20)):
            number_space.append(2)
        n = number_space[randrange(len(number_space))]
        return n

    def generate_number(self):
        index = self.new_index()
        new_n = self.new_number()
        self.grid[index] = new_n

    def left_moved_state(self):
        new_grid = []
        utility = 0

        for row in range(self.sz):
            # eliminate 0s
            new_row = [p for p in self.grid[self.sz*row:self.sz*(row+1)] if p != 0]

            i = 0
            while i < len(new_row) - 1:
                # combine the same powers
                if new_row[i] == new_row[i + 1]:
                    new_row[i] += 1
                    utility += new_row[i]
                    new_row.pop(i + 1)
                i += 1

            # fill the edges with 0
            len_new_row = len(new_row)
            for j in range(self.sz - len_new_row):
                new_row.append(0)

            # replace the row
            for col in range(self.sz):
                new_grid.append(new_row[col])

        # create the new state
        new_score = self.score + utility * 10
        new_state = State(new_grid, new_score, self.sz, self.p2, self.p4)

        return new_state

    def right_moved_state(self):
        new_grid = []
        utility = 0

        for row in range(self.sz):
            # eliminate 0s
            new_row = [p for p in self.grid[self.sz * row:self.sz * (row + 1)] if p != 0]

            i = len(new_row) - 1
            while i > 0:
                # combine the same powers
                if new_row[i] == new_row[i - 1]:
                    new_row[i] += 1
                    utility += new_row[i]
                    new_row.pop(i - 1)
                    i -= 2
                else:
                    i -= 1

            # fill the edges with 0
            len_new_row = len(new_row)
            for j in range(self.sz - len_new_row):
                new_row.insert(0, 0)

            # replace the row
            for col in range(self.sz):
                new_grid.append(new_row[col])

        # create the new state
        new_score = self.score + utility * 10
        new_state = State(new_grid, new_score, self.sz, self.p2, self.p4)

        return new_state

    def up_moved_state(self):
        new_grid = [0 for _ in range(self.sz ** 2)]
        utility = 0

        for col in range(self.sz):
            # eliminate 0s
            new_col = []
            for row in range(self.sz):
                p = self.grid[self.sz * row + col]
                if p != 0:
                    new_col.append(p)

            i = 0
            while i < len(new_col) - 1:
                # combine the same powers
                if new_col[i] == new_col[i + 1]:
                    new_col[i] += 1
                    utility += new_col[i]
                    new_col.pop(i + 1)
                i += 1

            # fill the edges with 0
            len_new_col = len(new_col)
            for j in range(self.sz - len_new_col):
                new_col.append(0)

            # replace the col
            for row in range(self.sz):
                new_grid[self.sz * row + col] = new_col[row]

        # create the new state
        new_score = self.score + utility * 10
        new_state = State(new_grid, new_score, self.sz, self.p2, self.p4)

        return new_state

    def down_moved_state(self):
        new_grid = [0 for _ in range(self.sz ** 2)]
        utility = 0

        for col in range(self.sz):
            # eliminate 0s
            new_col = []
            for row in range(self.sz):
                p = self.grid[self.sz * row + col]
                if p != 0:
                    new_col.append(p)

            i = len(new_col) - 1
            while i > 0:
                # combine the same powers
                if new_col[i] == new_col[i - 1]:
                    new_col[i] += 1
                    utility += new_col[i]
                    new_col.pop(i - 1)
                    i -= 2
                else:
                    i -= 1

            # fill the edges with 0
            len_new_col = len(new_col)
            for j in range(self.sz - len_new_col):
                new_col.insert(0, 0)

            # replace the col
            for row in range(self.sz):
                new_grid[self.sz * row + col] = new_col[row]

        # create the new state
        new_score = self.score + utility * 10
        new_state = State(new_grid, new_score, self.sz, self.p2, self.p4)

        return new_state

    def valid_states(self):
        states = []

        new_state_functions = (
            self.left_moved_state, self.up_moved_state,
            self.right_moved_state, self.down_moved_state
        )

        for fn in new_state_functions:
            new_state = fn()
            if move_valid(self.grid, new_state.grid):
                states.append(new_state)
            else:
                states.append(None)

        return states
