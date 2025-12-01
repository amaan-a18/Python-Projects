"""The sudoku is represented as follows:
1. The empty cells are represented as "?"
2. The confirmed cells are represented with a number.

The sudoku which we will be testing is as follows:

? ? ? 8 ? 1 ? ? ?

? ? ? ? ? ? 4 3 ?

5 ? ? ? ? ? ? ? ?

? ? ? ? 7 ? 8 ? ?

? ? ? ? ? ? 1 ? ?

? 2 ? ? 3 ? ? ? ?

6 ? ? ? ? ? ? 7 5

? ? 3 4 ? ? ? ? ?

? ? ? 2 ? ? 6 ? ?
"""

board = [["?" for _ in range(9)] for _ in range(9)]
board[0][3] = 8
board[0][5] = 1
board[1][6] = 4
board[1][7] = 3
board[2][0] = 5
board[3][4] = 7
board[3][6] = 8
board[4][6] = 1
board[5][1] = 2
board[5][4] = 3
board[6][0] = 6
board[6][7] = 7
board[6][8] = 5
board[7][2] = 3
board[7][3] = 4
board[8][3] = 2
board[8][6] = 6
unknownValues = [x for x in range(1,10)]
print(unknownValues)

for row in board:
  print(row)

"""1. Instantiate the problem."""

from constraint import *
sudoku = Problem()

"""2. Create the variables"""

for i in range(len(board)):
  row = board[i]
  #print("i = ", i)
  for j in range(len(row)):
    col = row[j]
    #print("j = ", j)
    if col == "?":
      sudoku.addVariable((i,j), unknownValues)
    else:
      print([col])
      sudoku.addVariable((i,j), [col])

"""2. Create the constraints."""

def getRowList(i):
  ret = []
  for j in range(9):
    ret.append((i,j))
  return ret

def getColList(j):
  ret = []
  for i in range(9):
    ret.append((i,j))
  return ret

#Here, we are hard-coding the boxes.
def getBoxes():
  ret = [[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
         [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
         [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
         [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
         [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
         [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
         [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
         [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
         [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]
         ]
  return ret

from re import A
boxes = getBoxes()
for box in boxes:
  sudoku.addConstraint(AllDifferentConstraint(), box)
for i in range(9):
  sudoku.addConstraint(AllDifferentConstraint(), getRowList(i))
  sudoku.addConstraint(AllDifferentConstraint(), getColList(i))

"""Finally, get the solution"""

solution = sudoku.getSolution()
answer = [["?" for x in range(9)] for y in range(9)]

print(solution)
for var in solution:
  answer[var[0]][var[1]] = solution[var]

for i in range(9):
  for j in range(9):
    print(answer[i][j], end=" ")  #To make sure that we have the next number on the same row
  print("") #print a new line