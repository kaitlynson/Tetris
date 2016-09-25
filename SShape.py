class SShape:
    ROTATIONS = [[[0,0,0],
                  [0,1,1],
                  [1,1,0]],#ROTATIONS[0]
                 [[1,0,0],
                  [1,1,0],#ROTATIONS[1]
                  [0,1,0]]]

    def __init__(self):
        self.rotation = 0
        self.shape = SShape.ROTATIONS[0]

    def rotate(self):
        self.rotation += 1
        self.rotation %= 2
        self.updateRotation()

    def updateRotation(self):
        self.shape = SShape.ROTATIONS[self.rotation]

    def delete(self, gameBoard):
        if self.rotation == 0:
            for i in range(2):
                gameBoard.board[gameBoard.x + 1][(gameBoard.y + 1) + i] = 0
                gameBoard.board[gameBoard.x + 2][gameBoard.y + i] = 0
                    
        if self.rotation == 1:
            for i in range(2):
                gameBoard.board[gameBoard.x + i][gameBoard.y] = 0
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
                ret =  gb[x+1][y + 3] or gb[x + 2][y + 2]
        else:
            if y == gameBoard.COLS - 2:
                ret = True
            else:
                ret = gb[x][y + 1] or gb[x + 1][y + 2] or gb[x + 2][y + 2]
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
                ret =  gb[x+2][y-1] or gb[x + 1][y]
        else:
            if y == 0:
                ret = True
            else:
                ret = gb[x][y-1] or gb[x + 1][y-1] or gb[x + 2][y]
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
                ret =  gb[x + 3][y] or gb[x + 3][y + 1] or gb[x + 2][y + 2]
        else:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret = gb[x + 2][y] or gb[x + 3][y + 1]
        return ret
    
    def canRotate(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = True
        if self.rotation == 0:
            ret = not(gb[x + 1][y] or gb[x][y])
        else:
            if y == gameBoard.COLS - 2:
                ret = False
            else:
                ret = not(gb[x + 2][y] or gb[x + 1][y + 2])
        return ret
