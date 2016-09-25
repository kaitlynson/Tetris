from TShape import *
from OShape import *
from SShape import *
from LShape import *
from JShape import *
from ZShape import *
from IShape import *
import random, pygame, sys
from GameOverGui import *

class Board:
    COLS = 10   #how many columns
    ROWS = 22   #how many rows
    def __init__(self):     #r                      g
        self.color = (random.randint(0, 255), random.randint(0, 255), \
                  random.randint(0, 255))
                            #b
        self.board = []   #tetris board
        for row in range(Board.ROWS):
            row = []
            for col in range(Board.COLS):
                row.append(0)       #adding ten 0's to each row
            self.board.append(row)

        self.currentShape = JShape() #starting Shape
        self.heldShape = None
        self.x = 0                   #starting postition of
        self.y = 3                   #generated shapes
        self.score = 0
        
        self.draw()                  

    def check(self): #used to check if new shape can spawn
                     #this is called when a shape can't move down anymore
        for row in range(len(self.currentShape.shape)):
            for col in range(len(self.currentShape.shape[row])):
                if self.board[row][col] == True:
                    pygame.quit()
                    GameOverGui(self.score)
                    sys.exit()
                    
    def draw(self): #this draws everything onto the board
        for row in range(len(self.currentShape.shape)):
            for col in range(len(self.currentShape.shape[row])):
                if self.currentShape.shape[row][col]:
                    self.board[self.x + row][self.y + col] = \
                                      self.currentShape.shape[row][col]

    def left(self): #checks if piece can move to the left. calls methods
        if not self.currentShape.collideLeft(self):
            self.currentShape.delete(self)    
            self.y -= 1
            self.draw()

    def right(self): #checks if piece can move to the right. calls methods
        if not self.currentShape.collideRight(self):
            self.currentShape.delete(self)
            self.y += 1
            self.draw() 

    def down(self): #checks if piece can move to the down. calls methods
        if not self.currentShape.collideDown(self):
            self.currentShape.delete(self)
            self.x += 1
            self.draw()
            
        else:               #if piece can't move down, checks for line clear
            self.lineClear()#and new shape.
            self.x = 0
            self.y = 2
            self.randomShape()
            self.color = (random.randint(0,255), \
                          random.randint(0, 255), random.randint(0, 255))
            self.check()    #generates a new color
            self.draw()
            # shape is drawn on board
            
    def up(self): #checks if a shape can be rotated
        if self.currentShape.canRotate(self):
            self.currentShape.delete(self)
            self.currentShape.rotate()
            self.draw()
            
    def lineClear(self): #clears lines if full of 1's
        for i, row in enumerate(self.board):            
            #i holds index #row hold element
            if all(row):            #checks if line is full of 1's
                self.board.pop(i)   #pops out element
                self.score += 10 
                newRow = [] #list for inputing a new row into game
                for j in range(Board.COLS):
                    newRow.append(0) #makes new row full of 0's

                self.board.insert(0, newRow) #inserts new row onto top of board
                
    def randomShape(self): #generates random shape
        randNum = random.randint(0, 6) 
        if randNum == 0:
            self.currentShape = TShape()
            
        elif randNum == 1:
            self.currentShape = LShape()

        elif randNum == 2:
            self.currentShape = IShape()

        elif randNum == 3:
            self.currentShape = OShape()

        elif randNum == 4:
            self.currentShape = JShape()

        elif randNum == 5:
            self.currentShape = SShape()

        else:
            self.currentShape = ZShape()

    def hardDrop(self): #makes shape move down almost instantly
        while not self.currentShape.collideDown(self):
            self.down() #calls down() method many times until it collides
        self.down() #calls one final time so that new shape can instantly
                    #generate

    def hold(self): #holds the shape so that it can be switched when needed to
        if not self.heldShape: # sets currentShape to heldShape
            self.heldShape = self.currentShape
            self.currentShape.delete(self)
            self.randomShape()
            self.x = 0
            self.y = 2
            self.draw()
        else: #swaps heldSwap to currentShape
            tempShape = self.currentShape
            self.currentShape.delete(self)
            self.currentShape = self.heldShape
            self.x = 0
            self.y = 2
            self.draw()
            self.heldShape = tempShape
