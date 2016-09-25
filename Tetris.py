import pygame, sys
from Board import *
from random import *

SPEED = 25 #Controls how fast the pieces come down
            #making this number bigger slows down the speed

class Tetris:
    def __init__(self):
        pygame.init()       #initiate pygame

        pygame.mixer.music.load('tetrisb.mid')
        
        pygame.mixer.music.play(-1, 0.0)
       #pygame.mixer.music.play(loop, start = 0.0)
        
        tetrisBoard = Board()

        screen = pygame.display.set_mode((30*tetrisBoard.COLS,\
                                          30*tetrisBoard.ROWS))
                                            #sets dimensions
                                            #sets display
                #pygame.display.set_mode((width * height))
        
        ctr = 0 #also used to control speed

        while True:
            for event in pygame.event.get(): #handles all events
                if event.type == pygame.QUIT: #handles QUIT event
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN: #handles all key events
                    if event.key == pygame.K_LEFT:
                        tetrisBoard.left()
                    if event.key == pygame.K_RIGHT:
                        tetrisBoard.right()
                    if event.key == pygame.K_UP:
                        tetrisBoard.up()
                    if event.key == pygame.K_DOWN:
                        tetrisBoard.down()
                    if event.key == pygame.K_SPACE:
                        tetrisBoard.hardDrop()
                    if event.key == pygame.K_LSHIFT:
                        tetrisBoard.hold()

            if ctr % SPEED == 0:    #This is where the speed is controlled
                tetrisBoard.down()                
                        
            screen.fill((255,255,255)) #makes the background white

            for x, row in enumerate(tetrisBoard.board): #This all gets the
                for y, col in enumerate(row):           #dimensions of
                    if col:                             #each block filled
                        pygame.draw.rect(screen, tetrisBoard.color, \
                                         (y * 30, x * 30, 30, 30))
                        #pygame.draw.rect(surface, color (y, x, width, height))
                    
            pygame.display.flip() #updates surface
            ctr += 1
