# Game-of-Life
This project is a Python implementation of a Game of Life simulator, featuring a user interface for interacting with the grid and managing patterns. It combines core principles of Game of Life with additional functionality for saving, loading, and placing predefined patterns on an 8x8 grid. Below is a detailed description of its components and features.

Interactive Command-Line Interface:
The program includes a UI class that allows users to interact with the game through commands like:
tick [n]: Advances the simulation by n steps (default is 1 if no parameter is provided).
place [pattern_name x,y]: Places a predefined pattern (e.g., "block", "blinker") at specified coordinates.
save [filename]: Saves the current grid state to a file.
load [filename]: Loads a grid state from a file.
exit: Exits the program.

Grid Simulation:
The Grid class implements the logic for Game of Life:
Each cell can either be alive (X) or dead ( ).
The state of each cell is updated based on its neighbors, following the rules:
A live cell with fewer than 2 or more than 3 neighbors dies.
A dead cell with exactly 3 neighbors becomes alive.
The grid state is updated using the change_board method.

Pattern Management:
Patterns are defined in an external file (Pattern.txt) and include shapes like:
Block: A stable 2x2 square.
Tub: A static shape resembling a tub.
Blinker: A simple oscillator.
Beacon: A larger oscillator.
Spaceship: A moving pattern.
The place command allows users to position these patterns on the grid while ensuring they do not overlap or exceed boundaries.

File Operations:
Users can save the grid state to a file (grid.txt) and reload it later using the save and load commands.
Patterns are read from Pattern.txt, enabling easy customization or addition of new patterns.
Error Handling:
The program includes checks for invalid inputs, such as out-of-bounds coordinates, overlapping cells, or unrecognized patterns.
Testing:
Unit tests are provided to validate key functionalities, including pattern placement, grid updates, and pattern recognition.

How It Works
The game starts with an empty 8x8 grid initialized by the Grid class.
Users interact with the game through commands entered into the terminal.
Predefined patterns can be placed on the grid, and users can simulate generations using the tick command.
The grid evolves according to the rules, creating dynamic and visually interesting patterns.

This project showcases several important programming concepts:
Object-Oriented Design: Classes like Grid and UI encapsulate functionality for modularity and scalability.
File I/O Operations: Reading from and writing to files for saving/loading game states and patterns.
Algorithm Implementation: Simulating Game of Life rules efficiently on an 8x8 grid.
Error Handling: Managing invalid inputs gracefully to ensure smooth user interaction.
Unit Testing: Validating core functionalities using Python's unittest framework.
