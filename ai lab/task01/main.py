class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  
        self.current_player = 'X'

    def display_board(self):
        print("\n")
        print(" " + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---|---|---")
        print(" " + self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---|---|---")
        print(" " + self.board[6] + " | " + self.board[7] + " | " + self.board[8])
        print("\n")

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6)              
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None

    def is_board_full(self):
        return ' ' not in self.board

    def play_game(self):
        while True:
            self.display_board()
            move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
            
            if self.board[move] != ' ':
                print("Invalid move! Try again.")
                continue
            
            self.board[move] = self.current_player
            winner = self.check_winner()
            
            if winner:
                self.display_board()
                print(f"Player {winner} wins!")
                break
            
            if self.is_board_full():
                self.display_board()
                print("It's a tie!")
                break
            
            
            self.current_player = 'O' if self.current_player == 'X' else 'X'


game = TicTacToe()
game.play_game()
