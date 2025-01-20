from copy import deepcopy
from texttable import Texttable
import unittest
from unittest import TestCase


class Grid:

    def __init__(self):
        self.data = [[" ", " ", " ", " ", " ", " ", " ", " "] for i in range(8)]

    def __str__(self):
        self.table = Texttable()
        self.table.add_rows(self.data, [])
        return self.table.draw()

    def change_board(self):
        """
        Output: no return, the data of the board is changed accordingly to the rules stated
        the neighbours are checked and based on their values the new board is created
        """
        data = deepcopy(self.data)
        for i in range(8):
            for j in range(8):
                alive = 0
                dead = 0
                if i - 1 >= 0 and j - 1 >= 0:
                    if data[i - 1][j - 1] == "X":
                        alive += 1
                    else:
                        dead += 1
                if i - 1 >= 0:
                    if data[i - 1][j] == "X":
                        alive += 1
                    else:
                        dead += 1
                if j - 1 >= 0:
                    if data[i][j - 1] == "X":
                        alive += 1
                    else:
                        dead += 1
                if i + 1 < 8 and j + 1 < 8:
                    if data[i + 1][j + 1] == "X":
                        alive += 1
                    else:
                        dead += 1
                if i + 1 < 8:
                    if data[i + 1][j] == "X":
                        alive += 1
                    else:
                        dead += 1
                if j + 1 < 8:
                    if data[i][j + 1] == "X":
                        alive += 1
                    else:
                        dead += 1
                if i - 1 >= 0 and j + 1 < 8:
                    if data[i - 1][j + 1] == "X":
                        alive += 1
                    else:
                        dead += 1
                if i + 1 < 8 and j - 1 >= 0:
                    if data[i + 1][j - 1] == "X":
                        alive += 1
                    else:
                        dead += 1
                if data[i][j] == "X":
                    if alive > 3 or alive < 2:
                        self.data[i][j] = " "
                if data[i][j] == " ":
                    if alive == 3:
                        self.data[i][j] = "X"

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            i = 0
            for line in lines:
                for j in range(8):
                    if line[j] == "-":
                        self.data[i][j] = " "
                    elif line[j] == "X":
                        self.data[i][j] = "X"
                i += 1
        f.close()

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            for line in self.data:
                for elem in line:
                    if elem == " ":
                        f.write("-")
                    else:
                        f.write(elem)
                f.write("\n")
        f.close()

    def read_pattern(self, filename):
        """
        return: a list containing the patterns and their data
        The function reads the pattern from Pattern.txt and creates a list with
        the name of the pattern and its data
        """
        pattern = []
        with open(filename, "r") as f:
            lines = f.readlines()
            newlines = []
            for line in lines:
                newline = line.strip()
                newlines.append(newline)
            lines = newlines
            for i in range(len(lines)):
                if lines[i] == "block":
                    blockdata = []
                    line = [lines[i+1][0], lines[i+1][1]]
                    blockdata.append(line)
                    line = [lines[i + 2][0], lines[i + 2][1]]
                    blockdata.append(line)
                    pattern.append("block")
                    pattern.append(blockdata)
                if lines[i] == "tub":
                    tub_data = []
                    line = [lines[i + 1][0], lines[i + 1][1], lines[i + 1][2]]
                    tub_data.append(line)
                    line = [lines[i + 2][0], lines[i + 2][1], lines[i + 2][2]]
                    tub_data.append(line)
                    line = [lines[i + 3][0], lines[i + 3][1], lines[i + 3][2]]
                    tub_data.append(line)
                    pattern.append("tub")
                    pattern.append(tub_data)
                if lines[i] == "blinker":
                    blinker_data = []
                    line = [lines[i + 1][0], lines[i + 1][1], lines[i + 1][2]]
                    blinker_data.append(line)
                    line = [lines[i + 2][0], lines[i + 2][1], lines[i + 2][2]]
                    blinker_data.append(line)
                    line = [lines[i + 3][0], lines[i + 3][1], lines[i + 3][2]]
                    blinker_data.append(line)
                    pattern.append("blinker")
                    pattern.append(blinker_data)
                if lines[i] == "beacon":
                    beacon_data = []
                    line = [lines[i + 1][0], lines[i + 1][1], lines[i + 1][2], lines[i + 1][3]]
                    beacon_data.append(line)
                    line = [lines[i + 2][0], lines[i + 2][1], lines[i + 2][2], lines[i + 2][3]]
                    beacon_data.append(line)
                    line = [lines[i + 3][0], lines[i + 3][1], lines[i + 3][2], lines[i + 3][3]]
                    beacon_data.append(line)
                    line = [lines[i + 4][0], lines[i + 4][1], lines[i + 4][2], lines[i + 4][3]]
                    beacon_data.append(line)
                    pattern.append("beacon")
                    pattern.append(beacon_data)
                if lines[i] == "spaceship":
                    spaceship_data = []
                    line = [lines[i + 1][0], lines[i + 1][1], lines[i + 1][2], lines[i + 1][3]]
                    spaceship_data.append(line)
                    line = [lines[i + 2][0], lines[i + 2][1], lines[i + 2][2], lines[i + 2][3]]
                    spaceship_data.append(line)
                    line = [lines[i + 3][0], lines[i + 3][1], lines[i + 3][2], lines[i + 3][3]]
                    spaceship_data.append(line)
                    line = [lines[i + 4][0], lines[i + 4][1], lines[i + 4][2], lines[i + 4][3]]
                    spaceship_data.append(line)
                    pattern.append("spaceship")
                    pattern.append(spaceship_data)
        f.close()
        return pattern


