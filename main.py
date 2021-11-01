import re

from robot import Robot
from utils import ACTIONS

robot = Robot()


def main():
    place_regex = re.compile('^PLACE [0-5],[0-5],(NORTH|SOUTH|WEST|EAST)$')

    while True:
        command = input()

        if place_regex.match(command):
            inputs = command.split(' ')
            position_values = inputs[1].split(',')
            x, y, facing = int(position_values[0]), int(position_values[1]), position_values[2]

            robot.place(x, y, facing)
        elif robot.valid() and command in ACTIONS:
            getattr(robot, command.lower())()
            if command == 'REPORT':
                break


if __name__ == '__main__':
    main()
