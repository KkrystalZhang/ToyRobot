from grid import Grid
from utils import DIRECTIONS, MOVES


class Robot(object):
    """
    The Robot class contains state of the robot and methods to update the state.
    """
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None

    def place(self, x: int, y: int, direction: DIRECTIONS):
        """
        Place the robot at the specified position.

        Attributes:
            x (int): x coordination value.
            y (int): y coordination value.
            direction (DIRECTIONS): facing direction.
        """
        if Grid.valid_position(x, y) and Grid.valid_direction(direction):
            self.x, self.y, self.direction = x, y, direction

    def move(self):
        """
        Move the robot a step forward against the facing direction.
        """
        if self.valid():
            delta = MOVES[self.direction]
            new_x = self.x + delta[0]
            new_y = self.y + delta[1]
            if Grid.valid_position(new_x, new_y):
                self.x = new_x
                self.y = new_y

    def left(self):
        """
        Change the facing direction counterclockwise by 90 degree.
        """
        if self.valid():
            current_index = DIRECTIONS.index(self.direction)
            self.direction = DIRECTIONS[current_index - 1]

    def right(self):
        """
        Change the facing direction clockwise by 90 degree.
        """
        if self.valid():
            current_index = DIRECTIONS.index(self.direction)
            self.direction = DIRECTIONS[(current_index + 1) % 4]

    def report(self):
        """
        Print the current state of the robot.
        """
        if self.valid():
            print(f'Output: {self.x},{self.y},{self.direction}')

    def valid(self):
        """
        Check if current state of the robot is valid against the grid.

        Returns:
            boolean
        """
        return Grid.valid_position(self.x, self.y) and Grid.valid_direction(self.direction)

    def get_state(self) -> (int, int, DIRECTIONS):
        """
        Get current state of the robot.

        Returns:
            x, y, direction
        """
        return self.x, self.y, self.direction