class Tests(TestCase):
    def test_grid_tick(self):
        grid = Grid()
        grid.data[3][3] = "X"
        grid.data[3][4] = "X"
        grid.data[4][3] = "X"
        grid.data[4][4] = "X"
        grid.change_board()
        assert grid.data[3][3] == "X"
        assert grid.data[3][4] == "X"
        assert grid.data[4][3] == "X"
        assert grid.data[4][4] == "X"

    def test_grade_tick_tub(self):
        grid = Grid()
        grid.data[1][1] = " "
        grid.data[1][2] = "X"
        grid.data[1][3] = " "
        grid.data[2][1] = "X"
        grid.data[2][2] = " "
        grid.data[2][3] = "X"
        grid.data[3][1] = " "
        grid.data[3][2] = "X"
        grid.data[3][3] = " "
        assert grid.data[1][2] == "X"
        assert grid.data[2][1] == "X"
        assert grid.data[2][3] == "X"
        assert grid.data[3][2] == "X"
        assert grid.data[2][2] == " "

    def test_grade_tick_blinker(self):
        grid = Grid()
        grid.data[1][1] = " "
        grid.data[1][2] = " "
        grid.data[1][3] = " "
        grid.data[2][1] = "X"
        grid.data[2][2] = "X"
        grid.data[2][3] = "X"
        grid.data[3][1] = " "
        grid.data[3][2] = " "
        grid.data[3][3] = " "
        assert grid.data[1][2] == " "
        assert grid.data[2][1] == "X"
        assert grid.data[2][3] == "X"
        assert grid.data[3][2] == " "
        assert grid.data[2][2] == "X"

    def test_grid_place(self):
        grid = Grid()
        patterns = grid.read_pattern("Pattern.txt")
        assert "block" in patterns
        assert [["X", "X"], ["X", "X"]] in patterns
        assert [["X", "X"], ["X", " "]] not in patterns
        assert "tub" in patterns
        assert "blinker" in patterns
        assert "beacon" in patterns
        assert "spaceship" in patterns
        assert [[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]] not in patterns


if __name__ == '__main__':
    unittest.main()
