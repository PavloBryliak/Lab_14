import random

from fourth.board import Board, computer


if __name__ == "__main__":
    board = Board()
    board.show()

    while not board.complete():
        player = 'X'
        player_move = int(input("Next Move: ")) - 1
        if not player_move in board.available_moves():
            continue
        board.make_move(player_move, player)
        board.show()

        if board.complete():
            break
        player = computer(player)
        computer_move = random.choice(board.available_moves())
        board.make_move(computer_move, player)
        board.show()
    print(board.winner(), "won!")