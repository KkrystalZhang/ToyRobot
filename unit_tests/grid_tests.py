import unittest
from unittest.mock import patch

from grid import Grid


class GridUnitTests(unittest.TestCase):
    @patch('builtins.input', side_effect=((0, 0), (5, 5), (0, 5), (5, 0), (1, 1), (2, 2)))
    def test_valid_position(self, mock_input):
        for _ in range(6):
            x, y = mock_input()
            self.assertTrue(Grid.valid_position(x, y))

    @patch('builtins.input', side_effect=((-1, 0), (6, 0), (0, -1), (0, 6), (6, 6), (-1, -1), (None, None)))
    def test_invalid_position(self, mock_input):
        for _ in range(7):
            x, y = mock_input()
            self.assertFalse(Grid.valid_position(x, y))

    @patch('builtins.input', side_effect=('NORTH', 'SOUTH', 'WEST', 'EAST'))
    def test_valid_direction(self, mock_input):
        for _ in range(4):
            direction = mock_input()
            self.assertTrue(Grid.valid_direction(direction))

    @patch('builtins.input', side_effect=('CENTRE', 1, None))
    def test_invalid_direction(self, mock_input):
        for _ in range(3):
            direction = mock_input()
            self.assertFalse(Grid.valid_direction(direction))
