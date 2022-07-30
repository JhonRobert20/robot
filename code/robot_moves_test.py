import unittest
from robot.robot_move import RobotMove


class MyTestCase(unittest.TestCase):
    def test_data_1(self):
        robot_move = RobotMove()
        robot_move.call_function("move")
        robot_move.call_function("left")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "not in place")

    def test_data_2(self):
        robot_move = RobotMove()
        robot_move.call_function("place", x=1, y=2, facing="NORTH")
        self.assertEqual(robot_move.call_function("report"), "1, 2, NORTH")

    def test_data_3(self):
        robot_move = RobotMove()
        robot_move.call_function("place", x=9, y=9, facing="North")
        self.assertEqual(robot_move.call_function("report"), "not in place")

    def test_data_4(self):
        robot_move = RobotMove()
        robot_move.call_function("place", x=1, y=1, facing="north")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "1, 1, EAST")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "1, 1, SOUTH")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "1, 1, WEST")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "1, 1, NORTH")

    def test_data_5(self):
        robot_move = RobotMove()
        robot_move.call_function("place", x=1, y=1, facing="NORTH")
        robot_move.call_function("left")
        self.assertEqual(robot_move.call_function("report"), "1, 1, WEST")
        robot_move.call_function("left")
        self.assertEqual(robot_move.call_function("report"), "1, 1, SOUTH")
        robot_move.call_function("left")
        self.assertEqual(robot_move.call_function("report"), "1, 1, EAST")
        robot_move.call_function("left")
        self.assertEqual(robot_move.call_function("report"), "1, 1, NORTH")

    def test_data_6(self):
        robot_move = RobotMove()
        robot_move.call_function("place", x=1, y=1, facing="NORTH")
        robot_move.call_function("move")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "1, 2, EAST")
        robot_move.call_function("move")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "2, 2, SOUTH")
        robot_move.call_function("move")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "2, 1, WEST")
        robot_move.call_function("move")
        robot_move.call_function("right")
        self.assertEqual(robot_move.call_function("report"), "1, 1, NORTH")

    def test_data_7(self):
        robot_move = RobotMove()
        robot_move.call_function("place", x=4, y=4, facing="NORTH")
        robot_move.call_function("move")
        robot_move.call_function("move")
        robot_move.call_function("move")
        robot_move.call_function("move")
        robot_move.call_function("move")
        self.assertEqual(robot_move.call_function("report"), "4, 4, NORTH")

    def test_data_8(self):
        robot_move = RobotMove()
        robot_move.call_function("AUTODESTRUCT")
        robot_move.call_function("TAKEOFF")
        robot_move.call_function("KILL")
        self.assertEqual(robot_move.call_function("report"), "not in place")


if __name__ == '__main__':
    unittest.main()
