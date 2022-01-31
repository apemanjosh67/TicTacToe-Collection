import pygame, sys, time

pygame.init()

#refresh rate
FPS = 144

#screen info
width, height = 600, 600
size = width, height
screen = pygame.display.set_mode(size)

#game info
GRID = 3
board=[] #0 if space hasn't been filled, 1 if filled by x, -1 if filled by 
for i in range(GRID*GRID):
    board.append([0,0,0])
XX = 1
OO = -1
isPlayerTurn = True #take turns between player and computer
game_won = False

#colors
background_color = 0xFF, 0xE5, 0xAB 
line_color = 0x6E, 0x1D, 0x1D

def check_score():

    win_check = 0
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

    #check diagonal topright-bottomleft winner
    for i in range(GRID):
        win_check += board[i][GRID-i-1]
        if win_check == GRID*XX:
            game_won = True
            return win_check
        if win_check == GRID*OO:
            game_won = True
            return win_check


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                x,y = pygame.mouse.get_pos()
                x = int((x/width)*GRID)
                y = int((y/height)*GRID)
                if isPlayerTurn and board[x][y] == 0:
                    board[x][y] = XX
                    isPlayerTurn = False

            if right:
                x,y = pygame.mouse.get_pos()
                x = int((x/width)*GRID)
                y = int((y/height)*GRID)
                if not isPlayerTurn and board[x][y] == 0:
                    board[x][y] = OO
                    isPlayerTurn = True


    screen.fill(background_color)

    #draw border
    pygame.draw.line(screen, line_color, (0,0), (0,height-2), 4)
    pygame.draw.line(screen, line_color, (0,0), (width-2,0), 4)
    pygame.draw.line(screen, line_color, (width-2, 0), (width-2, height-2), 4)
    pygame.draw.line(screen, line_color, (0, height-2), (width-2, height-2), 4)

    #set window title status
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
                pygame.draw.circle(screen, line_color, ((width/GRID)*i + width/6,(height/GRID)*j + height/6), width/6, 6)

    if check_score() == XX*GRID:
        pygame.display.set_caption("Player wins")
    if check_score() == OO*GRID:
        pygame.display.set_caption("Computer wins")

    time.sleep(1/FPS)
    pygame.display.update()