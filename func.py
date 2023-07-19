import array

def checkWin(bd, pnum):
    win = False
    if checkRow(bd[0], pnum):
        win = True
    if checkRow(bd[1], pnum):
        win = True
    if checkRow(bd[2], pnum):
        win = True
    if checkDiagonals(bd, pnum):
        win = True
    if checkColumns(bd, pnum):
        win = True
    
    return win

def checkRow(list, num):
    return all(i == num for i in list)

def checkColumns(bd, num):
    c1 = [bd[0][0], bd[1][0], bd[2][0]] 
    c2 = [bd[0][1], bd[1][1], bd[2][1]] 
    c3 = [bd[0][2], bd[1][2], bd[2][2]] 

    if checkRow(c1, num):
        return True
    if checkRow(c2, num):
        return True
    if checkRow(c3, num):
        return True
    else: return False

def checkDiagonals(bd, num):
    d1 = [bd[0][0], bd[1][1], bd[2][2]] 
    d2 = [bd[2][0], bd[1][1], bd[0][2]] 

    if checkRow(d1, num):
        return True
    if checkRow(d2, num):
        return True
    else: return False