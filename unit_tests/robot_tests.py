import unittest

from robot import Robot


class RobotUnitTests(unittest.TestCase):

    robot = None

    @classmethod
    def setUp(self):
        self.robot = Robot()

    def test_valid_check(self):
        self.assertFalse(self.robot.valid())

        self.robot.x, self.robot.y, self.robot.direction = None, 0, 'NORTH'
        self.assertFalse(self.robot.valid())

        self.robot.x, self.robot.y, self.robot.direction = 0, 6, 'NORTH'
        self.assertFalse(self.robot.valid())

        self.robot.x, self.robot.y, self.robot.direction = -1, 0, 'NORTH'
        self.assertFalse(self.robot.valid())

        self.robot.x, self.robot.y, self.robot.direction = 0, 0, 'CENTRE'
        self.assertFalse(self.robot.valid())

        self.robot.x, self.robot.y, self.robot.direction = 0, 0, None
        self.assertFalse(self.robot.valid())

        self.robot.x, self.robot.y, self.robot.direction = 2, 3, 'NORTH'
        self.assertTrue(self.robot.valid())

    def test_place_valid(self):
        self.robot.place(0, 0, 'NORTH')

        self.assertTrue(self.robot.valid())
        self.assertEqual((0, 0, 'NORTH'), self.robot.get_state())

    def test_place_invalid(self):
        self.robot.place(0, 9, 'NORTH')

        self.assertFalse(self.robot.valid())
        self.assertEqual((None, None, None), self.robot.get_state())

    def test_move_without_place(self):
        self.robot.move()

        self.assertFalse(self.robot.valid())
        self.assertEqual((None, None, None), self.robot.get_state())

    def test_move_with_valid_place(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.move()

        self.assertTrue(self.robot.valid())
        self.assertEqual((0, 1, 'NORTH'), self.robot.get_state())

    def test_move_out_of_grid(self):
        self.robot.place(5, 5, 'NORTH')
        self.robot.move()

        self.assertTrue(self.robot.valid())
        self.assertEqual((5, 5, 'NORTH'), self.robot.get_state())

    def test_turn_left_without_place(self):
        self.robot.left()

        self.assertFalse(self.robot.valid())
        self.assertEqual((None, None, None), self.robot.get_state())

    def test_turn_left_with_valid_place(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()

        self.assertTrue(self.robot.valid())
        self.assertEqual((0, 0, 'WEST'), self.robot.get_state())

    def test_turn_right_without_place(self):
        self.robot.right()

        self.assertFalse(self.robot.valid())
        self.assertEqual((None, None, None), self.robot.get_state())

    def test_turn_right_with_valid_place(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()

        self.assertTrue(self.robot.valid())
        self.assertEqual((0, 0, 'EAST'), self.robot.get_state())
