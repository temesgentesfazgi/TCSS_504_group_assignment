import random

def generate_mines_field(n, m, mine_density=0.2):
    """
    Generates a Minesweeper field with random mines.

    Parameters:
    - n, m: Dimensions of the Minesweeper field.
    - mine_density: Probability of a cell containing a mine.

    Returns:
    - field: List representing the Minesweeper field.
    """
    field = []

    # Generate random Minesweeper field
    for _ in range(n):
        row = ''.join(['*' if random.random() < mine_density else '.' for _ in range(m)])
        field.append(row)

    return [f"{n} {m}"] + field

def generate_mines_file(filename, num_fields=5, max_dimension=10):
    """
    Generates a Minesweeper file with multiple fields.

    Parameters:
    - filename: Output file name.
    - num_fields: Number of Minesweeper fields to generate.
    - max_dimension: Maximum dimension for each field.

    Writes the generated fields to the specified file.
    """
    with open(filename, 'w') as file:
        for _ in range(num_fields):
            n, m = random.randint(1, max_dimension), random.randint(1, max_dimension)
            field = generate_mines_field(n, m)
            for line in field:
                file.write(line + '\n')

if __name__ == "__main__":
    generate_mines_file("minesweeper_input_ya.txt", num_fields=55, max_dimension=50)
