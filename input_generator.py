import random


class InputGenerator:
    def __init__(self, output_file):
        self.output_file = output_file
        self.output = ""

    def get_output(self):
        return self.output

    def input_generator(self):
        row = int(input("How many rows do you want the field to have? "))
        col = int(input("How many columns do you want the field to have? "))
        chance = float(input("Give the probability of the mine in the field (a decimal number): "))
        item_chances = [chance, 1 - chance]
        items = ["mine", "no_mine"]
        field_line = ""
        for i in range(row):
            field_col = ""
            for j in range(col):
                mine_success = random.choices(items, item_chances)
                if mine_success == ["mine"]:
                    field_col += "*"
                else:
                    field_col += "."
            field_line += f"{field_col}\n"

        self.output += f"{row} {col}\n"
        self.output += field_line

    def random_generator(self):
        row = random.randint(1, 100)
        col = random.randint(1, 100)
        field_line = ""
        for i in range(row):
            field_col = ""
            for j in range(col):
                if random.choice([True, False]):
                    field_col += "*"
                else:
                    field_col += "."
            field_line += f"{field_col}\n"

        self.output += f"{row} {col}\n"
        self.output += field_line

    def mine_fields_generator(self, n):
        for i in range(n):
            self.random_generator()

    def ending_input(self):
        self.output += f"0 0\n"

    def write_output(self):
        with open(self.output_file, "w", encoding='utf-8') as f:
            f.write(self.output)


if __name__ == "__main__":
    generator = InputGenerator("minesweeper_input.txt")
    generator.input_generator()
    # generator.mine_fields_generator(3)
    generator.ending_input()
    generator.write_output()
    print(generator.output)
