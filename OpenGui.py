from tkinter import *
from Tetris import *

class OpenGui(Frame):
    def __init__(self):
        #Sets up the window and widgets 
        Frame.__init__(self) # initializing the Frame class from tkinter
        self.master.title("Tetris Menu") # sets title of the window ^^
        self.grid() # initialize grid

        self.__dataPane = Frame(self) # sets frame for label 
        
        self.__dataPane.grid(row = 0, column = 0) #sets grid
        self.__buttonPane = Frame(self)# sets frame of buttons
         
        self.__label1 = Label(self.__dataPane, text = "Tetris Game!      ")                     
        self.__label1.grid()
        
        self.__label2 = Label(self.__dataPane, text = "                  ")                    
        self.__label2.grid()

        self.__label2 = Label(self.__dataPane, text = "                  ")                    
        self.__label2.grid()

        self.__label2 = Label(self.__dataPane, text = "                  ")                    
        self.__label2.grid()
        
        self.__buttonPane.grid(row = 1, column = 1)

        self.__button1 = Button(self.__buttonPane, text = " Start ", \
                                command = self.startGame)
        
        self.__button2 = Button(self.__buttonPane, text = " Quit ", \
                                command = self.master.destroy)
                                        
        self.__button1.grid()
        self.__button2.grid()

    def startGame(self):
        Tetris()
        
def main():
    #Instantiate and pop up the window
    OpenGui().mainloop()
    
main()
