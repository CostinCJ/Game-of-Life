from domain import Grid
from copy import deepcopy


class UI:

    def __init__(self):
        self.grid = Grid()

    def save(self, filename):
        self.grid.write_to_file(filename)

    def load(self, filename):
        self.grid.read_from_file(filename)

    def tick(self, param):
        if param.isdigit():
            prm = int(param)
            for i in range(prm):
                self.grid.change_board()
        else:
            print("The parameter is not a digit!")

    def read_command(self):
        cmd = input("Please type your command: ")
        cmd = cmd.split(" ", 1)

        if cmd[0] == "exit":
            return False

        if cmd[0] == "tick":
            if len(cmd) == 1:
                self.tick('1')
                return True
            else:
                self.tick(cmd[1])
                return True
        elif cmd[0] == "place":
            self.place(cmd[1])
            return True
        elif cmd[0] == "save":
            self.save(cmd[1])
            return True
        elif cmd[0] == "load":
            self.load(cmd[1])
            return True
        else:
            print("Wrong command!")
            return True

    def place(self, params):
        """
        This function places a pattern on the board
        :param params: this is the pattern and the coordinates where it will be placed
        """
        old_data = deepcopy(self.grid.data)
        patterns = self.grid.read_pattern("Pattern.txt")
        parameters = params.split()
        if len(parameters) != 2:
            print("Wrong format for command!")
            return
        if len(parameters[1]) != 3:
            print("Wrong format for command!")
            return
        if parameters[1][1] != ",":
            print("Wrong format for command!")
            return
        if parameters[1][0].isdigit() and parameters[1][2].isdigit():
            x = int(parameters[1][0])
            y = int(parameters[1][2])
            if x > 7 or y > 7:
                print("Outside the board!")
                return
            if parameters[0] in patterns:
                for i in range(len(patterns)):
                    if patterns[i] == parameters[0]:
                        for j in range(len(patterns[i + 1])):
                            for k in range(len(patterns[i + 1][j])):
                                if patterns[i + 1][j][k] == "X":
                                    if x + j > 7 or y + k > 7:
                                        print("Outside the board!!")
                                        self.grid.data = old_data
                                        return
                                    if self.grid.data[x + j][y + k] == "X":
                                        print("Life cells can not overlap!")
                                        self.grid.data = old_data
                                        return
                                    else:
                                        self.grid.data[x + j][y + k] = patterns[i + 1][j][k]
                                if patterns[i + 1][j][k] == "+":
                                    if x + j > 7 or y + k > 7:
                                        print("Outside the board!!")
                                        self.grid.data = old_data
                                        return
                                    if self.grid.data[x + j][y + k] == "X":
                                        print("Life cells can not overlap!")
                                        self.grid.data = old_data
                                        return
                                    self.grid.data[x + j][y + k] = " "
            else:
                print("No such pattern!")
        else:
            print("Parameters are not integers!")

    def main(self):

        print(self.grid)
        r = self.read_command()
        while True:
            if r:
                print(self.grid)
                r = self.read_command()
            else:
                break


ui = UI()
ui.main()
