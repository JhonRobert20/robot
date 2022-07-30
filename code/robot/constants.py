cardinal_directions = ["WEST", "NORTH", "EAST", "SOUTH"]
all_methods = ["MOVE", "PLACE", "RIGHT", "LEFT",  "REPORT"]
options = all_methods.copy()
options.append("EXIT")
input_place_text = (
    "place(x: int, y: int, facing: str). \n"
    "The x and y must be "
    "equal or higher than zero and must be lower or equal than five. \n"
    "The facing must be one of the following "
    f"values: {', '.join(cardinal_directions)} \n"
    "Separated by commas: "
)
input_options_text = f"Select options: \n{', '.join(options)}: "

