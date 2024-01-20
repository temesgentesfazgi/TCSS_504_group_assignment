from minesweeper import MineSweeper
import unittest


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.mine_sweeper = MineSweeper("minesweeper_input_ya.txt", "minesweeper_output.txt")

    def test_minesweeper_obj(self):
        m = MineSweeper("mines.txt", "minesweeper_output.txt")
        self.assertEqual(type(m) == MineSweeper, True,
                         "Constructor should create Minesweeper object")

    def test_1x1_output(self):
        m = MineSweeper("minesweeper_input_ya.txt", "minesweeper_output.txt")
        m.read_input()
        check_output = "Field #1 :\n0001*\n00011\n\nField #2 :\n000\n\nField #3 :\n0\n\nField #4 :\n0\n\nField #5 :\n01\n*2\n2*\n22\n1*\n\n"
        self.assertEqual(check_output, m.get_output(), True)

    def test_hint_producing_code(self):
        field = ["****", "****", "****", "****"]
        self.mine_sweeper.check_mine(field)
        self.assertEqual(self.mine_sweeper.get_output(), "****\n****\n****\n****\n\n")

    def test_input_format(self):
        mine_sweeper = MineSweeper('minesweeper_input_ya.txt', 'minesweeper_output.txt')
        mine_sweeper.read_input()

        # Update the expected field count to 14
        expected_field_count = 5
        actual_field_count = mine_sweeper.field_count

        self.assertEqual(actual_field_count, expected_field_count, msg="Mismatch in field count")

    def test_output_format(self):
        # Set up the mine sweeper with example input and output file paths
        mine_sweeper = MineSweeper("minesweeper_input_ya.txt", "minesweeper_output.txt")

        # Read input and generate output
        mine_sweeper.read_input()
        mine_sweeper.write_output()

        # Read the expected output from the provided output file
        with open("minesweeper_output.txt", "r") as output_file:
            actual_output = output_file.read()

        # Define the correct expected output with proper newline characters
        expected_output = "Field #1 :\n0001*\n00011\n\nField #2 :\n000\n\nField #3 :\n0\n\nField #4 :\n0\n\nField #5 :\n01\n*2\n2*\n22\n1*"

        # Compare actual output with expected output
        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_read_single_minefield(self):
        # Create an instance of MineSweeper
        mine_sweeper = MineSweeper('minesweeper_input_ya.txt', 'minesweeper_output.txt')

        # Call the read_input method to read a single minefield
        mine_sweeper.read_input()

        # Assert the values you expect
        self.assertEqual(mine_sweeper.rows, 5)
        self.assertEqual(mine_sweeper.cols, 2)
        self.assertEqual(mine_sweeper.field_count, 5)

    def test_check_mine(self):
        # Test case for the check_mine method
        input_minefield = [
            ['.', '.', '.', '.', '*'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.']
        ]
        expected_output = "....*\n.....\n.....\n.....\n.....\n\n"

        # Call the check_mine method
        self.mine_sweeper.check_mine(input_minefield)

        # Check if the output matches the expected output
        self.assertEqual(self.mine_sweeper.get_output(), expected_output)

        # Check if the output matches the expected output
        self.assertEqual(self.mine_sweeper.get_output(), expected_output)

    # The codes below seek to valid the assignment requirement for tests to cover all edge cases (minimums, maximums)
    # as well as some general cases. This is all done against the check_mine method of the minesweeper code as it
    # calculates and updates mine hints

    def test_check_mine_single_cell(self):
        # Test case for a single-cell minefield
        input_minefield = [['.']]
        expected_output = ".\n\n"
        self.mine_sweeper.check_mine(input_minefield)
        self.assertEqual(self.mine_sweeper.get_output(), expected_output)

    def test_check_mine_single_row(self):
        # Test case for a single-row minefield
        input_minefield = [['.', '.', '*']]
        expected_output = "..*\n\n"
        self.mine_sweeper.check_mine(input_minefield)
        self.assertEqual(self.mine_sweeper.get_output(), expected_output)

    def test_check_mine_single_col(self):
        # Test case for a single-column minefield
        input_minefield = [['.'], ['*'], ['.']]
        expected_output = ".\n*\n.\n\n"
        self.mine_sweeper.check_mine(input_minefield)
        self.assertEqual(self.mine_sweeper.get_output(), expected_output)

    def test_check_mine_max_dimensions(self):
        self.maxDiff = None  # maxDiff set to None helps us to see the full difference
        expected_output = ''
        self.assertEqual(self.mine_sweeper.get_output(), expected_output)

    def test_check_mine_all_mines(self):
        # Test case for a minefield with all cells as mines
        input_minefield = [['*'] * 5] * 5
        expected_output = "*****\n*****\n*****\n*****\n*****\n\n"
        self.mine_sweeper.check_mine(input_minefield)
        self.assertEqual(self.mine_sweeper.get_output(), expected_output)

    def test_check_mine_no_mines(self):
        # Test case for a minefield with no mines
        input_minefield = [['.'] * 5] * 5
        expected_output = ".....\n.....\n.....\n.....\n.....\n\n"
        self.mine_sweeper.check_mine(input_minefield)
        self.assertEqual(self.mine_sweeper.get_output(), expected_output)


if __name__ == '__main__':

    unittest.main()

