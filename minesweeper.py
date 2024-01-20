import sys

def count_adjacent_mines(field, i, j, n, m):
    """
    Count the number of adjacent mines to a given cell in the Minesweeper field.

    Parameters:
    - field: List of strings representing the Minesweeper field.
    - i, j: Coordinates of the cell for which adjacent mines are counted.
    - n, m: Dimensions of the Minesweeper field.

   directions: List of tuples representing the possible directions of adjacent cells in a grid.Each tuple (di, dj)
   corresponds to the change in row (di) and column (dj) coordinates to reach an adjacent cell.
   The eight tuples cover all possible adjacent cells, including diagonals and horizontally/vertically adjacent cells.

    Returns:
    - count: Number of adjacent mines to the specified cell.
    """

    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == '*':
            count += 1

    return count


def solve_minesweeper(entry):
    """
    This method processes each Minesweeper field and prints the solved result.

    Parameters:
    - field: List representing a Minesweeper field. The first element contains the dimensions,
             and the subsequent elements represent rows of the field.

    The loop iterates over each Minesweeper field in the provided 'entry', solves the Minesweeper game,
    and prints the results to the standard output.

    It prints an empty line between the outputs of consecutive fields and displays the field number along with the solved grid.

    The solved grid consists of numbers representing the count of adjacent mines for each cell, and mines are represented by "*".

    """

    field_number = 1

    for field in entry:
        n, m = map(int, field[0].split())
        if n == 0 and m == 0:
            break

        if field_number > 1:
            print()  # Empty line between field outputs

        print(f"Field #{field_number}:")
        field_number += 1

        for i in range(n):
            for j in range(m):
                if field[i + 1][j] == '*':
                    print("*", end="")
                else:
                    adjacent_mines = count_adjacent_mines(field[1:], i, j, n, m)
                    print(adjacent_mines, end="")
            print()  # Move to the next line


if __name__ == "__main__":
    """
       Reads Minesweeper fields from the mines input file, solves the game, and prints the results to the minesweeper output file.

       Input:
       - Reads Minesweeper fields from the file specified by 'input_filename' ("mines.txt").
         Each field in the file is represented by its dimensions followed by the grid of cells.

       Output:
       - Prints the solved Minesweeper fields to the file specified by 'output_filename' ("minesweeper_output.txt").

       """
    input_filename = "mines.txt"
    output_filename = "minesweeper_output.txt"

    with open(input_filename, "r") as infile:
        fields = []
        while True:
            # Read the dimensions of the Minesweeper field
            n, m = map(int, infile.readline().split())
            if n == 0 and m == 0:
                break

            # Read the current Minesweeper field
            current_field = [infile.readline().strip() for _ in range(n)]
            fields.append([f"{n} {m}"] + current_field)

    # Outputs to minesweeper_output.txt
    with open(output_filename, "w") as outfile:
        original_stdout = sys.stdout
        sys.stdout = outfile

        # Solve and print Minesweeper fields
        solve_minesweeper(fields)

        sys.stdout = original_stdout
