"""
TIC TAC TOE!
"""
import turtle
import math
import copy
import board_drawer

class TicTacToe():
    """Tic Tac Toe Game"""
    __BOARD_DEFAULT = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

    __TAKEN_DEFAULT = [[False, False, False],
                       [False, False, False],
                       [False, False, False]]

    def __init__(self):
        self.__cell_size = 100
        self.__grid_size = 3
        self.__cell_margin = 10
        self.__start_x = -(self.__cell_size * self.__grid_size / 2)
        self.__start_y = (self.__cell_size * self.__grid_size / 2)
        self.__pen_size = 5
        self.__stroke_size = 10
        self.__pen = turtle.Turtle()
        self.__pen.hideturtle()
        self.__pen.speed(8)
        self.__pen.pensize(self.__pen_size)
        self.__turn = 0
        self.__click_processed = True
        self.__game_is_finished = False
        self.__board = copy.deepcopy(self.__BOARD_DEFAULT)
        self.__taken = copy.deepcopy(self.__TAKEN_DEFAULT)
        turtle.title('TIC TAC TOE')
        self.__drawer = board_drawer.Drawer(self.__start_x, self.__start_y)

    def __stroke_winning_row(self, row):
        """Stroke the winning row"""
        pen_x = self.__start_x + self.__cell_margin
        pen_y = self.__start_y - row * self.__cell_size - self.__cell_size / 2
        self.__pen.penup()
        self.__pen.goto(pen_x, pen_y)
        self.__pen.pendown()
        stroke_length = self.__grid_size * self.__cell_size - self.__cell_margin * 2
        self.__pen.color('red')
        self.__pen.pensize(self.__stroke_size)
        self.__pen.forward(stroke_length)
        self.__pen.pensize(self.__pen_size)
        self.__pen.color('black')
        return


    def __stroke_winnning_col(self, col):
        """Stroke the winning column"""
        pen_x = self.__start_x + col * self.__cell_size + self.__cell_size / 2
        pen_y = self.__start_y - self.__cell_margin
        self.__pen.penup()
        self.__pen.goto(pen_x, pen_y)
        self.__pen.pendown()
        stroke_length = self.__grid_size * self.__cell_size - self.__cell_margin * 2
        self.__pen.color('red')
        self.__pen.right(90)
        self.__pen.pensize(self.__stroke_size)
        self.__pen.forward(stroke_length)
        self.__pen.pensize(self.__pen_size)
        self.__pen.color('black')
        self.__pen.left(90)
        return


    def __check_rows(self):
        """Check rows for win state"""
        for i in range(self.__grid_size):
            if self.__board[i][0] == self.__board[i][1] == self.__board[i][2] and self.__board[i][0] != 0:
                self.__stroke_winning_row(i)
                return self.__board[i][0]

        return -1

    def __check_cols(self):
        """Check columns for win state"""
        for col in range(self.__grid_size):
            if self.__board[0][col] == self.__board[1][col] == self.__board[2][col] and self.__board[0][col] != 0:
                self.__stroke_winnning_col(col)
                return self.__board[col][0]

        return -1

    def __stroke_winning_diagonal(self, diagonal):
        """Stroke the winning diagonal"""
        pen_x = self.__start_x + self.__cell_margin
        pen_y = self.__start_y - diagonal * self.__cell_size - self.__cell_margin
        self.__pen.penup()
        self.__pen.goto(pen_x, pen_y)
        self.__pen.pendown()
        stroke_length = self.__grid_size * self.__cell_size * math.sqrt(2) - self.__cell_margin * 3
        self.__pen.color('red')
        if diagonal == 0:
            self.__pen.right(45)
            self.__pen.pensize(self.__stroke_size)
            self.__pen.forward(stroke_length)
            self.__pen.pensize(self.__stroke_size)
            self.__pen.left(45)
        else:
            pen_y += self.__cell_margin * 2
            self.__pen.penup()
            self.__pen.goto(pen_x, pen_y)
            self.__pen.pendown()
            self.__pen.left(45)
            self.__pen.pensize(self.__stroke_size)
            self.__pen.forward(stroke_length)
            self.__pen.pensize(self.__pen_size)
            self.__pen.right(45)
        self.__pen.color('black')
        return

    def __check_diags(self):
        """Check diagonals for a win state"""
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] and self.__board[0][0] != 0:
            self.__stroke_winning_diagonal(0)
            return self.__board[0][0]

        if self.__board[2][0] == self.__board[1][1] == self.__board[0][2] and self.__board[2][0] != 0:
            self.__stroke_winning_diagonal(3)
            return self.__board[2][0]

        return -1

    def __check_for_winner(self):
        """Check the board at current state for a winner"""
        winner = self.__check_rows()
        if winner == -1:
            winner = self.__check_cols()

        if winner == -1:
            winner = self.__check_diags()

        if winner != -1:
            return winner

        return -1


    def __draw_shape(self, row, col, player):
        """Draw a circle or square depending on which player's turn it is"""
        stroke_length = self.__cell_size * math.sqrt(2) - self.__cell_margin * 3
        if player == 1:
            self.__pen.penup()
            stroke_start_x = self.__start_x + self.__cell_size * col + self.__cell_margin
            stroke_start_y = self.__start_y - self.__cell_size * row - self.__cell_margin
            self.__pen.goto(stroke_start_x, stroke_start_y)
            self.__pen.pendown()
            self.__pen.right(45)
            self.__pen.forward(stroke_length)
            self.__pen.left(45)
            self.__pen.penup()
            stroke_start_x = self.__start_x + self.__cell_size * (col + 1) - self.__cell_margin
            stroke_start_y = self.__start_y - self.__cell_size * row - self.__cell_margin
            self.__pen.goto(stroke_start_x, stroke_start_y)
            self.__pen.pendown()
            self.__pen.left(225)
            self.__pen.forward(stroke_length)
            self.__pen.right(225)
        else:
            self.__pen.penup()
            cicle_center_x = self.__start_x + self.__cell_size * col + self.__cell_size / 2
            cicle_center_y = self.__start_y - self.__cell_size * row - self.__cell_size + self.__cell_margin
            self.__pen.goto(cicle_center_x, cicle_center_y)
            self.__pen.pendown()
            self.__pen.circle(radius=self.__cell_size / 2 - self.__cell_margin)


    def __get_click_col(self, x_coord):
        """Get the column corresponding to the clicked x coordinate"""
        col = -1
        if x_coord > self.__start_x and x_coord < self.__start_x + self.__cell_size:
            col = 0
        elif x_coord > self.__start_x + self.__cell_size and x_coord < self.__start_x + self.__cell_size * 2:
            col = 1
        elif x_coord > self.__start_x + self.__cell_size * 2 and x_coord < self.__start_x + self.__cell_size * 3:
            col = 2
        return col


    def __get_click_row(self, y_coord):
        """Get the row corresponding to the clicked y coordinate"""
        row = -1
        if y_coord < self.__start_y and y_coord > self.__start_y - self.__cell_size:
            row = 0
        elif y_coord < self.__start_y - self.__cell_size and y_coord > self.__start_y - self.__cell_size * 2:
            row = 1
        elif y_coord < self.__start_y - self.__cell_size * 2 and y_coord > self.__start_y - self.__cell_size * 3:
            row = 2
        return row


    def __end_game(self, winner):
        """End the game"""
        end_by_win = winner != -1
        self.__game_is_finished = True
        self.__board = copy.deepcopy(self.__BOARD_DEFAULT)
        self.__taken = copy.deepcopy(self.__TAKEN_DEFAULT)
        self.__turn = 0
        self.__pen.penup()
        self.__pen.goto(self.__start_x - 100, self.__start_y - self.__grid_size * self.__cell_size - self.__cell_size / 2)
        if end_by_win:
            win_message = 'Player ' + str(winner) + ' wins!'
            self.__pen.write(win_message, font=("Arial", 20, "normal"))
        else:
            self.__pen.write('It\'s a tie!', font=("Arial", 20, "normal"))
        self.__pen.pendown()
        self.__pen.penup()
        self.__pen.goto(self.__start_x - 100, self.__start_y - self.__grid_size * self.__cell_size - self.__cell_size)
        self.__pen.pendown()
        self.__pen.write('Click anywhere to play again', font=("Arial Black", 25, "normal"))
        return


    def __register_move(self, x_coord, y_coord):
        """Advance game state"""
        if self.__click_processed:
            self.__click_processed = False
            if self.__game_is_finished:
                self.__pen.clear()
                self.__game_is_finished = False
                self.__click_processed = True
                return

            row = self.__get_click_row(y_coord)
            col = self.__get_click_col(x_coord)

            #Return from function if click is outside the board
            if row == -1 or col == -1 or self.__taken[row][col]:
                self.__click_processed = True
                return
            self.__taken[row][col] = True
            player = 1

            if self.__turn % 2 != 0:
                player = 2
            self.__turn += 1
            self.__board[row][col] = player
            self.__draw_shape(row, col, player)
            winner = -1
            if self.__turn >= 5:
                winner = self.__check_for_winner()
            if winner != -1 or self.__turn >= 9:
                self.__end_game(winner)
            self.__click_processed = True
            return

    def run(self):
        """Run the game"""
        self.__drawer.draw_board()
        turtle.onscreenclick(self.__register_move)
        turtle.done()

if __name__ == '__main__':
    TicTacToe().run()
    