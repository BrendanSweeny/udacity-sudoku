correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# This function simply checks if the specified value exists in the row/column
def findNumber(row, number):
  if number in row:
    return True
  return False

def checkRow(sudoku):
  for row in sudoku:
    number = 1 # the value to be checked
    while number <= len(row): # the largest number should be equal to the length of a row
      if findNumber(row, number) == True:
        number += 1
      else:
        return False
  return True

def checkColumn(sudoku):
  index = 0
  while index < len(sudoku):
    column = []
    number = 1
    for row in sudoku:
      column.append(row[index]) # a new list is assigned to column that includes value at a specific index
    while number <= len(column): # the largest number should be equal to the length of a column
      if findNumber(column, number) == True:
        number += 1
      else:
        return False
    index += 1
  return True

def check_sudoku(sudoku):
  if checkRow(sudoku) == True and checkColumn(sudoku) == True:
    return True
  return False
    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False

'''print checkColumn(correct)
print checkColumn(incorrect)
print checkColumn(incorrect2)
print checkColumn(incorrect3)
print checkColumn(incorrect4)
print checkColumn(incorrect5)'''

'''print checkRow(correct)
print checkRow(incorrect)
print checkRow(incorrect2)
print checkRow(incorrect3)
print checkRow(incorrect4)
print checkRow(incorrect5)'''
