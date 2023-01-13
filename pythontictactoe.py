#print board
def board(grid):
  print("012") 
  for col in range(0,3):
    for row in range(0,3):
      print(grid[col][row],end='')
    print(col,' ')

#switch player
def switch(currentplayer):
  player = True
  if currentplayer == True:
    player = False  #no switch
  else:
    player = True  #switching 
  return player

#symboles
def insymbole(currentplayer):
  if currentplayer :
    return 'X'
  return 'O'

#checking row number
def checkrow(row):
  while row >= 3 or row< 0:
    row = int(input('out of bound. try again'))
  return row
  
#checking col number
def checkcol(col):
  while col >= 3 or col< 0:
    col = int(input('out of bound. try again'))
  return col

## check row
def checkRowWin(grid):
  for i in range(0, len(grid)):
    if ((grid[i][0] == grid[i][1]) and (grid[i][1] == grid[i][2]) and (grid[i][0] != '-')): 
      return True
  return False

##check col win
def checkColWin(grid):
  for j in range(0, len(grid)):
    if ((grid[0][j] == grid[1][j]) and (grid[1][j] == grid[2][j]) and (grid[0][j] != '-')):
      return True
  return False  
  
#check diagonal win 
def checkDiagonalWin(grid):
  if ((grid[0][0] == grid[1][1]) and (grid[1][1] == grid[2][2]) and (grid[0][0] != '-')): 
  
	  return True

  elif ((grid[0][2] == grid[1][1]) and (grid[1][1] == grid[2][0]) and (grid[0][2] != '-')):
	  return True
  
  return False;  
    

#global varibles
row = 0 
column = 0 
player1IsPlaying = True
gameEnd = False
counter= 0 

#intro
player1 = input('what is your name player 1? ')
player2 = input('what is your name player 2? ')
print(player1, "is X, ", player2, "is O")

grid = [['','',''],['','',''],['','','']]
for col in range(0,3):
    for row in range(0,3):
        grid[col][row] = '-'

while not gameEnd:
  board(grid)
  symbole = insymbole(player1IsPlaying)
  
  if player1IsPlaying:
    print(player1, 'should draw')
  else:
    print(player2, 'should draw')
  
  row = int(input('enter row number'))
  realrow = checkrow(row)
  
  col = int(input('enter col number'))
  realcol = checkrow(col) 
  
  while grid[realrow][realcol] != '-':
    print('Full!!try again')
    
    row = int(input('enter row number'))
    realrow = checkrow(row)
    
    col = int(input('enter col number'))
    realcol = checkrow(col)
  
  grid[realrow][realcol] = symbole
  
  if checkRowWin(grid) or  checkColWin(grid) or checkDiagonalWin(grid) == True:
    if player1IsPlaying:
      print(player1, 'is the winner')
      gameEnd = True
    else:
      print(player2, 'is the winner')
      gameEnd = True      
  elif checkRowWin(grid) or  checkColWin(grid) or checkDiagonalWin(grid) == False:
    print('Game not finished')
    player1IsPlaying = switch(player1IsPlaying)
    counter+= 1
  newcounter = counter
  if newcounter == 9:
    print('cats game no winner')
    gameEnd = True
    
board(grid)
    
