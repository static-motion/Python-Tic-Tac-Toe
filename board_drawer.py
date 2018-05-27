"""Game board and title drawer for ttt.py"""
import turtle

class Drawer():
    """Board drawer class"""
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.__pen_size = 5
        self.__speed = 7
        self.__cell_size = 100
        self.__grid_size = 3
        self.__drawer = turtle.Turtle()
        self.__drawer.hideturtle()
        self.__drawer.pensize(self.__pen_size)
        self.__drawer.speed(self.__speed)


    @staticmethod
    def __check_x_y(x_coord, y_coord):
        if not isinstance(x_coord, int) or not isinstance(y_coord, int):
            raise ValueError("The starting coordinates for the board drawer need to be of type int")

    def change_speed(self, speed):
        """Change drawer speed"""
        if not isinstance(speed, int) or speed <= 0:
            raise ValueError('Speed value must be an integer larger than 0.')

        self.__drawer.speed(speed)
        self.__speed = speed


    def get_speed(self):
        """Get current drawer speed"""
        return self.__speed

    def draw_board(self, alt=False):
        """Draw the board - the title and the grid"""
        self.draw_title()
        if alt:
            self.draw_grid_alt()
        else:
            self.draw_grid()


    def draw_grid_alt(self):
        """Alternative grid drawing style"""

        for i in range(1, self.__grid_size * self.__grid_size + 1):
            for mov in range(self.__grid_size + 1):
                self.__drawer.forward(self.__cell_size)
                self.__drawer.right(90)

            self.__drawer.goto(self.__drawer.xcor() + self.__cell_size, self.__drawer.ycor())

            if i % self.__grid_size == 0:
                self.__drawer.penup()
                new_line_x = self.__drawer.xcor() - self.__cell_size * self.__grid_size
                new_line_y = self.__drawer.ycor() - self.__cell_size
                self.__drawer.goto(new_line_x, new_line_y)
                self.__drawer.pendown()


    def draw_title(self):
        """Draw the board title"""
        self.__drawer.penup()
        self.__drawer.goto(self.start_x - 75, self.start_y + 60)
        self.__drawer.write('TIC TAC TOE', move=True, font=("Arial Black", 50, "normal"))
        self.__drawer.penup()
        self.__drawer.goto(self.start_x, self.start_y)
        self.__drawer.pendown()


    def draw_grid(self):
        """Draw the game board(grid)"""

        #Vertical lines
        self.__drawer.right(90)
        for vertical in range(0, self.__grid_size + 1):
            self.__drawer.penup()
            self.__drawer.goto(self.start_x + self.__cell_size * vertical, self.start_y)
            self.__drawer.pendown()
            self.__drawer.forward(self.__grid_size * self.__cell_size)

        #horizontal lines
        self.__drawer.left(90)
        for horizontal in range(0, self.__grid_size + 1):
            self.__drawer.penup()
            self.__drawer.goto(self.start_x, self.start_y - self.__cell_size * horizontal)
            self.__drawer.pendown()
            self.__drawer.forward(self.__grid_size * self.__cell_size)

    def pen_size(self, size):
        """Change drawer pen size"""
        if not isinstance(size, int):
            raise ValueError("pen_size expected int but %s was passed as argument" % (type(size)))

        self._pen_size = size
