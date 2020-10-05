# File which contains all the test cases for solve_sudoku.ipynb. These tests are run using pytest

import import_ipynb
import solve_sudoku
import numpy as np
from solve_sudoku import *

DEBUG_ARRAY = np.resize([0 ,6, 0, 0, 4, 5, 3, 7, 0,
                         0, 0, 5, 6, 7, 3, 4, 2, 0,
                         0, 0, 4, 0, 0, 0, 0, 0, 1,
                         5, 0, 0, 7, 0, 2, 0, 0, 4,
                         6, 0, 9, 0, 0, 0, 2, 5, 0,
                         8, 0, 7, 0, 0, 9, 0, 0, 3,
                         4, 9, 0, 5, 1, 7, 8, 0, 0,
                         2, 1, 0, 0, 3, 6, 0, 0, 0,
                         0, 5, 0, 0, 2, 0, 1, 0, 0], (9,9))

def test_get_sub_square_row_col():
    assert(get_sub_square_row_col(0) == 1)
    assert(get_sub_square_row_col(1) == 1)
    assert(get_sub_square_row_col(2) == 1)
    assert(get_sub_square_row_col(3) == 4)
    assert(get_sub_square_row_col(4) == 4)
    assert(get_sub_square_row_col(5) == 4)
    assert(get_sub_square_row_col(6) == 7)
    assert(get_sub_square_row_col(7) == 7)
    assert(get_sub_square_row_col(8) == 7)


