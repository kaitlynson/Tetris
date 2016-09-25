from tkinter import *
from Board import *

class GameOverGui(Frame): 
    def __init__(self, score): # calls the self.score from Board
        self.score = score 
        Frame.__init__(self) 
        self.master.title("Game Over:")
                              
        self.grid()
        self.__buttonPane = Frame(self)
        self.__dataPane = Frame(self)
        
        self.__dataPane.grid(row = 10, column = 10)
                 
        self.__label1 = Label(self.__dataPane, text = "     ")
        self.__label1.grid(row = 1, column = 1)

        self.__label2 = Label(self.__dataPane, text = "Score:")
        self.__label2.grid(row = 2, column = 2)
        
        self.__label3 = Label(self.__dataPane, text = str(self.score))
        self.__label3.grid(row = 2, column = 8)

        messagebox.showinfo("Game score:", str(self.score))

