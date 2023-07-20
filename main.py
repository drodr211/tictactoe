import pygame
from array import *
from func import *
import time

pygame.init()

window = pygame.display.set_mode((750, 750))
FONT = pygame.font.Font(pygame.font.get_default_font(), 36)
board = [[pygame.Rect((150, 150, 150, 150)), pygame.Rect((300, 150, 150, 150)), pygame.Rect((450, 150, 150, 150))],
         [pygame.Rect((150, 300, 150, 150)), pygame.Rect((300, 300, 150, 150)), pygame.Rect((450, 300, 150, 150))],
         [pygame.Rect((150, 450, 150, 150)), pygame.Rect((300, 450, 150, 150)), pygame.Rect((450, 450, 150, 150))]]
boarddata = [[0,0,0], [0,0,0], [0,0,0] ]
turn = 0
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

p1score = [0,0,0]
p2score = [0,0,0]

run = True
while run:
    window.fill((204, 204, 204))

    p = 1
    if turn % 2 == 1:
        p = 2
    text_surface = FONT.render("Player " +str(p)+ " turn", True, (0, 0, 0))
    #draws board
    for row in board: 
        for rect in row:
            pygame.draw.rect(window, black, rect, 2)
    #chek for any clicks of button presses or quits
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            turn = checkClick(boarddata, board, turn)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: run = False
        if event.type == pygame.QUIT:
            run = False
    #draws turn pieces
    for i, row in enumerate(boarddata):
        for j, column in enumerate(row):
            if column != 0:
                temp = pygame.Rect((150*j+200), columnY(i), 50, 50)
                if column == 1: pygame.draw.rect(window, blue, temp)     
                elif column == 2: pygame.draw.rect(window, red, temp) 

    p1 = FONT.render("P1: "+str(p1score[0])+"-"+str(p1score[1])+"-"+str(p1score[2]), True, blue)
    p2 = FONT.render("P2: "+str(p2score[0])+"-"+str(p2score[1])+"-"+str(p2score[2]), True, red)
       
    #update window
    window.blit(text_surface, dest=(270,630))
    window.blit(p1, dest=(0,0))
    window.blit(p2, dest=(0,50))

    pygame.display.flip()
    #chek win conditions
    check_win1 = checkWin(boarddata, 1)
    check_win2 = checkWin(boarddata, 2)
    if check_win1 or check_win2:
        if check_win1:
            game_win = FONT.render("Player 1 wins", True, blue)
            p1score[0] += 1
            p2score[1] += 1
        elif check_win2:
            game_win = FONT.render("Player 2 wins", True, red)
            p2score[0] += 1
            p1score[1] += 1
       
        window.blit(game_win, dest=(250,100))
        turn = 0
        boarddata = [[0,0,0], [0,0,0], [0,0,0]]
        pygame.display.flip()
        time.sleep(3)

    if checkDraw(boarddata):
        p1score[2] += 1
        p2score[2] += 1
        draw = FONT.render("Draw", True, black)
        window.blit(draw, dest=(330,100))
        turn = 0
        boarddata = [[0,0,0], [0,0,0], [0,0,0]]
        pygame.display.flip()
        time.sleep(3)

pygame.quit()