class ZShape:
    ROTATIONS = [[[0,0,0],
                  [1,1,0],
                  [0,1,1]],#ROTATIONS[0]
                 [[0,0,1],
                  [0,1,1],#ROTATIONS[1]
                  [0,1,0]]]
                
    def __init__(self):
        self.rotation = 0
        self.shape = ZShape.ROTATIONS[0]

    def rotate(self):
        self.rotation += 1
        self.rotation %= 2
        self.updateRotation()

    def updateRotation(self):
        self.shape = ZShape.ROTATIONS[self.rotation]

    def delete(self, gameBoard):
        if self.rotation == 0:
            for i in range(2):
                gameBoard.board[gameBoard.x + 1][gameBoard.y + i] = 0
                gameBoard.board[gameBoard.x + 2][(gameBoard.y + 1) + i] = 0
        else:
            for i in range(2):
                gameBoard.board[gameBoard.x + i][gameBoard.y + 2] = 0
                gameBoard.board[(gameBoard.x + 1) + i][gameBoard.y + 1] = 0

    def collideRight(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if y == gameBoard.COLS - 3:
                ret = True
            else:
                ret =  gb[x+1][y + 2] or gb[x + 2][y + 3]
        else:
            if y == gameBoard.COLS - 3:
                ret = True
            else:
                ret = gb[x][y + 3] or gb[x + 1][y + 3] or gb[x + 2][y + 2]
        return ret

    def collideLeft(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if y == 0:
                ret = True
            else:
                ret =  gb[x+2][y] or gb[x + 1][y-1]
        else:
            if y == -1:
                ret = True
            else:
                ret = gb[x][y + 1] or gb[x + 1][y] or gb[x + 2][y]
        return ret

    def collideDown(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret =  gb[x + 3][y + 2] or gb[x + 3][y + 1] or gb[x + 2][y]
        else:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret = gb[x + 2][y + 2] or gb[x + 3][y + 1]
        return ret
    
    def canRotate(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = True
        if self.rotation == 0:
            ret = not(gb[x + 1][y + 2] or gb[x][y + 2])
        else:
            if y == -1:
                ret = False
            else:
                ret = not(gb[x + 2][y + 2] or gb[x + 1][y])
        return ret


    
