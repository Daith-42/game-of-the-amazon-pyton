"""game of the amazons - moteur graphique"""
import os.path

from V1.algorithms import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog


def chooseTemplate():
    path = filedialog.askopenfilename(
        title="Sélectionnez une configuration de plateau",
        filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")],
        initialdir="../templates")
    if not path:
        return
    return template(os.path.basename(path))

class display:
    def __init__(self, template = None):
        if template is None:
            self.__template = chooseTemplate()
        else:
            self.__template = template
        self.__playerList = [player("Joueur 1", "Human"), player("Joueur 2", "Human")]
        self.__gameCore = GameCore(self, self.__template, self.__playerList)

        self.__caseSize = 50
        self.__root = Tk()
        self.__root.title("Game of Amazons")
        self.__root.config(bg="black")
        self.__root.geometry('+100+100')

        icon = Image.open("../assets/icon.png")
        icon = ImageTk.PhotoImage(icon)
        self.__root.iconphoto(False, icon)

        self.__canvas = Canvas(self.__root)
        self.__canvas.config(width=self.__caseSize*self.__template.getSizeTemplate() + 1, height=self.__caseSize*self.__template.getSizeTemplate() + 1, highlightthickness=0, bd=0, bg="black")
        self.__canvas.pack(padx=50, pady=50)

        self.__playerText = StringVar()
        self.__text1 = Label(self.__root, textvariable=self.__playerText, bg="black", fg="white")

        self.__actionText = StringVar()
        self.__text2 = Label(self.__root, textvariable=self.__actionText, bg="black", fg="white")

        self.__text1.pack(pady=(0, 0))
        self.__text2.pack(pady=(0, 20))


        self.__templateBtn = Button(self.__root, text="Choisir une autre configuration (réinisialise la partie)", bg="black", fg="white", command=self.newGame)
        self.__templateBtn.pack(pady=(0, 20))

        self.displayBoard()

        self.__root.mainloop()

    def getGameCore(self):
        return self.__gameCore

    def getRoot(self):
        return self.__root

    def updateLabels(self):
        self.__playerText.set("Au tour de " + self.__gameCore.getCurrentPlayer().getName())
        self.__actionText.set("Action: " + self.__gameCore.getFormattedAction())


    def newGame(self):
        template = chooseTemplate()
        self.__root.destroy()
        display(template)


    def displayBoard(self):
        self.__canvas.delete("all")
        for i in range(self.__template.getSizeTemplate() + 1):
            for j in range(self.__template.getSizeTemplate() + 1):
                self.__canvas.create_line(i * self.__caseSize, 0, i * self.__caseSize, (j + 1) * self.__caseSize, fill="white")
                self.__canvas.create_line(0, j * self.__caseSize, (i + 1) * self.__caseSize, j * self.__caseSize, fill="white")
        for i in range(self.__template.getSizeTemplate()):
            for j in range(self.__template.getSizeTemplate()):
                value = self.getGameCore().getBoard()[j][i].getState()
                if value == "0" and not self.__gameCore.getSelectedPawn() is None and self.__gameCore.isReachable(self.__gameCore.getSelectedPawn().getX(), self.__gameCore.getSelectedPawn().getY(), i, j):
                    self.__canvas.create_oval(i * self.__caseSize + 20, j*self.__caseSize + 20, i * self.__caseSize + 30, j*self.__caseSize+30, fill="white")
                if value == "1" or value == "2":
                    if self.__gameCore.getSelectedPawn() is not None and self.__gameCore.getSelectedPawn() == self.getGameCore().getBoard()[j][i]:
                        self.__canvas.create_oval(i * self.__caseSize + 10, j*self.__caseSize + 10, i * self.__caseSize + 40, j*self.__caseSize+40, fill=self.getGameCore().getBoard()[j][i].getColor(), outline="white", width=2)
                    else:
                        self.__canvas.create_oval(i * self.__caseSize + 10, j*self.__caseSize + 10, i * self.__caseSize + 40, j*self.__caseSize+40, fill=self.getGameCore().getBoard()[j][i].getColor())
                elif value == "3":
                    self.__canvas.create_line(i * self.__caseSize + 10, j * self.__caseSize + 10, i * self.__caseSize + 40, j * self.__caseSize + 40, fill="green", width=3)
                    self.__canvas.create_line(i * self.__caseSize + 40, j * self.__caseSize + 10, i * self.__caseSize + 10, j * self.__caseSize + 40, fill="green", width=3)
                self.__canvas.bind('<Button-1>', self.getGameCore().select)
        self.__canvas.update()
        self.updateLabels()

    def endGame(self):
        if messagebox.askretrycancel("Game Over", self.__gameCore.getCurrentPlayer().getName() + " wins !"):
            self.__root.destroy()
            display(chooseTemplate())
        else:
            self.__root.destroy()

display(chooseTemplate())