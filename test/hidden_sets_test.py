# pylint: disable=wrong-import-position, no-member, unexpected-keyword-arg
# I have no clue why pylint is throwing the second error
"""
Tests accuracy of hidden and naked functions of the board class
"""
import unittest
import sys
sys.path.append(".")

from sudoku_package.Board import board
from sudoku_package.Square import square

class Test_hidden_doubles(unittest.TestCase):
    """
    Tests matches_h finding hidden doubles
    """
    
    def test_hidden_double_1(self):
        """
        Test 1 of hidden double
        """
        test_row = board([[square(pos_in=[1,2,3]), square(pos_in=[1,2,3]), square(pos_in=[3,4]), square(pos_in=[3,5])]])
        solution_row = board([[square(pos_in=[1,2]), square(pos_in=[1,2]), square(pos_in=[3,4]), square(pos_in=[3,5])]])
        test_row.hidden_pairs_h()
        self.assertEqual(test_row.test_out_table(),solution_row.test_out_table())

    def test_hidden_double_2(self):
        """
        Test 2 of hidden double
        """
        test_row = board([[square(pos_in=[1,3,5]), square(pos_in=[5,6,7]), square(pos_in=[1,3,7]), square(pos_in=[8,9])]])
        solution_row = board([[square(pos_in=[1,3]), square(pos_in=[5,6,7]), square(pos_in=[1,3]), square(pos_in=[8,9])]])
        test_row.hidden_pairs_h()
        self.assertEqual(test_row.test_out_table(),solution_row.test_out_table())

class Test_hidden_sets_h(unittest.TestCase):
    """
    Tests hidden_sets_h finding hidden doubles
    """

    def test_hidden_double_1(self):
        """
        Test 1 of hidden double
        """
        test_row = board([[square(pos_in=[1,2,3]), square(pos_in=[1,2,3]), square(pos_in=[3,4,8]), square(pos_in=[3,5,9])]])
        solution_row = board([[square(pos_in=[1,2]), square(pos_in=[1,2]), square(pos_in=[3,4,8]), square(pos_in=[3,5,9])]])
        test_row.hidden_sets_h()
        self.assertEqual(test_row.test_out_table(),solution_row.test_out_table())

    def test_hidden_double_2(self):
        """
        Test 2 of hidden double
        """
        test_row = board([[square(pos_in=[1,3,5]), square(pos_in=[2,4,5,6,7]), square(pos_in=[1,3,7]), square(pos_in=[2,4,6,7,8,9])]])
        solution_row = board([[square(pos_in=[1,3]), square(pos_in=[2,4,5,6,7]), square(pos_in=[1,3]), square(pos_in=[2,4,6,7,8,9])]])
        test_row.hidden_sets_h()
        self.assertEqual(test_row.test_out_table(),solution_row.test_out_table())

class Test_hidden_sets_v(unittest.TestCase):
    """
    Tests hidden_sets_v finding hidden sets
    """

    def test_hidden_set_1(self):
        """
        Test 1 of hidden set vertical
        """
        test_board = board(([square(pos_in=[1,3,5]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,5,6,7]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,3,7]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(pos_in=[1,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(5),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[1,3]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,6,7,8,9]),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_sets_v()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

    def test_hidden_set_2(self):
        """
        Test 2 of hidden set vertical
        """
        test_board = board(([square(1),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(3),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,5,6,7,8]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(9),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,8]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,5,6,7,8]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,5,6,7,8]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,8]),square(),square(),square(),square(),square(),square(),square(),square()]))
        solution_board = board(([square(1),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(3),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(2),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[5,6,7]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(9),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,8]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[5,6,7]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[5,6,7]),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(pos_in=[2,4,8]),square(),square(),square(),square(),square(),square(),square(),square()]))
        test_board.naked_sets_v()
        solution_board.basic_scans()
        self.assertEqual(test_board.test_out_table(),solution_board.test_out_table())

if __name__== '__main__':
    unittest.main()
