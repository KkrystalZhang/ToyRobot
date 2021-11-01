from utils import DIRECTIONS


class Grid(object):
    """
    The Grid class contains properties and static methods of the grid.
    """
    DIM_X = 5
    DIM_Y = 5

    @staticmethod
    def valid_position(x: int, y: int):
        """
        Check if the provided coordination is valid.

        Attributes:
            x (int): x coordination value.
            y (int): y coordination value.

        Returns:
            boolean
        """
        return x in range(0, Grid.DIM_X + 1) and y in range(0, Grid.DIM_Y + 1)

    @staticmethod
    def valid_direction(direction: DIRECTIONS):
        """
        Check if the provided direction is valid.

        Attributes:
            direction : direction value.

        Returns:
            boolean
        """
        return direction in DIRECTIONS
