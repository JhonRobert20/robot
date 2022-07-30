from robot.constants import cardinal_directions, all_methods


class RobotMove:

    def __init__(self):
        self.facing = None
        self.x = None
        self.y = None
        self.freedom_of_choice = False
        self.cardinal_directions = cardinal_directions

    def __report(self) -> str:
        if self.freedom_of_choice:
            return f"{self.x}, {self.y}, {self.facing}"
        else:
            return "not in place"

    def __validate_move(self, future_x: int, future_y: int):
        """Validate that the robot is inside an imaginary table"""
        if 0 <= future_x <= 4 and 0 <= future_y <= 4:
            self.x = future_x
            self.y = future_y

    def __move(self):
        """Move forward the robot"""
        if self.freedom_of_choice:
            future_x = self.x
            future_y = self.y
            if self.facing == self.cardinal_directions[3]:
                future_y = self.y - 1
            if self.facing == self.cardinal_directions[0]:
                future_x = self.x - 1
            if self.facing == self.cardinal_directions[2]:
                future_x = self.x + 1
            if self.facing == self.cardinal_directions[1]:
                future_y = self.y + 1

            self.__validate_move(future_x, future_y)

    def __left(self):
        """Change the facing 90 degrees to the left"""
        if self.freedom_of_choice:
            move_to_left = {
                self.cardinal_directions[3]: self.cardinal_directions[2],
                self.cardinal_directions[2]: self.cardinal_directions[1],
                self.cardinal_directions[1]: self.cardinal_directions[0],
                self.cardinal_directions[0]: self.cardinal_directions[3],
            }
            self.facing = move_to_left[self.facing]

    def __right(self):
        """Change the facing 90 degrees to the right"""
        if self.freedom_of_choice:
            move_to_right = {
                self.cardinal_directions[3]: self.cardinal_directions[0],
                self.cardinal_directions[2]: self.cardinal_directions[3],
                self.cardinal_directions[1]: self.cardinal_directions[2],
                self.cardinal_directions[0]: self.cardinal_directions[1],
            }
            self.facing = move_to_right[self.facing]

    def __place(self, x: int, y: int, facing: str):
        """Place the robot in a valid position"""
        if facing.upper() in self.cardinal_directions:
            self.__validate_move(x, y)
            if self.x is not None:
                self.facing = facing.upper()
                self.freedom_of_choice = True

    def call_function(self, function_name, **kwargs):
        """C"""
        function_name = function_name.upper()
        if function_name in all_methods:
            if function_name == all_methods[0]:
                self.__move()
            elif function_name == all_methods[1]:
                self.__place(x=kwargs["x"], y=kwargs["y"], facing=kwargs["facing"])
            if function_name == all_methods[2]:
                self.__right()
            elif function_name == all_methods[3]:
                self.__left()
            elif function_name == all_methods[4]:
                return self.__report()


