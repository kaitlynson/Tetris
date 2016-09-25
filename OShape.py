class OShape:
    ROTATIONS = [[[0,1,1],
                  [0,1,1],
                  [0,0,0]]]
    
    def __init__(self):
        self.rotation = 0
        self.shape = OShape.ROTATIONS[0]

    def rotate(self):
        pass

    def delete(self, gameBoard):
        for i in range(2):
            gameBoard.board[gameBoard.x][(gameBoard.y + 1) + i] = 0
            gameBoard.board[gameBoard.x + 1][(gameBoard.y + 1) + i] = 0

    def collideRight(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        if y == gameBoard.COLS - 3:
            ret = True
            
        else:
            ret = gb[x][y + 3] or gb[x + 1][y + 3]
            
        return ret

    def collideLeft(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        if y == -1:
            ret = True
            
        else:
            ret = gb[x][y] or gb[x + 1][y]
            
        return ret

    def collideDown(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        if x == gameBoard.ROWS - 2:
            ret = True
            
        else:
            ret = gb[x + 2][y + 1] or gb[x + 2][y + 2]
            
        return ret

    def canRotate(self, gameBoard):
        return True
        
        
        
        
