from minesweeper import MineSweeper
from input_generator import InputGenerator
import unittest


class TestMinesweeper(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minesweeper_obj(self):
        m = MineSweeper("mines.txt", "minesweeper_output.txt")
        self.assertEqual(type(m) == MineSweeper, True,
                         "Constructor should create Minesweeper object")

    def test_output(self):
        m = MineSweeper("minesweeper_input.txt", "minesweeper_output.txt")
        check_output = "Field #1:\n*\n\n"
        self.assertEqual(check_output, m.get_output(), True)