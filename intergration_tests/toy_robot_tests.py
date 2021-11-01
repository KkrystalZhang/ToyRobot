import main
import unittest

from unittest.mock import patch


class ToyRobotIntegrationTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['MOVE', 'LEFT', 'RIGHT', 'REPORT', 'PLACE 1,1,NORTH', 'REPORT'])
    def test_actions_ignored_until_valid_place(self, mock_input):
        main.main()
        self.assertEqual((1, 1, 'NORTH'), main.robot.get_state())

    @patch('builtins.input', side_effect=['PLACE 4,0,NORTH', 'RIGHT', 'MOVE', 'MOVE', 'MOVE', 'REPORT'])
    def test_valid_actions_state(self, mock_input):
        main.main()
        self.assertEqual((5, 0, 'EAST'), main.robot.get_state())

    @patch('builtins.input', side_effect=['PLACE 0,0,NORTH', 'MOVE', 'LEFT', 'RIGHT', 'REPORT'])
    def test_falling_actions_ignored(self, mock_input):
        main.main()
        self.assertEqual((0, 1, 'NORTH'), main.robot.get_state())

    @patch('builtins.input', side_effect=['PLACE 1,1,NORTH', 'RIGHT', 'MOVE', 'MOVE', 'PLACE 4,0,NORTH', 'REPORT'])
    def test_actions_with_multiple_place(self, mock_input):
        main.main()
        self.assertEqual((4, 0, 'NORTH'), main.robot.get_state())

    @patch('builtins.input', side_effect=[
        'PLACE 4,0,NORTH', 'RIGHT', 'MOVE', 'MOVE', 'MOVE', 'PLACE 1,1,NORTH', 'REPORT'])
    def test_falling_actions_and_place(self, mock_input):
        main.main()
        self.assertEqual((1, 1, 'NORTH'), main.robot.get_state())

    @patch('builtins.input', side_effect=['PLACE 0,0,NORTH', 'JUMP', 'WRONG', 'MOVE', 'REPORT'])
    def test_invalid_inputs_ignored(self, mock_input):
        main.main()
        self.assertEqual((0, 1, 'NORTH'), main.robot.get_state())
