class TicTacToe():
    # Create initial states
    def __init__(self, state=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.state = state

    # make moves and specify the rows and cols
    def make_move(self, row, col, val):
        if (isinstance(row, int)) and (row >= 0) and (row <= 2):
            if (isinstance(col, int)) and (col >= 0) and (col <= 2):
                if self.state[row][col] == 0:
                    if (val == -1) or (val == 1):
                        self.state[row][col] = val
                        return True
        return False

    # test out a move: set val to the cell
    # with coordinates [row, col]
    def try_move(self, state, row, col, val):
        if (isinstance(row, int)) and (row >= 0) and (row <= 2):
            if (isinstance(col, int)) and (col >= 0) and (col <= 2):
                if state[row][col] == 0:
                    if (val == -1) or (val == 1):
                        new_state = [row[:] for row in state]
                        new_state[row][col] = val
                        return new_state
        return state

    # check if the terminal node
    def terminal_node(self, state):
        # result of the game
        # win1 = +10, win2 = -10, tie=0
        result = 0
        isGameOver = False

        # check if there is an empty cell
        emptyCells = False
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    emptyCells = True

        # check rows if there is a winner
        isWinner = False
        for i in range(3):
            sum_p1 = 0
            sum_p2 = 0
            for j in range(3):
                if state[i][j] == 1:
                    sum_p1 += 1
                if state[i][j] == -1:
                    sum_p2 += -1
            if (sum_p1 == 3) or (sum_p2 == -3):
                isWinner = True
                if (sum_p1 == 3):
                    result = 10
                if (sum_p2 == -3):
                    result = -10

        # check cols if there is a winner
        for j in range(3):
            sum_p1 = 0
            sum_p2 = 0
            for i in range(3):
                if state[i][j] == 1:
                    sum_p1 += 1
                if state[i][j] == -1:
                    sum_p2 += -1
            if (sum_p1 == 3) or (sum_p2 == -3):
                isWinner = True
                if (sum_p1 == 3):
                    result = 10
                if (sum_p2 == -3):
                    result = -10

        # check diagonals if there is a winner
        sum_p1 = 0
        sum_p2 = 0
        for i in range(3):
            if state[i][i] == 1:
                sum_p1 += 1
            if state[i][i] == -1:
                sum_p2 += -1
        if (sum_p1 == 3) or (sum_p2 == -3):
            isWinner = True
            if (sum_p1 == 3):
                result = 10
            if (sum_p2 == -3):
                result = -10

        sum_p1 = 0
        sum_p2 = 0
        for i in range(3):
            if state[i][2 - i] == 1:
                sum_p1 += 1
            if state[i][2 - i] == -1:
                sum_p2 += -1
        if (sum_p1 == 3) or (sum_p2 == -3):
            isWinner = True
            if (sum_p1 == 3):
                result = 10
            if (sum_p2 == -3):
                result = -10

        isGameOver = isWinner or not emptyCells
        return {"gameover": isGameOver, "result": result}

    # find the children of the given state
    # returns the coordinates (x,y) of empty cells
    def expand_state(self, state):
        children = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    child = [i, j]
                    children.append(child)
        return children

    # minimax algorithm
    def minimax(self, state, depth, player):
        # check if the current state is a terminal node
        terminal = self.terminal_node(state)
        if terminal["gameover"]:
            return terminal["result"]

        # maximize for the computer player
        if player == 1:
            best_score = -float("inf")
            children = self.expand_state(state)
            for child in children:
                new_state = self.try_move(state, child[0], child[1], player)
                score = self.minimax(new_state, depth + 1, -player)
                best_score = max(best_score, score)
            return best_score

        # minimize for the human player
        else:
            best_score = float("inf")
            children = self.expand_state(state)
            for child in children:
                new_state = self.try_move(state, child[0], child[1], player)
                score = self.minimax(new_state, depth + 1, -player)
                best_score = min(best_score, score)
            return best_score

    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("You are X and the computer is O.")
        print("Enter the row and column of your move (0-2).")
        print("For example, to play in the top right corner, enter '0 2'.")
        print("You can quit at any time by entering 'q'.")
        player = 1
        while not self.terminal_node(self.state)["gameover"]:
            if player == 1:
                # human player's turn
                print("Your turn.")
                row, col = input("Enter row and column: ").split()
                if row == "q" or col == "q":
                    print("Quitting...")
                    return
                row, col = int(row), int(col)
                if self.make_move(row, col, player):
                    print(self.make_move(row, col, player))
                    player = -1
                else:
                    print("Invalid move. Try again.")
            else:
                # computer player's turn
                print("Bot's turn.")
                best_score = -float("inf")
                best_move = None
                children = self.expand_state(self.state)
                for child in children:
                    new_state = self.try_move(self.state, child, child, -player)
                    score = self.minimax(new_state, 0, player)
                    if score > best_score:
                        best_score = score
                        best_move = child
                self.make_move(best_move, best_move, -player)
                print(self.make_move(best_move, best_move, -player))
                player = 1
            # print the current state of the game
            print("Current state of the game:")
            for row in self.state:
                print(row)
        # game over
        result = self.terminal_node(self.state)["result"]
        if result == 0:
            print("It's a tie!")
        elif result == 10:
            print("You win!")
        else:
            print("Computer wins!")

game = TicTacToe()
game.play()
