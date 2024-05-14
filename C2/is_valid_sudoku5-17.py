import collections
import math
from typing import List

def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # Return true if subarray
    
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block != len(set(block)))
    
    n = len(partial_assignment)
    # Check row and column constraints
    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or has_duplicate([partial_assignment[j][i] for j in range(n)])
        for i in range(n)
    ):
        return False