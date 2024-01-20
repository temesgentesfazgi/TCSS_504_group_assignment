class MineSweeper:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.output = ""
        self.field_count = 0
        self.rows = 0
        self.cols = 0

    def get_output(self):
        """
        :return: the output
        """
        return self.output

    def write_output(self):
        """
        Writes the output produced to output file created.
        """
        with open(self.output_file, "w", encoding='utf-8') as f:
            f.write(self.output)

    def read_input(self):
        """
        reads the input provided from an input file provided and writes the output
        by calling other function.
        """
        file_name = open(self.input_file, "r")
        while file_name:
            first_line = file_name.readline()
            if first_line == "":
                break
            self.rows, self.cols = (int(val) for val in first_line.split())
            if self.rows == 0 and self.cols == 0:
                break
            if isinstance(self.rows, int) and isinstance(self.cols, int):
                self.field_count += 1
                self.output += f"Field #{self.field_count} :\n"

            single_field = []
            for row in range(self.rows):
                line = file_name.readline().strip()
                field_line = [*line]
                single_field.append(field_line)
            self.check_mine(single_field)
        file_name.close()

    def check_mine(self, single_field):
        for i in range(self.rows):
            for j in range(self.cols):
                if single_field[i][j] == "*":
                    continue
                adjacent = 0
                if single_field[i][j] == ".":
                    if len(single_field[i]) == 1 and len(single_field) == 1:  # in case of single row & col
                        single_field[i][j] == 0
                    elif len(single_field[i]) == 1 and len(single_field) > 1:  # in case of one col
                        if i != len(single_field) - 1:
                            if single_field[i + 1][j] == "*":
                                adjacent += 1
                        else:
                            if single_field[i - 1][j] == "*":
                                adjacent += 1
                    elif len(single_field) == 1 and len(single_field[i]) > 1:  # case of one row
                        if j != len(single_field[i]) - 1:
                            if single_field[i][j + 1] == "*":
                                adjacent += 1
                            else:
                                if single_field[i][j - 1] == "*":
                                    adjacent += 1
                    elif i == 0 and j != 0 and j != len(single_field[i]) - 1: # top row and middle cols
                        if single_field[i][j - 1] == "*":
                            adjacent += 1
                        if single_field[i + 1][j - 1] == "*":
                            adjacent += 1
                        if single_field[i + 1][j] == "*":
                            adjacent += 1
                        if single_field[i + 1][j + 1] == "*":
                            adjacent += 1
                        if single_field[i][j + 1] == "*":
                            adjacent += 1
                    elif i == 0 and j == len(single_field[i]) - 1:  # top row and last col
                        if single_field[i][j - 1] == "*":
                            adjacent += 1
                        if single_field[i + 1][j - 1] == "*":
                            adjacent += 1
                        if single_field[i + 1][j] == "*":
                            adjacent += 1
                    elif j == len(single_field[i]) - 1 and i != 0 \
                            and i != len(single_field) - 1:  # right col and middle rows
                        if single_field[i - 1][j] == "*":
                            adjacent += 1
                        if single_field[i - 1][j - 1] == "*":
                            adjacent += 1
                        if single_field[i][j - 1] == "*":
                            adjacent += 1
                        if single_field[i + 1][j - 1] == "*":
                            adjacent += 1
                        if single_field[i + 1][j] == "*":
                            adjacent += 1
                    elif i == len(single_field) - 1 and j == len(single_field[i]) - 1:  # bottom right corner
                        if single_field[i - 1][j] == "*":
                            adjacent += 1
                        if single_field[i][j - 1] == "*":
                            adjacent += 1
                        if single_field[i - 1][j - 1] == "*":
                            adjacent += 1
                    elif i != 0 and i != len(single_field) - 1 and j == 0:  # left col and middle rows
                        if single_field[i + 1][j] == "*":
                            adjacent += 1
                        if single_field[i + 1][j + 1] == "*":
                            adjacent += 1
                        if single_field[i][j + 1] == "*":
                            adjacent += 1
                        if single_field[i - 1][j + 1] == "*":
                            adjacent += 1
                        if single_field[i - 1][j] == "*":
                            adjacent += 1
                    elif j == 0 and i == len(single_field) - 1:  # bottom left corner
                        if single_field[i - 1][j] == "*":
                            adjacent += 1
                        if single_field[i - 1][j + 1] == "*":
                            adjacent += 1
                        if single_field[i][j + 1] == "*":
                            adjacent += 1
                    elif i == len(single_field) - 1 and j != len(single_field[i]) - 1 \
                            and j != 0:  # bottom row and middle cols
                        if single_field[i - 1][j] == "*":
                            adjacent += 1
                        if single_field[i - 1][j - 1] == "*":
                            adjacent += 1
                        if single_field[i][j + 1] == "*":
                            adjacent += 1
                        if single_field[i - 1][j + 1] == "*":
                            adjacent += 1
                        if single_field[i][j - 1] == "*":
                            adjacent += 1
                    elif i != len(single_field) - 1 and j != len(single_field[i]) - 1 \
                            and j != 0 and i != 0:  # middle rows and middle cols
                        if single_field[i - 1][j] == "*":
                            adjacent += 1
                        if single_field[i - 1][j - 1] == "*":
                            adjacent += 1
                        if single_field[i][j + 1] == "*":
                            adjacent += 1
                        if single_field[i - 1][j + 1] == "*":
                            adjacent += 1
                        if single_field[i][j - 1] == "*":
                            adjacent += 1
                        if single_field[i + 1][j - 1] == "*":
                            adjacent += 1
                        if single_field[i + 1][j] == "*":
                            adjacent += 1
                        if single_field[i + 1][j + 1] == "*":
                            adjacent += 1
                single_field[i][j] = adjacent
        for row in single_field:
            for char in row:
                self.output += str(char)
            self.output += "\n"
        self.output += "\n"


if __name__ == '__main__':
    mine = MineSweeper('minesweeper_input_ya.txt', 'minesweeper_output.txt')
    mine.read_input()
    print(mine.output)
    mine.write_output()




