# -*- coding: utf-8 -*-
"""


@author: Admin
"""

import random

class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 1
        self.player_names = ["Player 1", "Player 2"]
        self.cpu_name = "CPU"
        self.winner = None

    def print_board(self):
        for row in self.board:
            print("|".join(row))
        print("1 2 3 4 5 6 7")

    def check_winner(self):
        for row in self.board:
            for i in range(4):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] != ' ':
                    self.winner = row[i]

        for col in range(7):
            for i in range(3):
                if self.board[i][col] == self.board[i + 1][col] == self.board[i + 2][col] == self.board[i + 3][col] != ' ':
                    self.winner = self.board[i][col]

        # Check diagonals
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != ' ':
                    self.winner = self.board[i][j]
            for j in range(3, 7):
                if self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3] != ' ':
                    self.winner = self.board[i][j]
    
    def make_move(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = 'X' if self.current_player == 1 else 'O'
                break

    def switch_player(self):
        self.current_player = 3 - self.current_player

    def cpu_move(self):
        valid_moves = [col for col in range(7) if self.board[0][col] == ' ']
        if valid_moves:
            return random.choice(valid_moves)
        else:
            return None

    def menu(self):
        print("Main Menu:")
        print("1. 2 Player Game")
        print("2. CPU Game")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")
        while choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a number between 1 and 3.")
            choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            self.player_names[0] = self.get_valid_name("Enter Player 1 name: ")
            self.player_names[1] = self.get_valid_name("Enter Player 2 name: ")
            self.play_game(2)
        elif choice == '2':
            self.player_names[0] = self.get_valid_name("Enter your name: ")
            self.player_names[1] = self.cpu_name
            self.play_game(1)
        elif choice == '3':
            print("Thanks for playing!")

    def get_valid_name(self, prompt):
        while True:
            name = input(prompt)
            if name.strip():  
                return name
            else:
                print("Name cannot be empty.")
        

    def play_game(self, mode):
        print("Welcome to Connect Four!")
        rematch = True
        while rematch:
            self.board = [[' ' for _ in range(7)] for _ in range(6)]
            self.winner = None
            self.current_player = 1

            while not self.winner:
                self.print_board()
                if mode == 1 and self.current_player == 2:
                    col = self.cpu_move()
                    if col is None:
                        print("The board is full. It's a draw!")
                        break
                    print(f"{self.cpu_name} chooses column {col + 1}")
                else:
                    while True:
                        try:
                            col = int(input(f"{self.player_names[self.current_player - 1]}, choose a column (1-7): ")) - 1
                            if col not in range(7):
                                raise ValueError
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number between 1 and 7.")

                self.make_move(col)
                self.check_winner()
                if all(cell != ' ' for row in self.board for cell in row):
                    print("The board is full. It's a draw!")
                    break
                self.switch_player()

            self.print_board()
            if self.winner == 'X':
                print(f"Congratulations, {self.player_names[0]} wins!")
            elif self.winner == 'O':
                print(f"Congratulations, {self.player_names[1]} wins!")
            else:
                print("It's a draw!")

            while True:
                rematch_choice = input("Do you want to play again? (yes/no): ")
                if rematch_choice.lower() in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if rematch_choice.lower() == 'no':
                while True:
                    back_to_menu = input("Do you want to go back to the menu or quit the game? (yes for menu/no to quit): ")
                    if back_to_menu.lower() in ['yes', 'no']:
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                if back_to_menu.lower() == 'yes':
                    self.menu()
                else:
                    print("Thanks for playing!")
                    rematch = False

if __name__ == "__main__":
    game = ConnectFour()
    game.menu()
