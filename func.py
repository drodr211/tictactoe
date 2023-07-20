import array
import pygame
import time

def checkWin(bd, pnum):
    if checkRow(bd[0], pnum):
        return True
    if checkRow(bd[1], pnum):
        return True
    if checkRow(bd[2], pnum):
        return True
    if checkDiagonals(bd, pnum):
        return True
    if checkColumns(bd, pnum):
        return True
    else: return False
    
def checkRow(list, num):
    return all(i == num for i in list)

def checkColumns(bd, num):
    if checkRow([bd[0][0], bd[1][0], bd[2][0]], num):
        return True
    if checkRow([bd[0][1], bd[1][1], bd[2][1]] , num):
        return True
    if checkRow([bd[0][2], bd[1][2], bd[2][2]] , num):
        return True
    else: return False

def checkDiagonals(bd, num):
    if checkRow([bd[0][0], bd[1][1], bd[2][2]], num):
        return True
    if checkRow([bd[2][0], bd[1][1], bd[0][2]], num):
        return True
    else: return False

def checkClick(bd, b, turn):
    for i, row in enumerate(b):
                for j, column in enumerate(row):
                    if bd[i][j] == 0:
                        if column.collidepoint(pygame.mouse.get_pos()):
                            bd[i][j] = turn % 2 + 1
                            return turn + 1 
def columnY(i):
    return ((i+1)*150)+50

def checkDraw(bd):
    temp = [bd[0][0], bd[0][1], bd[0][2], 
            bd[1][0], bd[1][1], bd[1][2],
            bd[2][0], bd[2][1], bd[2][2]]
    return all(i != 0 for i in temp)

    