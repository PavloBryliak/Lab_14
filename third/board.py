import random


class Board:
    winning_combinations = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    winners = ('X-won', 'Draw', 'O-won')

    def __init__(self, squares=[]):
        if len(squares) == 0:
            self.squares = [None for i in range(9)]
        else:
            self.squares = squares

    def show(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print(element)
        print()

    def available_moves(self):
        """Checks available moves"""
        return [k for k, v in enumerate(self.squares) if v is None]

    def complete(self):
        """Checks whether game field is full."""
        if None not in [v for v in self.squares]:
            return True
        if self.winner() != None:
            return True
        return False

    def x_won(self):
        return self.winner() == 'X'

    def o_won(self):
        return self.winner() == 'O'

    def draw(self):
        return self.complete() == True and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for combo in self.winning_combinations:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
        self.squares[position] = player


def computer(player):
    if player == 'X':
        return 'O'
    return 'X'