def test_get_sub_square_elem():
    assert(get_sub_square_elem(0, 0, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})
    assert(get_sub_square_elem(0, 1, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})    
    assert(get_sub_square_elem(0, 2, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})        
    assert(get_sub_square_elem(1, 0, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})
    assert(get_sub_square_elem(1, 1, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})    
    assert(get_sub_square_elem(1, 2, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})
    assert(get_sub_square_elem(2, 0, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})
    assert(get_sub_square_elem(2, 1, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})    
    assert(get_sub_square_elem(2, 2, input_arr=DEBUG_ARRAY) == {0, 4, 5, 6})
    
    assert(get_sub_square_elem(0, 3, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})    
    assert(get_sub_square_elem(0, 4, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})        
    assert(get_sub_square_elem(0, 5, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})            
    assert(get_sub_square_elem(1, 3, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})    
    assert(get_sub_square_elem(1, 4, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})        
    assert(get_sub_square_elem(1, 5, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})                
    assert(get_sub_square_elem(2, 3, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})    
    assert(get_sub_square_elem(2, 4, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})        
    assert(get_sub_square_elem(2, 5, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})                    
    
    assert(get_sub_square_elem(0, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    assert(get_sub_square_elem(0, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    assert(get_sub_square_elem(0, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    assert(get_sub_square_elem(1, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    assert(get_sub_square_elem(1, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    assert(get_sub_square_elem(1, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    assert(get_sub_square_elem(2, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    assert(get_sub_square_elem(2, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    assert(get_sub_square_elem(2, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})    
    
    
def test_get_row_col_elem():
    
    assert(get_row_elem(0, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})
    assert(get_row_elem(1, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7})
    assert(get_row_elem(2, input_arr=DEBUG_ARRAY) == {0, 1, 4})
    assert(get_row_elem(3, input_arr=DEBUG_ARRAY) == {0, 2, 4, 5, 7})
    assert(get_row_elem(4, input_arr=DEBUG_ARRAY) == {0, 2, 5, 6, 9})
    assert(get_row_elem(5, input_arr=DEBUG_ARRAY) == {0, 3, 7, 8, 9})
    assert(get_row_elem(6, input_arr=DEBUG_ARRAY) == {0, 1, 4, 5, 7, 8, 9})
    assert(get_row_elem(7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 6})
    assert(get_row_elem(8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 5})

    assert(get_col_elem(0, input_arr=DEBUG_ARRAY) == {0, 2, 4, 5, 6, 8})
    assert(get_col_elem(1, input_arr=DEBUG_ARRAY) == {0, 1, 5, 6, 9})
    assert(get_col_elem(2, input_arr=DEBUG_ARRAY) == {0, 4, 5, 7, 9})
    assert(get_col_elem(3, input_arr=DEBUG_ARRAY) == {0, 5, 6, 7})
    assert(get_col_elem(4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})
    assert(get_col_elem(5, input_arr=DEBUG_ARRAY) == {0, 2, 3, 5, 6, 7, 9})
    assert(get_col_elem(6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 8})
    assert(get_col_elem(7, input_arr=DEBUG_ARRAY) == {0, 2, 5, 7})
    assert(get_col_elem(8, input_arr=DEBUG_ARRAY) == {0, 1, 3, 4})
    
    
def test_get_row_col_sub_square_elem():
    assert(get_row_col_sub_square_elem(0, 0, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7, 8})
    assert(get_row_col_sub_square_elem(0, 1, input_arr=DEBUG_ARRAY) == {0, 1, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(0, 2, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(0, 3, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(0, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(0, 5, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(0, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 8})
    assert(get_row_col_sub_square_elem(0, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(0, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(1, 0, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7, 8})
    assert(get_row_col_sub_square_elem(1, 1, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(1, 2, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(1, 3, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(1, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(1, 5, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(1, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 8})
    assert(get_row_col_sub_square_elem(1, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(1, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(2, 0, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 6, 8})
    assert(get_row_col_sub_square_elem(2, 1, input_arr=DEBUG_ARRAY) == {0, 1, 4, 5, 6, 9})
    assert(get_row_col_sub_square_elem(2, 2, input_arr=DEBUG_ARRAY) == {0, 1, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(2, 3, input_arr=DEBUG_ARRAY) == {0, 1, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(2, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(2, 5, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(2, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7, 8})
    assert(get_row_col_sub_square_elem(2, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 7})
    assert(get_row_col_sub_square_elem(2, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7})
    assert(get_row_col_sub_square_elem(3, 0, input_arr=DEBUG_ARRAY) == {0, 2, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(3, 1, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(3, 2, input_arr=DEBUG_ARRAY) == {0, 2, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(3, 3, input_arr=DEBUG_ARRAY) == {0, 2, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(3, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 7, 9})
    assert(get_row_col_sub_square_elem(3, 5, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(3, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 7, 8})
    assert(get_row_col_sub_square_elem(3, 7, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 7})
    assert(get_row_col_sub_square_elem(3, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 7})
    assert(get_row_col_sub_square_elem(4, 0, input_arr=DEBUG_ARRAY) == {0, 2, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(4, 1, input_arr=DEBUG_ARRAY) == {0, 1, 2, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(4, 2, input_arr=DEBUG_ARRAY) == {0, 2, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(4, 3, input_arr=DEBUG_ARRAY) == {0, 2, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(4, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(4, 5, input_arr=DEBUG_ARRAY) == {0, 2, 3, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(4, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 8, 9})
    assert(get_row_col_sub_square_elem(4, 7, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(4, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 9})
    assert(get_row_col_sub_square_elem(5, 0, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(5, 1, input_arr=DEBUG_ARRAY) == {0, 1, 3, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(5, 2, input_arr=DEBUG_ARRAY) == {0, 3, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(5, 3, input_arr=DEBUG_ARRAY) == {0, 2, 3, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(5, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 7, 8, 9})
    assert(get_row_col_sub_square_elem(5, 5, input_arr=DEBUG_ARRAY) == {0, 2, 3, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(5, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 7, 8, 9})
    assert(get_row_col_sub_square_elem(5, 7, input_arr=DEBUG_ARRAY) == {0, 2, 3, 4, 5, 7, 8, 9})
    assert(get_row_col_sub_square_elem(5, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 0, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 1, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 2, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 3, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 5, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 7, 8, 9})
    assert(get_row_col_sub_square_elem(6, 8, input_arr=DEBUG_ARRAY) == {0, 1, 3, 4, 5, 7, 8, 9})
    assert(get_row_col_sub_square_elem(7, 0, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 8, 9})
    assert(get_row_col_sub_square_elem(7, 1, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 9})
    assert(get_row_col_sub_square_elem(7, 2, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(7, 3, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 5, 6, 7})
    assert(get_row_col_sub_square_elem(7, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(7, 5, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(7, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 6, 8})
    assert(get_row_col_sub_square_elem(7, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 5, 6, 7, 8})
    assert(get_row_col_sub_square_elem(7, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 6, 8})
    assert(get_row_col_sub_square_elem(8, 0, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 6, 8, 9})
    assert(get_row_col_sub_square_elem(8, 1, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 6, 9})
    assert(get_row_col_sub_square_elem(8, 2, input_arr=DEBUG_ARRAY) == {0, 1, 2, 4, 5, 7, 9})
    assert(get_row_col_sub_square_elem(8, 3, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 5, 6, 7})
    assert(get_row_col_sub_square_elem(8, 4, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 6, 7})
    assert(get_row_col_sub_square_elem(8, 5, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 5, 6, 7, 9})
    assert(get_row_col_sub_square_elem(8, 6, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 8})
    assert(get_row_col_sub_square_elem(8, 7, input_arr=DEBUG_ARRAY) == {0, 1, 2, 5, 7, 8})
    assert(get_row_col_sub_square_elem(8, 8, input_arr=DEBUG_ARRAY) == {0, 1, 2, 3, 4, 5, 8})    
    
    
def test_get_all_rel_indices_elem():    
    assert(get_all_rel_indices_elem(0, 0, input_arr=DEBUG_ARRAY) == 
           {(3, 0), (8, 0), (0, 7), (2, 1), (0, 3), (4, 0), (1, 2), 
            (5, 0), (2, 2), (0, 4), (1, 1), (0, 0), (6, 0), (0, 5), 
            (1, 0), (0, 8), (0, 1), (7, 0), (0, 6), (2, 0), (0, 2)})
    assert(get_all_rel_indices_elem(0, 6, input_arr=DEBUG_ARRAY) == {(6, 6), (5, 6), (2, 8), (0, 7), (1, 6), (0, 3), (7, 6), (3, 6), (0, 4), (8, 6), (0, 0), (2, 6), (0, 5), (0, 8), (0, 1), (2, 7), (4, 6), (0, 6), (1, 8), (1, 7), (0, 2)})
    assert(get_all_rel_indices_elem(1, 1, input_arr=DEBUG_ARRAY) == {(1, 3), (2, 1), (1, 6), (5, 1), (1, 2), (8, 1), (1, 5), (2, 2), (4, 1), (1, 1), (0, 0), (7, 1), (1, 4), (1, 0), (0, 1), (6, 1), (3, 1), (2, 0), (1, 8), (1, 7), (0, 2)})
    assert(get_all_rel_indices_elem(1, 2, input_arr=DEBUG_ARRAY) == {(1, 3), (2, 1), (6, 2), (1, 6), (7, 2), (1, 2), (1, 5), (2, 2), (1, 1), (3, 2), (0, 0), (8, 2), (1, 4), (4, 2), (1, 0), (0, 1), (2, 0), (1, 8), (1, 7), (5, 2), (0, 2)})
    assert(get_all_rel_indices_elem(1, 3, input_arr=DEBUG_ARRAY) == {(7, 3), (1, 3), (1, 6), (2, 5), (0, 3), (1, 2), (3, 3), (6, 3), (1, 5), (0, 4), (1, 1), (1, 4), (2, 3), (0, 5), (1, 0), (5, 3), (8, 3), (1, 8), (4, 3), (1, 7), (2, 4)})
    assert(get_all_rel_indices_elem(3, 5, input_arr=DEBUG_ARRAY) == {(3, 0), (3, 7), (2, 5), (8, 5), (3, 3), (5, 5), (4, 4), (1, 5), (3, 6), (3, 2), (5, 4), (4, 5), (7, 5), (0, 5), (6, 5), (5, 3), (3, 5), (3, 1), (3, 8), (4, 3), (3, 4)})
    assert(get_all_rel_indices_elem(3, 6, input_arr=DEBUG_ARRAY) == {(4, 7), (6, 6), (3, 0), (5, 6), (4, 8), (1, 6), (3, 7), (5, 8), (3, 3), (7, 6), (3, 6), (8, 6), (3, 2), (2, 6), (3, 5), (4, 6), (3, 1), (5, 7), (3, 8), (0, 6), (3, 4)})
    assert(get_all_rel_indices_elem(3, 7, input_arr=DEBUG_ARRAY) == {(4, 7), (4, 8), (3, 0), (5, 6), (7, 7), (0, 7), (3, 7), (5, 8), (6, 7), (3, 3), (3, 6), (3, 2), (8, 7), (3, 5), (2, 7), (4, 6), (3, 1), (5, 7), (3, 8), (1, 7), (3, 4)})
    assert(get_all_rel_indices_elem(5, 2, input_arr=DEBUG_ARRAY) == {(5, 6), (3, 0), (6, 2), (5, 1), (7, 2), (4, 0), (1, 2), (5, 8), (5, 5), (5, 0), (2, 2), (4, 1), (5, 4), (3, 2), (8, 2), (4, 2), (5, 3), (5, 7), (3, 1), (5, 2), (0, 2)})
    assert(get_all_rel_indices_elem(5, 3, input_arr=DEBUG_ARRAY) == {(7, 3), (1, 3), (5, 6), (5, 1), (0, 3), (5, 8), (5, 5), (3, 3), (4, 4), (6, 3), (5, 0), (5, 4), (4, 5), (5, 2), (2, 3), (3, 5), (5, 3), (8, 3), (5, 7), (4, 3), (3, 4)})
    assert(get_all_rel_indices_elem(5, 4, input_arr=DEBUG_ARRAY) == {(5, 6), (5, 1), (5, 8), (5, 5), (3, 3), (4, 4), (5, 0), (0, 4), (6, 4), (5, 4), (4, 5), (5, 2), (1, 4), (3, 5), (5, 3), (5, 7), (7, 4), (4, 3), (3, 4), (2, 4), (8, 4)})
    assert(get_all_rel_indices_elem(5, 5, input_arr=DEBUG_ARRAY) == {(5, 6), (5, 1), (2, 5), (8, 5), (5, 8), (5, 5), (3, 3), (4, 4), (1, 5), (5, 0), (5, 4), (4, 5), (5, 2), (7, 5), (0, 5), (6, 5), (3, 5), (5, 3), (5, 7), (4, 3), (3, 4)})
    assert(get_all_rel_indices_elem(5, 6, input_arr=DEBUG_ARRAY) == {(4, 7), (6, 6), (5, 6), (4, 8), (1, 6), (3, 7), (5, 1), (5, 8), (5, 5), (7, 6), (5, 0), (3, 6), (8, 6), (5, 4), (2, 6), (5, 3), (4, 6), (5, 7), (3, 8), (0, 6), (5, 2)})
    assert(get_all_rel_indices_elem(5, 7, input_arr=DEBUG_ARRAY) == {(4, 7), (4, 8), (5, 6), (7, 7), (0, 7), (3, 7), (5, 1), (5, 8), (6, 7), (5, 5), (5, 0), (3, 6), (5, 4), (8, 7), (5, 3), (2, 7), (4, 6), (5, 7), (3, 8), (1, 7), (5, 2)})
    assert(get_all_rel_indices_elem(5, 8, input_arr=DEBUG_ARRAY) == {(4, 7), (4, 8), (5, 6), (2, 8), (3, 7), (5, 1), (5, 8), (5, 5), (5, 0), (3, 6), (5, 4), (5, 2), (0, 8), (5, 3), (6, 8), (4, 6), (5, 7), (3, 8), (1, 8), (8, 8), (7, 8)})
    assert(get_all_rel_indices_elem(6, 0, input_arr=DEBUG_ARRAY) == {(6, 6), (3, 0), (8, 0), (6, 2), (7, 2), (4, 0), (6, 7), (8, 1), (6, 3), (5, 0), (6, 4), (0, 0), (8, 2), (7, 1), (6, 0), (1, 0), (6, 5), (7, 0), (6, 8), (6, 1), (2, 0)})
    assert(get_all_rel_indices_elem(6, 1, input_arr=DEBUG_ARRAY) == {(6, 6), (8, 0), (2, 1), (6, 2), (5, 1), (7, 2), (6, 7), (8, 1), (6, 3), (4, 1), (1, 1), (6, 4), (8, 2), (7, 1), (6, 0), (6, 5), (0, 1), (7, 0), (6, 8), (6, 1), (3, 1)})
    assert(get_all_rel_indices_elem(6, 2, input_arr=DEBUG_ARRAY) == {(6, 6), (8, 0), (6, 2), (7, 2), (1, 2), (6, 7), (8, 1), (6, 3), (2, 2), (6, 4), (3, 2), (8, 2), (7, 1), (6, 0), (4, 2), (6, 5), (7, 0), (6, 8), (6, 1), (5, 2), (0, 2)})
    assert(get_all_rel_indices_elem(6, 3, input_arr=DEBUG_ARRAY) == {(7, 3), (1, 3), (6, 6), (6, 2), (0, 3), (8, 5), (6, 7), (3, 3), (6, 3), (6, 4), (6, 0), (7, 5), (2, 3), (6, 5), (5, 3), (8, 3), (6, 8), (6, 1), (7, 4), (4, 3), (8, 4)})
    assert(get_all_rel_indices_elem(6, 4, input_arr=DEBUG_ARRAY) == {(7, 3), (6, 6), (6, 2), (8, 5), (6, 7), (4, 4), (6, 3), (0, 4), (6, 4), (5, 4), (6, 0), (1, 4), (7, 5), (6, 5), (8, 3), (6, 8), (6, 1), (7, 4), (3, 4), (2, 4), (8, 4)})
    assert(get_all_rel_indices_elem(8, 2, input_arr=DEBUG_ARRAY) == {(8, 0), (6, 2), (8, 5), (7, 2), (1, 2), (8, 1), (2, 2), (8, 6), (3, 2), (8, 2), (7, 1), (6, 0), (8, 7), (4, 2), (8, 3), (7, 0), (6, 1), (8, 8), (5, 2), (0, 2), (8, 4)})
    assert(get_all_rel_indices_elem(8, 3, input_arr=DEBUG_ARRAY) == {(7, 3), (1, 3), (8, 0), (0, 3), (8, 5), (3, 3), (8, 1), (6, 3), (8, 6), (6, 4), (8, 2), (7, 5), (2, 3), (8, 7), (6, 5), (5, 3), (8, 3), (7, 4), (8, 8), (4, 3), (8, 4)})
    assert(get_all_rel_indices_elem(8, 4, input_arr=DEBUG_ARRAY) == {(7, 3), (8, 0), (8, 5), (8, 1), (4, 4), (6, 3), (0, 4), (8, 6), (6, 4), (5, 4), (8, 2), (1, 4), (7, 5), (8, 7), (6, 5), (8, 3), (7, 4), (8, 8), (3, 4), (2, 4), (8, 4)})
    assert(get_all_rel_indices_elem(8, 5, input_arr=DEBUG_ARRAY) == {(7, 3), (8, 0), (2, 5), (8, 5), (5, 5), (8, 1), (6, 3), (1, 5), (8, 6), (6, 4), (8, 2), (4, 5), (7, 5), (0, 5), (8, 7), (6, 5), (3, 5), (8, 3), (7, 4), (8, 8), (8, 4)})
    assert(get_all_rel_indices_elem(8, 6, input_arr=DEBUG_ARRAY) == {(6, 6), (5, 6), (8, 0), (7, 7), (1, 6), (8, 5), (6, 7), (8, 1), (7, 6), (3, 6), (8, 6), (2, 6), (8, 2), (8, 7), (8, 3), (4, 6), (6, 8), (0, 6), (8, 8), (7, 8), (8, 4)})
    assert(get_all_rel_indices_elem(8, 7, input_arr=DEBUG_ARRAY) == {(4, 7), (6, 6), (8, 0), (7, 7), (0, 7), (3, 7), (8, 5), (6, 7), (8, 1), (7, 6), (8, 6), (8, 2), (8, 7), (2, 7), (8, 3), (6, 8), (5, 7), (8, 8), (1, 7), (7, 8), (8, 4)})
    assert(get_all_rel_indices_elem(8, 8, input_arr=DEBUG_ARRAY) == {(4, 8), (6, 6), (2, 8), (8, 0), (7, 7), (8, 5), (5, 8), (6, 7), (8, 1), (7, 6), (8, 6), (8, 2), (8, 7), (0, 8), (8, 3), (6, 8), (3, 8), (1, 8), (8, 8), (7, 8), (8, 4)})
    
    
def test_get_num_known_elem_vicinity_cur_elem():
    assert(get_num_known_elem_vicinity_cur_elem(0, 0, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(0, 1, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(0, 2, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(0, 3, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(0, 4, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(0, 5, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(0, 6, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(0, 7, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(0, 8, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(1, 0, input_arr=DEBUG_ARRAY) == 13)
    assert(get_num_known_elem_vicinity_cur_elem(1, 1, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(1, 2, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(1, 3, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(1, 4, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(1, 5, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(1, 6, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(1, 7, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(1, 8, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(2, 0, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(2, 1, input_arr=DEBUG_ARRAY) == 7)
    assert(get_num_known_elem_vicinity_cur_elem(2, 2, input_arr=DEBUG_ARRAY) == 6)
    assert(get_num_known_elem_vicinity_cur_elem(2, 3, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(2, 4, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(2, 5, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(2, 6, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(2, 7, input_arr=DEBUG_ARRAY) == 7)
    assert(get_num_known_elem_vicinity_cur_elem(2, 8, input_arr=DEBUG_ARRAY) == 8)
    assert(get_num_known_elem_vicinity_cur_elem(3, 0, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(3, 1, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(3, 2, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(3, 3, input_arr=DEBUG_ARRAY) == 7)
    assert(get_num_known_elem_vicinity_cur_elem(3, 4, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(3, 5, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(3, 6, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(3, 7, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(3, 8, input_arr=DEBUG_ARRAY) == 8)
    assert(get_num_known_elem_vicinity_cur_elem(4, 0, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(4, 1, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(4, 2, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(4, 3, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(4, 4, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(4, 5, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(4, 6, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(4, 7, input_arr=DEBUG_ARRAY) == 8)
    assert(get_num_known_elem_vicinity_cur_elem(4, 8, input_arr=DEBUG_ARRAY) == 7)
    assert(get_num_known_elem_vicinity_cur_elem(5, 0, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(5, 1, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(5, 2, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(5, 3, input_arr=DEBUG_ARRAY) == 8)
    assert(get_num_known_elem_vicinity_cur_elem(5, 4, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(5, 5, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(5, 6, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(5, 7, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(5, 8, input_arr=DEBUG_ARRAY) == 8)
    assert(get_num_known_elem_vicinity_cur_elem(6, 0, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(6, 1, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(6, 2, input_arr=DEBUG_ARRAY) == 13)
    assert(get_num_known_elem_vicinity_cur_elem(6, 3, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(6, 4, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(6, 5, input_arr=DEBUG_ARRAY) == 13)
    assert(get_num_known_elem_vicinity_cur_elem(6, 6, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(6, 7, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(6, 8, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(7, 0, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(7, 1, input_arr=DEBUG_ARRAY) == 8)
    assert(get_num_known_elem_vicinity_cur_elem(7, 2, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(7, 3, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(7, 4, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(7, 5, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(7, 6, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(7, 7, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(7, 8, input_arr=DEBUG_ARRAY) == 9)
    assert(get_num_known_elem_vicinity_cur_elem(8, 0, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(8, 1, input_arr=DEBUG_ARRAY) == 8)
    assert(get_num_known_elem_vicinity_cur_elem(8, 2, input_arr=DEBUG_ARRAY) == 11)
    assert(get_num_known_elem_vicinity_cur_elem(8, 3, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(8, 4, input_arr=DEBUG_ARRAY) == 10)
    assert(get_num_known_elem_vicinity_cur_elem(8, 5, input_arr=DEBUG_ARRAY) == 12)
    assert(get_num_known_elem_vicinity_cur_elem(8, 6, input_arr=DEBUG_ARRAY) == 7)
    assert(get_num_known_elem_vicinity_cur_elem(8, 7, input_arr=DEBUG_ARRAY) == 7)
    assert(get_num_known_elem_vicinity_cur_elem(8, 8, input_arr=DEBUG_ARRAY) == 7)
    
    
def test_explorationState():
    
    test_obj = explorationState(3, 7, 13, 5, np.ones((9,9)))
    (row, col, elem, impact, given_array) = test_obj.get_elements()
    np.testing.assert_equal(row, 3)
    np.testing.assert_equal(col, 7)
    np.testing.assert_equal(elem, 13)
    np.testing.assert_equal(impact, 5)
    np.testing.assert_array_equal(given_array, 
                                  np.array([[ 1,  1,  1,  1, 1,  1,  1,  1,  1],
                                            [ 1,  1,  1,  1, 1,  1,  1,  1,  1],
                                            [ 1,  1,  1,  1, 1,  1,  1,  1,  1],
                                            [ 1,  1,  1,  1, 1,  1,  1,  1,  1],
                                            [ 1,  1,  1,  1, 1,  1,  1,  1,  1],
                                            [ 1,  1,  1,  1, 1,  1,  1,  1,  1],
                                            [ 1,  1,  1,  1, 1,  1,  1,  1,  1],
                                            [ 1,  1,  1,  1, 1,  1,  1,  1,  1], 
                                            [ 1,  1,  1,  1, 1,  1,  1,  1,  1]]))    


    
def test_check_if_state_is_correct():
    np.testing.assert_equal(check_if_state_is_correct(
        np.array([[ 9,  9,  8,  7, 13,  9,  6,  5,  6],
                  [ 7,  7,  6,  8, 14, 10,  7,  6,  7],
                  [10, 10,  9,  9, 15, 11,  9,  8,  9],
                  [ 7,  8,  7,  7, 12,  9,  8,  7,  7],
                  [ 6,  7,  6,  7, 12,  9,  7,  6,  6],
                  [ 6,  7,  6,  6, 11,  8,  6,  5,  5],
                  [10,  7,  7,  7, 12,  9,  7,  7,  6],
                  [ 8,  5,  5,  6, 11,  8,  6,  6,  5], 
                  [ 9,  6,  6,  7, 12,  9,  6,  6,  5]])), False)
    np.testing.assert_equal(check_if_state_is_correct(DEBUG_ARRAY), True)

    
def test_get_max_min_elem_given_indices():
    input_test_array = np.array([[ 9,  9,  8,  7, 13,  9,  6,  5,  6],
                                 [ 7,  7,  6,  8, 14, 10,  7,  6,  7],
                                 [10, 10,  9,  9, 15, 11,  9,  8,  9],
                                 [ 7,  8,  7,  7, 12,  9,  8,  7,  7],
                                 [ 6,  7,  6,  7, 12,  9,  7,  6,  6],
                                 [ 6,  7,  6,  6, 11,  8,  6,  5,  5],
                                 [10,  7,  7,  7, 12,  9,  7,  7,  6],
                                 [ 8,  5,  5,  6, 11,  8,  6,  6,  5], 
                                 [ 9,  6,  6,  7, 12,  9,  6,  6,  5]])

    row_indices = np.array([0, 0, 0, 1])
    col_indices = np.array([0, 1, 2, 4])
    np.testing.assert_equal(get_max_elem_given_indices(input_test_array, row_indices, col_indices), (14, 1, 4))
    np.testing.assert_equal(get_min_elem_given_indices(input_test_array, row_indices, col_indices), (8, 0, 2))    
    
    
def test_pushing_into_stack_various_modes():
    input_test_array = np.array([[ 9,  9,  8,  7, 13,  9,  6,  5,  6],
                                 [ 7,  7,  6,  8, 14, 10,  7,  6,  7],
                                 [10, 10,  9,  9, 15, 11,  9,  8,  9],
                                 [ 7,  8,  7,  7, 12,  9,  8,  7,  7],
                                 [ 6,  7,  6,  7, 12,  9,  7,  6,  6],
                                 [ 6,  7,  6,  6, 11,  8,  6,  5,  5],
                                 [10,  7,  7,  7, 12,  9,  7,  7,  6],
                                 [ 8,  5,  5,  6, 11,  8,  6,  6,  5], 
                                 [ 9,  6,  6,  7, 12,  9,  6,  6,  5]])

    array_of_sets = \
        [[{2, 5}, {2, 4, 7}, {2, 5, 7}, {2, 5}, {6}, {8}, {9, 4, 5, 7}, {3}, {1, 5, 9}], 
         [{1}, {9}, {2, 5, 6, 7}, {2, 3, 5}, {4}, {2, 3}, {5, 6, 7}, {8, 5, 7}, {8, 5, 6}], 
         [{8}, {4, 6}, {3}, {1}, {9}, {7}, {2}, {4, 5}, {5, 6}], 
         [{4}, {8, 2, 3}, {8, 9, 2}, {8, 9, 3}, {5}, {1}, {9, 3, 7}, {6}, {9, 2, 3}], 
         [{7}, {8, 3, 6}, {1, 5, 6, 8, 9}, {8, 9, 3, 6}, {2}, {9, 3, 6}, {9, 3, 5}, {1, 5, 9}, {4}], 
         [{2, 3, 5, 6, 9}, {2, 3, 6}, {1, 2, 5, 6, 9}, {9, 3, 4, 6}, {7}, {9, 3, 4, 6}, {8}, {1, 2, 5, 9}, {1, 2, 3, 5, 9}], 
         [{9, 2, 3, 6}, {1}, {9, 2, 6}, {9, 2, 4, 6}, {8}, {5}, {9, 3, 4, 6}, {9, 2, 4}, {7}], 
         [{9, 2, 3, 6}, {2, 3, 6, 7, 8}, {4}, {9, 2, 6, 7}, {1}, {9, 2, 6}, {9, 3, 5, 6}, {8, 9, 2, 5}, {2, 3, 5, 6, 8, 9}], 
         [{9, 2, 6}, {5}, {2, 6, 7, 8, 9}, {2, 4, 6, 7, 9}, {3}, {9, 2, 4, 6}, {1}, {8, 9, 2, 4}, {8, 9, 2, 6}]]

    output = get_max_num_known_elem_row_col(input_test_array, array_of_sets)
    np.testing.assert_equal(output, (1, 5, {2, 3}, 10))
    output = get_min_num_known_elem_row_col(input_test_array, array_of_sets)
    np.testing.assert_equal(output, (5, 7, {1, 2, 5, 9}, 5))
    output = get_min_num_possiblities_first_unknown_elem_row_col(input_test_array, array_of_sets)
    np.testing.assert_equal(output, (0, 0, {2, 5}, 9))
    output = get_min_num_possibilities_max_num_known_elem_row_col(input_test_array, array_of_sets)
    np.testing.assert_equal(output, (1, 5, {2, 3}, 10))
    output = get_min_num_possibilities_min_num_known_elem_row_col(input_test_array, array_of_sets)
    np.testing.assert_equal(output, (0, 3, {2, 5}, 7))
    output = get_zero_elem_row_col_num_known_elem(input_test_array, array_of_sets)
    np.testing.assert_equal(output, (-1, -1, set(), 0))
    output = get_zero_elem_row_col_num_known_elem(DEBUG_ARRAY, array_of_sets)
    np.testing.assert_equal(output, (0, 0, {2, 5}, 0))
  
    output = get_unknown_elem_row_col_as_list(DEBUG_ARRAY, input_test_array, array_of_sets, run_mode='FIRST_UNKNOWN')
    np.testing.assert_equal(output, [(0, 0, 2, 0), (0, 0, 5, 0)])

    output = get_unknown_elem_row_col_as_list(DEBUG_ARRAY, input_test_array, array_of_sets, run_mode='FIRST_UNKNOWN')
    np.testing.assert_equal(output, [(0, 0, 2, 0), (0, 0, 5, 0)])
    output = get_unknown_elem_row_col_as_list(
        DEBUG_ARRAY, input_test_array, array_of_sets, run_mode='MIN_NUM_POSSIBILITIES_FIRST_UNKNOWN')
    np.testing.assert_equal(output, [(0, 0, 2, 9), (0, 0, 5, 9)])
    output = get_unknown_elem_row_col_as_list(
        DEBUG_ARRAY, input_test_array, array_of_sets, run_mode='MAX_NUM_KNOWN_ELEM')
    np.testing.assert_equal(output, [(1, 5, 2, 10), (1, 5, 3, 10)])
    output = get_unknown_elem_row_col_as_list(
        DEBUG_ARRAY, input_test_array, array_of_sets, run_mode='MIN_NUM_POSSIBILITIES_MAX_NUM_KNOWN_ELEM')
    np.testing.assert_equal(output, [(1, 5, 2, 10), (1, 5, 3, 10)])
    output = get_unknown_elem_row_col_as_list(
        DEBUG_ARRAY, input_test_array, array_of_sets, run_mode='MIN_NUM_POSSIBILITIES_MIN_NUM_KNOWN_ELEM')
    np.testing.assert_equal(output, [(0, 3, 2, 7), (0, 3, 5, 7)])
    output = get_unknown_elem_row_col_as_list(
        DEBUG_ARRAY, input_test_array, array_of_sets, run_mode='MIN_NUM_KNOWN_ELEM')
    np.testing.assert_equal(output, [(5, 7, 1, 5), (5, 7, 2, 5), (5, 7, 5, 5), (5, 7, 9, 5)])
    output = get_unknown_elem_row_col_as_list(
        DEBUG_ARRAY, input_test_array, array_of_sets)
    np.testing.assert_equal(output, [(0, 3, 2, 7), (0, 3, 5, 7)])
    output = get_unknown_elem_row_col_as_list(
        DEBUG_ARRAY, input_test_array, array_of_sets, run_mode='BLA_BLA')
    np.testing.assert_equal(output, [(0, 3, 2, 7), (0, 3, 5, 7)])
      
    stack_test = LifoQueue(maxsize=2)
    
    sort_items_by_impact_and_push_to_stack(DEBUG_ARRAY, input_test_array, array_of_sets, stack_test)
    np.testing.assert_equal(stack_test.qsize(), 2)  
    state1 = stack_test.get()
    (row, col, elem, impact, output_arr) = state1.get_elements()
    np.testing.assert_equal(row, 0)
    np.testing.assert_equal(col, 3)
    np.testing.assert_equal(elem, 5)
    np.testing.assert_equal(impact, 7)    
    np.testing.assert_equal(output_arr, DEBUG_ARRAY)

    state2 = stack_test.get()
    (row, col, elem, impact, output_arr) = state2.get_elements()
    np.testing.assert_equal(row, 0)
    np.testing.assert_equal(col, 3)
    np.testing.assert_equal(elem, 2)
    np.testing.assert_equal(impact, 7)        
    np.testing.assert_equal(output_arr, DEBUG_ARRAY)

    np.testing.assert_equal(stack_test.qsize(), 0)
    
    
def test_solve_sudoku():
    (solution, num_stack_iterations) = solve_sudoku(input_arr=DEBUG_ARRAY, debug_output=False)
    np.testing.assert_array_equal(solution,
                                 np.array([[9, 6, 2, 1, 4, 5, 3, 7, 8],
                                           [1, 8, 5, 6, 7, 3, 4, 2, 9],
                                           [3, 7, 4, 2, 9, 8, 5, 6, 1],
                                           [5, 3, 1, 7, 6, 2, 9, 8, 4],
                                           [6, 4, 9, 3, 8, 1, 2, 5, 7],
                                           [8, 2, 7, 4, 5, 9, 6, 1, 3],
                                           [4, 9, 6, 5, 1, 7, 8, 3, 2],
                                           [2, 1, 8, 9, 3, 6, 7, 4, 5],
                                           [7, 5, 3, 8, 2, 4, 1, 9, 6]]))
    np.testing.assert_equal(num_stack_iterations, 0)
    
    (solution, num_stack_iterations) = solve_sudoku(input_arr=np.array([[0, 0, 0, 0, 6, 8, 0, 3, 0],
                                                                        [1, 9, 0, 0, 0, 0, 0, 0, 0],
                                                                        [8, 0, 3, 1, 0, 0, 2, 0, 0],
                                                                        [4, 0, 0, 0, 5, 1, 0, 6, 0],
                                                                        [7, 0, 0, 0, 2, 0, 0, 0, 4],
                                                                        [0, 0, 0, 0, 7, 0, 8, 0, 0],
                                                                        [0, 1, 0, 0, 0, 5, 0, 0, 7],
                                                                        [0, 0, 4, 0, 0, 0, 0, 0, 0],
                                                                        [0, 5, 0, 0, 3, 0, 1, 0, 0]]), 
                                                    debug_output=False)
    np.testing.assert_array_equal(solution,
                                np.array([[2, 4, 7, 5, 6, 8, 9, 3, 1],
                                           [1, 9, 5, 3, 4, 2, 6, 7, 8],
                                           [8, 6, 3, 1, 9, 7, 2, 4, 5],
                                           [4, 3, 9, 8, 5, 1, 7, 6, 2],
                                           [7, 8, 1, 9, 2, 6, 3, 5, 4],
                                           [5, 2, 6, 4, 7, 3, 8, 1, 9],
                                           [3, 1, 2, 6, 8, 5, 4, 9, 7],
                                           [6, 7, 4, 2, 1, 9, 5, 8, 3],
                                           [9, 5, 8, 7, 3, 4, 1, 2, 6]]))    
    np.testing.assert_equal(num_stack_iterations, 22)    
    (solution, num_stack_iterations) = solve_sudoku(input_arr=np.array([[0, 0, 0, 0, 6, 8, 0, 3, 0],
                                                                        [1, 9, 0, 0, 0, 0, 0, 0, 0],
                                                                        [8, 0, 3, 1, 0, 0, 2, 0, 0],
                                                                        [4, 0, 0, 0, 5, 1, 0, 6, 0],
                                                                        [7, 0, 0, 0, 2, 0, 0, 0, 4],
                                                                        [0, 0, 0, 0, 7, 0, 8, 0, 0],
                                                                        [0, 1, 0, 0, 0, 5, 0, 0, 7],
                                                                        [0, 0, 4, 0, 0, 0, 0, 0, 0],
                                                                        [0, 5, 0, 0, 3, 0, 1, 0, 0]]), 
                                                    run_mode = 'FIRST_UNKNOWN',
                                                    debug_output=False)

    np.testing.assert_array_equal(solution,
                                np.array([[2, 4, 7, 5, 6, 8, 9, 3, 1],
                                           [1, 9, 5, 3, 4, 2, 6, 7, 8],
                                           [8, 6, 3, 1, 9, 7, 2, 4, 5],
                                           [4, 3, 9, 8, 5, 1, 7, 6, 2],
                                           [7, 8, 1, 9, 2, 6, 3, 5, 4],
                                           [5, 2, 6, 4, 7, 3, 8, 1, 9],
                                           [3, 1, 2, 6, 8, 5, 4, 9, 7],
                                           [6, 7, 4, 2, 1, 9, 5, 8, 3],
                                           [9, 5, 8, 7, 3, 4, 1, 2, 6]]))    
    #np.testing.assert_equal(num_stack_iterations, 75)        
    np.testing.assert_equal(num_stack_iterations, 26)            
    
    
    (solution, num_stack_iterations) = solve_sudoku(input_arr=np.array([[0, 0, 0, 0, 6, 8, 0, 3, 0],
                                                                        [1, 9, 0, 0, 0, 0, 0, 0, 0],
                                                                        [8, 0, 3, 1, 0, 0, 2, 0, 0],
                                                                        [4, 0, 0, 0, 5, 1, 0, 6, 0],
                                                                        [7, 0, 0, 0, 2, 0, 0, 0, 4],
                                                                        [0, 0, 0, 0, 7, 0, 8, 0, 0],
                                                                        [0, 1, 0, 0, 0, 5, 0, 0, 7],
                                                                        [0, 0, 4, 0, 0, 0, 0, 0, 0],
                                                                        [0, 5, 0, 0, 3, 0, 1, 0, 0]]), 
                                                    run_mode = 'MIN_NUM_POSSIBILITIES_FIRST_UNKNOWN',
                                                    debug_output=False)
    np.testing.assert_array_equal(solution,
                                np.array([[2, 4, 7, 5, 6, 8, 9, 3, 1],
                                           [1, 9, 5, 3, 4, 2, 6, 7, 8],
                                           [8, 6, 3, 1, 9, 7, 2, 4, 5],
                                           [4, 3, 9, 8, 5, 1, 7, 6, 2],
                                           [7, 8, 1, 9, 2, 6, 3, 5, 4],
                                           [5, 2, 6, 4, 7, 3, 8, 1, 9],
                                           [3, 1, 2, 6, 8, 5, 4, 9, 7],
                                           [6, 7, 4, 2, 1, 9, 5, 8, 3],
                                           [9, 5, 8, 7, 3, 4, 1, 2, 6]]))    
    #np.testing.assert_equal(num_stack_iterations, 75)        
    np.testing.assert_equal(num_stack_iterations, 30)                
    
    (solution, num_stack_iterations) = solve_sudoku(input_arr=np.array([[0, 0, 0, 0, 6, 8, 0, 3, 0],
                                                                        [1, 9, 0, 0, 0, 0, 0, 0, 0],
                                                                        [8, 0, 3, 1, 0, 0, 2, 0, 0],
                                                                        [4, 0, 0, 0, 5, 1, 0, 6, 0],
                                                                        [7, 0, 0, 0, 2, 0, 0, 0, 4],
                                                                        [0, 0, 0, 0, 7, 0, 8, 0, 0],
                                                                        [0, 1, 0, 0, 0, 5, 0, 0, 7],
                                                                        [0, 0, 4, 0, 0, 0, 0, 0, 0],
                                                                        [0, 5, 0, 0, 3, 0, 1, 0, 0]]), 
                                                    run_mode = 'MAX_NUM_KNOWN_ELEM',
                                                    debug_output=False)
    np.testing.assert_array_equal(solution,
                                np.array([[2, 4, 7, 5, 6, 8, 9, 3, 1],
                                           [1, 9, 5, 3, 4, 2, 6, 7, 8],
                                           [8, 6, 3, 1, 9, 7, 2, 4, 5],
                                           [4, 3, 9, 8, 5, 1, 7, 6, 2],
                                           [7, 8, 1, 9, 2, 6, 3, 5, 4],
                                           [5, 2, 6, 4, 7, 3, 8, 1, 9],
                                           [3, 1, 2, 6, 8, 5, 4, 9, 7],
                                           [6, 7, 4, 2, 1, 9, 5, 8, 3],
                                           [9, 5, 8, 7, 3, 4, 1, 2, 6]]))    
    np.testing.assert_equal(num_stack_iterations, 75)                    
    
    (solution, num_stack_iterations) = solve_sudoku(input_arr=np.array([[0, 0, 0, 0, 6, 8, 0, 3, 0],
                                                                        [1, 9, 0, 0, 0, 0, 0, 0, 0],
                                                                        [8, 0, 3, 1, 0, 0, 2, 0, 0],
                                                                        [4, 0, 0, 0, 5, 1, 0, 6, 0],
                                                                        [7, 0, 0, 0, 2, 0, 0, 0, 4],
                                                                        [0, 0, 0, 0, 7, 0, 8, 0, 0],
                                                                        [0, 1, 0, 0, 0, 5, 0, 0, 7],
                                                                        [0, 0, 4, 0, 0, 0, 0, 0, 0],
                                                                        [0, 5, 0, 0, 3, 0, 1, 0, 0]]), 
                                                    run_mode = 'MIN_NUM_POSSIBILITIES_MAX_NUM_KNOWN_ELEM',
                                                    debug_output=False)
    np.testing.assert_array_equal(solution,
                                np.array([[2, 4, 7, 5, 6, 8, 9, 3, 1],
                                           [1, 9, 5, 3, 4, 2, 6, 7, 8],
                                           [8, 6, 3, 1, 9, 7, 2, 4, 5],
                                           [4, 3, 9, 8, 5, 1, 7, 6, 2],
                                           [7, 8, 1, 9, 2, 6, 3, 5, 4],
                                           [5, 2, 6, 4, 7, 3, 8, 1, 9],
                                           [3, 1, 2, 6, 8, 5, 4, 9, 7],
                                           [6, 7, 4, 2, 1, 9, 5, 8, 3],
                                           [9, 5, 8, 7, 3, 4, 1, 2, 6]]))    
    np.testing.assert_equal(num_stack_iterations, 58)                        
    
    
    (solution, num_stack_iterations) = solve_sudoku(input_arr=np.array([[0, 0, 0, 0, 6, 8, 0, 3, 0],
                                                                        [1, 9, 0, 0, 0, 0, 0, 0, 0],
                                                                        [8, 0, 3, 1, 0, 0, 2, 0, 0],
                                                                        [4, 0, 0, 0, 5, 1, 0, 6, 0],
                                                                        [7, 0, 0, 0, 2, 0, 0, 0, 4],
                                                                        [0, 0, 0, 0, 7, 0, 8, 0, 0],
                                                                        [0, 1, 0, 0, 0, 5, 0, 0, 7],
                                                                        [0, 0, 4, 0, 0, 0, 0, 0, 0],
                                                                        [0, 5, 0, 0, 3, 0, 1, 0, 0]]), 
                                                    run_mode = 'MIN_NUM_POSSIBILITIES_MIN_NUM_KNOWN_ELEM',
                                                    debug_output=False)
    np.testing.assert_array_equal(solution,
                                np.array([[2, 4, 7, 5, 6, 8, 9, 3, 1],
                                           [1, 9, 5, 3, 4, 2, 6, 7, 8],
                                           [8, 6, 3, 1, 9, 7, 2, 4, 5],
                                           [4, 3, 9, 8, 5, 1, 7, 6, 2],
                                           [7, 8, 1, 9, 2, 6, 3, 5, 4],
                                           [5, 2, 6, 4, 7, 3, 8, 1, 9],
                                           [3, 1, 2, 6, 8, 5, 4, 9, 7],
                                           [6, 7, 4, 2, 1, 9, 5, 8, 3],
                                           [9, 5, 8, 7, 3, 4, 1, 2, 6]]))    
    np.testing.assert_equal(num_stack_iterations, 22)
    
def test_obvious_non_obvious_analysis():
    (output_arr, num_zero_elem, num_updations, num_iterations, possible_elems, impact_elems) = \
        do_obvious_analysis(
        input_arr=np.resize([0, 0, 0, 0, 6, 8, 0, 3, 0,
                             1, 9, 0, 0, 0, 0, 0, 0, 0,
                             8, 0, 3, 1, 0, 0, 2, 0, 0,
                             4, 0, 0, 0, 5, 1, 0, 6, 0,
                             7, 0, 0, 0, 2, 0, 0, 0, 4,
                             0, 0, 0, 0, 7, 0, 8, 0, 0,
                             0, 1, 0, 0, 0, 5, 0, 0, 7,
                             0, 0, 4, 0, 0, 0, 0, 0, 0,
                             0, 5, 0, 0, 3, 0, 1, 0, 0], (9,9)))
    np.testing.assert_array_equal(output_arr,
                                  np.array([[0, 0, 0, 0, 6, 8, 0, 3, 0],
                                            [1, 9, 0, 0, 4, 0, 0, 0, 0],
                                            [8, 0, 3, 1, 9, 7, 2, 0, 0],
                                            [4, 0, 0, 0, 5, 1, 0, 6, 0],
                                            [7, 0, 0, 0, 2, 0, 0, 0, 4],
                                            [0, 0, 0, 0, 7, 0, 8, 0, 0],
                                            [0, 1, 0, 0, 8, 5, 0, 0, 7],
                                            [0, 0, 4, 0, 1, 0, 0, 0, 0],
                                            [0, 5, 0, 0, 3, 0, 1, 0, 0]]))
    np.testing.assert_equal(num_zero_elem, 51)
    np.testing.assert_equal(num_updations, 5)    
    np.testing.assert_equal(num_iterations, 2)   
    np.testing.assert_array_equal(possible_elems, 
                                  [[{2, 5}, {2, 4, 7}, {2, 5, 7}, {2, 5}, {6}, {8}, {9, 4, 5, 7}, {3}, {1, 5, 9}], 
                                   [{1}, {9}, {2, 5, 6, 7}, {2, 3, 5}, {4}, {2, 3}, {5, 6, 7}, {8, 5, 7}, {8, 5, 6}], 
                                   [{8}, {4, 6}, {3}, {1}, {9}, {7}, {2}, {4, 5}, {5, 6}], 
                                   [{4}, {8, 2, 3}, {8, 9, 2}, {8, 9, 3}, {5}, {1}, {9, 3, 7}, {6}, {9, 2, 3}], 
                                   [{7}, {8, 3, 6}, {1, 5, 6, 8, 9}, {8, 9, 3, 6}, {2}, {9, 3, 6}, {9, 3, 5}, {1, 5, 9}, {4}], 
                                   [{2, 3, 5, 6, 9}, {2, 3, 6}, {1, 2, 5, 6, 9}, {9, 3, 4, 6}, {7}, {9, 3, 4, 6}, {8}, {1, 2, 5, 9}, {1, 2, 3, 5, 9}], 
                                   [{9, 2, 3, 6}, {1}, {9, 2, 6}, {9, 2, 4, 6}, {8}, {5}, {9, 3, 4, 6}, {9, 2, 4}, {7}], 
                                   [{9, 2, 3, 6}, {2, 3, 6, 7, 8}, {4}, {9, 2, 6, 7}, {1}, {9, 2, 6}, {9, 3, 5, 6}, {8, 9, 2, 5}, {2, 3, 5, 6, 8, 9}], 
                                   [{9, 2, 6}, {5}, {2, 6, 7, 8, 9}, {2, 4, 6, 7, 9}, {3}, {9, 2, 4, 6}, {1}, {8, 9, 2, 4}, {8, 9, 2, 6}]])

    np.testing.assert_array_equal(impact_elems, 
                                  np.array([[ 9,  9,  8,  7, 13,  9,  6,  5,  6],
                                            [ 7,  7,  6,  8, 14, 10,  7,  6,  7],
                                            [10, 10,  9,  9, 15, 11,  9,  8,  9],
                                            [ 7,  8,  7,  7, 12,  9,  8,  7,  7],
                                            [ 6,  7,  6,  7, 12,  9,  7,  6,  6],
                                            [ 6,  7,  6,  6, 11,  8,  6,  5,  5],
                                            [10,  7,  7,  7, 12,  9,  7,  7,  6],
                                            [ 8,  5,  5,  6, 11,  8,  6,  6,  5], 
                                            [ 9,  6,  6,  7, 12,  9,  6,  6,  5]]))
