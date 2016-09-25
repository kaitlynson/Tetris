class TShape:
    ROTATIONS = [[[0,1,0],
                  [1,1,1],
                  [0,0,0]],#ROTATIONS[0]
                 [[0,1,0],
                  [0,1,1],#ROTATIONS[1]
                  [0,1,0]],
                 [[0,0,0],
                  [1,1,1],
                  [0,1,0]],#ROTATIONS[2]
                 [[0,1,0],
                  [1,1,0],
                  [0,1,0]]]#ROTATIONS[3]   Change these to three by three
                                        #boxes make sure to validate different
                                        #lines depending on different
                                        #shapes and rotations

    
    def __init__(self):
        self.rotation = 0   #each rotation of each shape: 0, 1, 2, 3
        self.shape = TShape.ROTATIONS[0] #sets what the current rotation
                                         #the shape will be in

    def rotate(self):
        self.rotation += 1 #rotation is changed
        self.rotation %= 4 #this makes is so rotation will
                           #either be 0, 1, 2, 3
        self.updateRotation()

    def updateRotation(self):#updates which shape should be drawn onto board
        self.shape = TShape.ROTATIONS[self.rotation]

    def delete(self, gameBoard):#checks where ever there is a 1 and deletes it
        if self.rotation == 0:
            gameBoard.board[gameBoard.x][gameBoard.y + 1] = 0
            for i in range(3):
                gameBoard.board[gameBoard.x + 1][gameBoard.y + i] = 0
                
        elif self.rotation == 1:
            for i in range(3):
                gameBoard.board[gameBoard.x + i][gameBoard.y + 1] = 0
            gameBoard.board[gameBoard.x + 1][gameBoard.y + 2] = 0
            
        elif self.rotation == 2:
            for i in range(3):
                gameBoard.board[gameBoard.x + 1][gameBoard.y + i] = 0
            gameBoard.board[gameBoard.x + 2][gameBoard.y + 1] = 0
            
        else:
            for i in range(3):
                gameBoard.board[gameBoard.x + i][gameBoard.y + 1] = 0
            gameBoard.board[gameBoard.x + 1][gameBoard.y] = 0

    def collideRight(self, gameBoard): #check if a piece can move to the right
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if y == gameBoard.COLS - 3:
                ret = True
            else:
                ret =  gb[x][y + 2] or gb[x + 1][y + 3]
                
        elif self.rotation == 1:
            if y == gameBoard.COLS - 3:
                ret = True
            else:
                ret = gb[x][y + 2] or gb[x + 1][y + 3] or gb[x + 2][y + 2]
                
        elif self.rotation == 2:
            if y == gameBoard.COLS - 3:
                ret = True
            else:
                ret = gb[x + 2][y + 2] or gb[x + 1][y + 3]
                
        else:
            if y == gameBoard.COLS - 2:
                ret = True
            else:
                ret = gb[x][y + 2] or gb[x + 1][y + 2] or gb[x + 2][y + 2]
                
        return ret

    def collideLeft(self, gameBoard): #check if a piece can move to the left
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if y == 0:
                ret = True
            else:
                ret =  gb[x][y] or gb[x + 1][y - 1]
                
        elif self.rotation == 1:
            if y == -1:
                ret = True
            else:
                ret = gb[x][y] or gb[x + 1][y] or gb[x + 2][y]
                
        elif self.rotation == 2:
            if y == 0:
                ret = True
            else:
                ret = gb[x + 1][y - 1] or gb[x + 2][y]
                
        else:
            if y == 0:
                ret = True
            else:
                ret = gb[x][y] or gb[x + 1][y - 1] or gb[x + 2][y]
                
        return ret

    def collideDown(self, gameBoard): #check if the piece can move down
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if x == gameBoard.ROWS - 2:
                ret = True
            else:
                ret =  gb[x + 2][y] or gb[x + 2][y + 1] or gb[x + 2][y + 2]
                
        elif self.rotation == 1:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret = gb[x + 3][y + 1] or gb[x + 2][y + 2]
                
        elif self.rotation == 2:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret = gb[x + 2][y] or gb[x + 3][y + 1] or gb[x + 2][y + 2]
                
        else:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret = gb[x + 2][y] or gb[x + 3][y + 1]
                
        return ret
        
    def canRotate(self, gameBoard): #checks if the next rotated piece
        x = gameBoard.x             #can be drawn onto the board
        y = gameBoard.y
        gb = gameBoard.board
        ret = True
        if self.rotation == 0:
            if x == gameBoard.ROWS - 2:
                ret = False
            else:
                ret = not gb[x + 2][y + 1]
                
        elif self.rotation == 1:
            if y == -1:
                ret = False
            else:
                ret = not gb[x + 1][y]
                
        elif self.rotation == 2:
            ret = not gb[x][y + 1]
            
        else:
            if y != gameBoard.COLS - 2:
                ret = not gb[x + 1][y + 2]
            else:
                ret = False
                
        return ret
    
