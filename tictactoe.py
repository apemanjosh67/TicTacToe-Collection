#Josh Muszka
#January 29, 2021
#Last updated: February 1, 2021
#TicTacToe program--left click to place an X
#has turns, scoring, and game-ending (including draws), and computer AI

import pygame, sys, time, random

pygame.init()

#refresh rate
FPS = 144

#screen info
width, height = 600, 600
size = width, height
screen = pygame.display.set_mode(size)

#game info

GRID = 3
board=[] #0 if space hasn't been filled, 1 if filled by x, -1 if filled by o

#set up board
for i in range(GRID):
    row = []
    for j in range(GRID):
        row.append(0)
    board.append(row)

XX = 1
OO = -1
isPlayerTurn = True #take turns between player and computer
game_won = False
draw_flag = 6 #returns this value if game is a draw (if no winner yet no empty squares remain)
prev_time = time.time()
current_time = time.time()


#colors
background_color = 0xFF, 0xE5, 0xAB 
line_color = 0x6E, 0x1D, 0x1D

def check_score():

    win_check = 0
    global game_won
    #check for vertical winner
    for i in range(GRID):
        for j in range(GRID):
            win_check += board[i][j]
        if win_check == GRID*XX:
            game_won = True
            return win_check
        if win_check == GRID*OO:
            game_won = True
            return win_check
        win_check = 0
    
    #check for horizontal winner
    for i in range(GRID):
        for j in range(GRID):
            win_check += board[j][i]
        if win_check == GRID*XX:
            game_won = True
            return win_check
        if win_check == GRID*OO:
            game_won = True
            return win_check
        win_check = 0

    #check diagonal topleft-bottomright winner
    for i in range(GRID):
        win_check += board[i][i]
        if win_check == GRID*XX:
            game_won = True
            return win_check
        if win_check == GRID*OO:
            game_won = True
            return win_check
    win_check = 0

    #check diagonal topright-bottomleft winner
    for i in range(GRID):
        win_check += board[i][GRID-i-1]
        if win_check == GRID*XX:
            game_won = True
            return win_check
        if win_check == GRID*OO:
            game_won = True
            return win_check

    #check for empty square
    for i in range(GRID):
        for j in range(GRID):
            if board[i][j] == 0:
                return
    game_won = True
    return draw_flag
    
def computerTurn():

    #scan board
    #if computer has a chance to win, place O
    #if player has a chance to win, place O
    #else, place random O

    #check for computer victory

    check_board = 0
    #horizontally
    for i in range(GRID):
        for j in range (GRID):
            check_board += board[j][i]
        
        #if there is one empty space in row
        if check_board == (GRID-1)*OO:
            for j in range (GRID):
                #check to see which space is the empty one
                if board[j][i] == 0:
                    board[j][i] = OO
                    return
        check_board = 0

    #vertically
    for i in range(GRID):
        for j in range (GRID):
            check_board += board[i][j]
        
        #if there is one empty space in row
        if check_board == (GRID-1)*OO:
            for j in range (GRID):
                #check to see which space is the empty one
                if board[i][j] == 0:
                    board[i][j] = OO
                    return
        check_board = 0

    #diagonally topleft bottom right
    for i in range(GRID):
        check_board += board[i][i]
    if check_board == (GRID-1)*OO:
        for i in range(GRID):
            if board[i][i] == 0:
                board[i][i] = OO
                return
    check_board = 0

    #diagonally topright bottomleft
    for i in range(GRID):
        check_board += board[i][GRID-1-i]
    if check_board == (GRID-1)*OO:
        for i in range(GRID):
            if board[i][GRID-1-i] == 0:
                board[i][GRID-1-i] = OO
                return
    check_board = 0


    #check to prevent player victory

    #horizontally
    for i in range(GRID):
        for j in range (GRID):
            check_board += board[j][i]
        
        #if there is one empty space in row
        if check_board == (GRID-1)*XX:
            for j in range (GRID):
                #check to see which space is the empty one
                if board[j][i] == 0:
                    board[j][i] = OO
                    return
        check_board = 0

    #vertically
    for i in range(GRID):
        for j in range (GRID):
            check_board += board[i][j]
        
        #if there is one empty space in row
        if check_board == (GRID-1)*XX:
            for j in range (GRID):
                #check to see which space is the empty one
                if board[i][j] == 0:
                    board[i][j] = OO
                    return
        check_board = 0

    #diagonally topleft bottom right
    for i in range(GRID):
        check_board += board[i][i]
    if check_board == (GRID-1)*XX:
        for i in range(GRID):
            if board[i][i] == 0:
                board[i][i] = OO
                return
    check_board = 0

    #diagonally topright bottomleft
    for i in range(GRID):
        check_board += board[i][GRID-1-i]
    if check_board == (GRID-1)*XX:
        for i in range(GRID):
            if board[i][GRID-1-i] == 0:
                board[i][GRID-1-i] = OO
                return
    check_board = 0


    #if there were no other spaces to win / block player from winning
    i = random.randint(0,GRID-1)
    j = random.randint(0,GRID-1)
    while board[i][j] != 0:
        i = random.randint(0,GRID-1)
        j = random.randint(0,GRID-1)
    board[i][j] = OO
    return

