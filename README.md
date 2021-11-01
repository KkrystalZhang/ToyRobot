# Toy Robot
**Author:** Krystal Zhang

**Email:** zkkrystal1121@gmail.com

**Github:** https://github.com/KkrystalZhang/ToyRobot

## Structure
### Main
Contains the logic to interact with user input to move and report position of the robot. The program takes input from standard console input, ignores all commands until a valid PLACE command is provided and all subsequent invalid commands or commands causing the robot to fall.
* [main.py](main.py)
### Models
Contains models of object involved in the toy robot simulation.
* [grid.py](grid.py)
* [robot.py](robot.py)
### Tests
Unit tests to test the fuctionalities of models and end-to-end integration tests to test the correctness of moves and robustness agsinst user inputs.
* [grid_tests.py](unit_tests/grid_tests.py)
* [robot_tests.py](unit_tests/robot_tests.py)
* [toy_robot_tests.py](integration_tests/toy_robot_tests.py)

## Setups
### Main
The program requires Python 3.3+ with no dependency on 3rd-party libraries, run
```sh
python main.py
```
from the root directory of the project in your venv if any.
### Tests
The program uses Python standard unittest.
Unit tests against models can be run from the project root directory by
```sh
python unit_tests_main.py
```
Integration tests can be run by
```sh
python integration_tests_main.py
```

