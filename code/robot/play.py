from robot.constants import options, input_place_text, input_options_text
from robot.robot_move import RobotMove


def play_with_robot():
    robot_move = RobotMove()
    while True:
        option = input(input_options_text).upper()
        if option in options:
            if option == options[0]:
                robot_move.call_function("move")
            if option == options[1]:
                arguments_input = input(
                    input_place_text
                )
                arguments = arguments_input.replace(" ", "").split(',')
                if len(arguments) == 3:
                    x = arguments[0]
                    y = arguments[1]
                    if x.isnumeric() and y.isnumeric():
                        robot_move.call_function(
                            "place", x=int(x), y=int(y), facing=arguments[2]
                        )
            if option == options[2]:
                robot_move.call_function("right")
            if option == options[3]:
                robot_move.call_function("left")
            if option == options[4]:
                print(robot_move.call_function("REPORT"))
            if option == options[5]:
                break