def random_wait_time():
    return random.uniform(1.0,3.0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_won:
                left, middle, right = pygame.mouse.get_pressed()
                if left:
                    x,y = pygame.mouse.get_pos()
                    x = int((x/width)*GRID)
                    y = int((y/height)*GRID)
                    if isPlayerTurn and board[x][y] == 0:
                        board[x][y] = XX
                        isPlayerTurn = False
                    prev_time = time.time()

    screen.fill(background_color)

    #draw border
    pygame.draw.line(screen, line_color, (0,0), (0,height-2), 4)
    pygame.draw.line(screen, line_color, (0,0), (width-2,0), 4)
    pygame.draw.line(screen, line_color, (width-2, 0), (width-2, height-2), 4)
    pygame.draw.line(screen, line_color, (0, height-2), (width-2, height-2), 4)

    #set window title status
    if not game_won:
        if isPlayerTurn:
            pygame.display.set_caption("Player Turn!")
        else:
            pygame.display.set_caption("Computer Turn!")

    for i in range(GRID):
        for j in range(GRID):
            x1 = (width/GRID)*i
            y1 = (height/GRID)*j

            #draw gridlines
            pygame.draw.line(screen, line_color, (x1,0), (x1,height), 4)
            pygame.draw.line(screen, line_color, (0,y1), (width, y1), 4)

            x2 = (width/GRID)*(i)
            y2 = (width/GRID)*(j)



            #draw x's and o's
            if board[i][j] == XX:
                #pygame.draw.line(screen, line_color, (0, 0), (width/GRID,height/GRID))
                #pygame.draw.line(screen, line_color, (0, height/GRID), (width/GRID,0))
                x = i+1
                y= j+1
                pygame.draw.line(screen, line_color, ((width/GRID)*i,(height/GRID)*j),((width/GRID)*x,(width/GRID)*y), 8)
                pygame.draw.line(screen, line_color, ((width/GRID)*x,(height/GRID)*j),((width/GRID)*i,(height/GRID)*y), 8)
            if board[i][j] == OO:
                x = i+1
                y = j+1
                pygame.draw.circle(screen, line_color, ((width/GRID)*i + width/GRID/2,(height/GRID)*j + height/GRID/2), width/GRID/2, 6)

    if check_score() == XX*GRID:
        pygame.display.set_caption("Player wins")
    if check_score() == OO*GRID:
        pygame.display.set_caption("Computer wins")
    if check_score() == draw_flag:
        pygame.display.set_caption("Draw")

    #computer turn
    if not isPlayerTurn and not game_won:
        current_time = time.time()
        if current_time - prev_time > random_wait_time():
            computerTurn()
            isPlayerTurn = True

    time.sleep(1/FPS)
    pygame.display.update()
