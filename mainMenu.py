from tkinter import *


def Exit():
    exit(0)


class StartScreen(object):

    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500+500+200")
        self.root.protocol("WM_DELETE_WINDOW", Exit)
        self.runGame = False
        image = PhotoImage(file="MainScreen.gif")
        label = Label(image=image)
        label.image = image
        label.pack()
        label.place(x=0, y=0)
        button = Button(self.root,
                        text='Play Game',
                        width=25,
                        height=5,
                        bg="blue",
                        fg="white",
                        command=self.startGame)

        button.place(x=170, y=250)
        quitBtn = Button(self.root, text='Quit', command=Exit)
        quitBtn.place(x=240, y=340)

    def start(self):
        self.root.mainloop()

    def startGame(self):
        self.root.destroy()
        self.runGame = True


class EndScreen(object):
    def __init__(self, string):
        self.root = Tk()
        self.root.geometry("200x200+500+200")
        self.root.protocol("WM_DELETE_WINDOW", Exit)
        self.root.config(bg="green")
        label = Label(self.root, text=string, width=200,height=10, bg="red")
        label.pack()
        button = Button(self.root,
                        text='Exit',
                        width=50,
                        height=10,
                        bg="blue",
                        fg="white",
                        command=Exit)
        button.pack()

    def start(self):
        self.root.mainloop()
