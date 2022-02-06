#global variables

#It is used to define the size of the box, it contains size*size grid boxes
size = 4

#It is used to take input 
inp = ""

#Functions
import random


#When we start the game, we need to assign any of the grid box with 2 or 4, I'm starting it with 2 
#the startGame() begins the game that we play and creates the big grid 
def startGame():
    index = 0
    grid = []
    for _ in range(size**2):
        if (index < (size**2)-1):
            grid.append(0)
        else:
            grid.append(2)
        index = index+1
    return grid

#Everytime after we make a particular move , we need to print the updated grid 
# The printGrid() function takes grid as paramter and prints the grid 
def printGrid(grid):
    index = 0
    for _ in range(size):
        print("   ",end='')
        for _ in range(size):
            print(grid[index], end="    ")
            index = index + 1
        print("")
        print("")



#It returns a particular column as a list
#Some times to make operations on a particular column we need that single column 
#So at that time getCol() is used retrive that particular column
def getCol(grid, colNum):
    column = []
    index = colNum - 1
    for _ in range(size):
        column.append(grid[index])
        index = index + size
    return column

#To make easy updates we need to rotate our grid sometimes 
# The rotateAntiClock() function takes grid as a paramter and rotates it in Anticlock Wise Direction
def rotateAntiClock(grid):
    grid2 = []
    colNum = size
    for _ in range(size):
        col = getCol(grid, colNum)
        for num in col:
            grid2.append(num)
        colNum = colNum-1
    grid[:] = grid2

# It returns the number of empty spaces in a given list with a between a starting and ending index inclusive
#It makes sures that the game was still not over and there is a move to play
def empty(row, low_limit, high_limit, index):
    count = 0
    for i in range(low_limit, high_limit):
        if row[i] == 0:
            index.append(i)
            count = count+1
    return count

#gets all the indices in the grid with no values and randomly selects a 
# value either 2 or 4 and adds it to that position in the grid
def addVal(grid):
    rand = random.choice([2, 4])
    index = []
    empty(grid, 0, size**2, index)
    rand2 = random.choice(index)
    grid[rand2] = rand

#The arrange() function arranges all the empty spaces on the right side and all the numbers on the left
def arrange(grid, low_limit, high_limit):
    index = [] #will not use this for the arrange function but this is required to call the empty function
    numZero = empty(grid, low_limit, high_limit-1, index)
    count1 = 0
    while count1 <= numZero:
        for i in range(low_limit,high_limit-1):
            if grid[i] == 0:
                grid[i] = grid[i+1]
                grid[i+1] = 0
        count1 = count1+1


#This function is used to make lefe move of all the elements
def move_row_left(grid, low_limit, high_limit):
    grid_copy = grid[:]
    arrange(grid, low_limit, high_limit)

    for i in range(low_limit, high_limit-1):
        if (grid[i] == grid[i+1]) and (grid[i] != 0):
            grid[i] = 2*grid[i]
            grid[i+1] = 0
    
    arrange(grid, low_limit, high_limit)
    if(grid_copy == grid):
        return False
    return True

#moves the whole grid left
def moveLeft(grid):
    c = False
    changed = False
    #I use "changed" to determine if the grid changed after a move to the left or if the move did not do anything
    for i in range(size):
        low_limit = i*size
        high_limit = low_limit + size
        c = move_row_left(grid, low_limit, high_limit)
        if(c):
            changed = True
    return changed

# To move our whole grid right we use moveRight() function 
# I'm making every move to be on the left side and call the moveLeft() function and again retaining its original position.
def moveRight(grid):
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    #After two rotations right it becomes left 
    u = moveLeft(grid)
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    #Again we are putting it back in its original position
    return u

# To move our whole grid up we use moveUp() function 
def moveUp(grid):
    #After one rotation up becomes left 
    rotateAntiClock(grid)
    #
    u = moveLeft(grid)
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    #Again we are putting it back in its original position
    return u
    
# To move our whole grid down we use moveDown() function 
def moveDown(grid):
    #After three rotations down becomes left 
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    u = moveLeft(grid)
    rotateAntiClock(grid)
    #Again we are putting it back in its original position
    return u

#So after making every move , the winGame() function will be called and checks if we got 2048 or not. 
def winGame(grid):
    for i in range(size):
        for j in range(size):
            if grid[i][j]==2048:
                print("Game Won")
                return True 
                
    return False


# If we dont have any move to go either left or Right or Down or Up then our game is over 
#The endGame() function stops the program
def endGame(grid):
    grid2 = grid[:]
    if moveLeft(grid2) == False and moveDown(grid2) == False and moveRight(grid2) == False and moveUp(grid2) == False:
        return True
    elif(inp == "quit"):
        return True
    return False

#Everytime when we make a move we need to add a random value into the grid and also print the grid 
#Also we need to check if we have reached 2048 or not, so we also need to call the winGame to check 
# makeMove() function class those two functions from its body
def makeMove(grid):
    addVal(grid)
    printGrid(grid)
    winGame(grid)
    
#Main code
#From this point the main function starts
grid = startGame()
print("This is the start of the game")
print("")
instructions()


printGrid(grid)
count = 0
while(endGame(grid) == False):
     print("Type '1' for left\n  '2' for right\n  '3' for up\n  '4' for down")
    inp = input("What is your move?")
    print("")
    if inp == "1":
        if(moveLeft(grid)):
            makeMove(grid)
        else:
            print("Make a valid move!!")
            print("")
    
    elif inp == "2":
        if(moveRight(grid)):
            makeMove(grid)
        else:
            print("Make a valid move!!")
            print("")

    elif inp == "3":
        if(moveUp(grid)):
            makeMove(grid)
        else:
            print("Make a valid move!!")
            print("")

    elif inp == "4":
        if(moveDown(grid)):
            makeMove(grid)
        else:
            print("Make a valid move!!")
            print("")
    else:
        print("Wrong button pressed!!!")
    count = count+1
    highest = max(grid)

print("Your game has ended!")
print("")
print("Your score is: " + str(count) + " moves and the highest number you got is: " + str(highest))

