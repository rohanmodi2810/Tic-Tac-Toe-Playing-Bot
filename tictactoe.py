class TicTacToe:
    human = -1
    cpu = +1
    chars = {
        -1: 'X',
        +1: 'O',
        0: ' '
    }
    str_line = '---------------'

    def __init__(self, board=None, parent=None):
        # 0 1 2
        # 3 4 5
        # 6 7 8
        if board is None:
            board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.board = board
        self.parent = parent
        self.win = self.initwin()

    def emptyindices(self):
        return [i for i, x in enumerate(self.board) if x == 0]

    def getnextmoves(self, player):
        indices = self.emptyindices()
        moves = []
        for i in indices:
            board = self.board.copy()
            board[i] = player
            moves.append(TicTacToe(board, self))
        return moves

    def move(self, index, player):
        self.board[index] = player

    def initwin(self):
        # win happens when
        # 123,456,789,147,258,369,159,357
        win = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[3], self.board[4], self.board[5]],
            [self.board[6], self.board[7], self.board[8]],
            [self.board[0], self.board[3], self.board[6]],
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[0], self.board[4], self.board[8]],
            [self.board[2], self.board[4], self.board[6]],
        ]
        return win

    def wins(self, player):
        if [player, player, player] in self.win:
            return True
        else:
            return False

    def print2d(self):
        print('\n' + TicTacToe.str_line)
        i = -1
        for cell in self.board:
            i = i + 1
            symbol = TicTacToe.chars[cell]
            print(f'| {symbol} |', end='')
            if i in [2, 5, 8]:
                print('\n' + TicTacToe.str_line)
