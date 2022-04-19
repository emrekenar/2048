from state import State
from constants import SUCCESS, GAME_OVER, QUIT
from utils import request_move
from os import system


class Game:
    def __init__(self, sz=4, p4=0.1):
        self.sz = sz
        self.p2 = 1 - p4
        self.p4 = p4

        self.powers = {i: 2 ** i for i in range(16)}
        self.moves = {0: '->', 1: 'v', 2: '<-', 3: '^'}

        self.state = State(sz=sz, p2=self.p2, p4=p4)

        for _ in range(2):
            self.state.generate_number()

    def get_make_move(self):
        valid_states = self.state.valid_states()
        valid_moves = []
        for state in valid_states:
            if state is not None:
                valid_moves.append(True)
            else:
                valid_moves.append(False)

        if sum(valid_moves) == 0:
            return GAME_OVER

        next_move = request_move(valid_moves)

        if next_move == 'q':
            return QUIT

        new_state = valid_states[next_move]
        self.state = new_state

        return SUCCESS

    def play(self):
        while True:
            system('clear')
            print(self)
            feedback = self.get_make_move()
            if feedback == GAME_OVER:
                print('Game over. Score:', self.state.score)
                break
            elif feedback == QUIT:
                print('Shutting down. Score:', self.state.score)
                break
            else:
                self.state.generate_number()

    def __str__(self):
        s = ''

        for i in range(self.sz):
            s += '------'
        s += '-\n'

        for row in range(self.sz):
            for col in range(self.sz):
                i = row * self.sz + col
                n = self.state.grid[i]
                if n == 0:
                    s += '|     '
                else:
                    s += '|{:^5d}'.format(self.powers[self.state.grid[i]])
            s += '|\n'

            for i in range(self.sz):
                s += '------'
            s += '-\n'

        return s
