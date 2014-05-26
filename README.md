udacity-sudoku
==============

checks a modified sudoku puzzle for correctness

My answer to Udacity CS101 PS 3-8:

Define a procedure, check_sudoku,
that takes as input a square list
of lists representing an n x n
sudoku puzzle solution and returns the boolean
True if the input is a valid
sudoku square and returns the boolean False
otherwise.

A valid sudoku square satisfies these
two properties:

1. Each column of the square contains
   each of the whole numbers from 1 to n exactly once.

2. Each row of the square contains each
   of the whole numbers from 1 to n exactly once.

You may assume the the input is square and contains at
least one row and column.
