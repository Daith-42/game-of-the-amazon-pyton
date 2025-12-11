"""game of the amazons - moteur graphique - version 2"""
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from V2.impl.theme import *
from V2.algorithms import *


class Display:
    def __init__(self, playerList, arrowIcon, templateName, theme, mode="basic", caseSize = 50):
        self.__template = template(templateName)
        self.__gameCore = GameCore(self, self.__template, playerList, mode)
        self.__arrowIcon = arrowIcon

        self.__templateName = templateName
        self.__playerList = playerList
        self.__mode = mode
        self.__theme = theme

        self.__caseSize = caseSize
        self.__root = tk.Toplevel()
        self.__root.title("Game of Amazons")
        self.__root.config(bg=self.__theme.getBackground())
        self.__root.geometry('+100+100')

        self.__images = []

        icon = Image.open("../assets/icon.png")
        icon = ImageTk.PhotoImage(icon)
        self.__root.iconphoto(True, icon)

        self.__frame4 = tk.Frame(self.__root, bg=self.__theme.getBackground())
        self.__frame4.grid(row = 0, column = 0, columnspan=3)
        self.__saveBtn = tk.Button(self.__frame4, text="Sauvegarder et quitter la partie", bg=self.__theme.getBackground(), fg="white", command=self.saveAndQuit)
        self.__saveBtn.pack(pady=(20, 0))

        self.__frame1 = tk.Frame(self.__root, bg=self.__theme.getBackground())
        self.__frame1.grid(row = 1, column = 0, columnspan=3)
        self.__canvas = tk.Canvas(self.__frame1)
        self.__canvas.config(width=self.__caseSize*self.__template.getSizeTemplate() + 1, height=self.__caseSize*self.__template.getSizeTemplate() + 1, highlightthickness=0, bd=0, bg=self.__theme.getBackground())
        self.__canvas.pack(padx=50, pady=50)


        self.__frame2 = tk.Frame(self.__root, bg=self.__theme.getBackground())
        self.__frame2.grid(row=2, column=1)
        self.__playerText = tk.StringVar()
        self.__text1 = tk.Label(self.__frame2, textvariable=self.__playerText, bg=self.__theme.getBackground(), fg="white")
        self.__actionText = tk.StringVar()
        self.__text2 = tk.Label(self.__frame2, textvariable=self.__actionText, bg=self.__theme.getBackground(), fg="white")

        self.__text1.pack(pady=(0, 0))
        self.__text2.pack(pady=(0, 20))


        #Affichages des joueurs
        self.__frame3 = tk.Frame(self.__root, bg=self.__theme.getBackground())
        self.__frame3.grid(row=2, column=0)

        self.__player1Icon = (Image.open("../assets/pawns/" + playerList[0].getIcon() + ".png")
                              .resize((self.__caseSize, self.__caseSize),Image.Resampling.LANCZOS))
        self.__player1Photo = ImageTk.PhotoImage(self.__player1Icon)
        self.__image1 = tk.Label(self.__frame3, image=self.__player1Photo, borderwidth=0)
        self.__image1.image = self.__player1Photo

        self.__text3 = tk.Label(self.__frame3, text=playerList[0].getName(), bg=self.__theme.getBackground(), fg="white")

        self.__text3.pack(pady=(0, 5))
        self.__image1.pack(pady=(0, 20))


        self.__frame4 = tk.Frame(self.__root, bg=self.__theme.getBackground())
        self.__frame4.grid(row=2, column=2)

        self.__player2Icon = (Image.open("../assets/pawns/" + playerList[1].getIcon() + ".png")
                              .resize((self.__caseSize, self.__caseSize),Image.Resampling.LANCZOS))
        self.__player2Photo = ImageTk.PhotoImage(self.__player2Icon)
        self.__image2 = tk.Label(self.__frame4, image=self.__player2Photo, borderwidth=0)
        self.__image2.image = self.__player2Photo

        self.__text4 = tk.Label(self.__frame4, text=playerList[1].getName(), bg=self.__theme.getBackground(), fg="white")

        self.__text4.pack(pady=(0, 5))
        self.__image2.pack(pady=(0, 20))



        self.updateBoard()

        if self.__gameCore.getCurrentPlayer().getType() == "Bot":
            self.__gameCore.botRound()

        self.__root.mainloop()

    def getGameCore(self):
        return self.__gameCore

    def getRoot(self):
        return self.__root

    def getCaseSize(self):
        return self.__caseSize

    def updateLabels(self):
        self.__playerText.set("Au tour de " + self.__gameCore.getCurrentPlayer().getName())
        self.__actionText.set("Action: " + self.__gameCore.getFormattedAction())

    def saveAndQuit(self):
        self.__gameCore.saveGame()
        self.__root.destroy()

    def convertImage(self, access):
        """renvoit, à partir d'un chemin, une image"""
        image = Image.open(access)
        image = image.resize((self.__caseSize-10, self.__caseSize-10), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

    def updateBoard(self):
        self.updateLabels()
        if self.__gameCore.getCurrentPlayer().getType() == "Bot":
            self.botDisplay()
        else:
            self.displayBoard()

    def botDisplay(self):
        # permet de mettre de la latence et que ce soit pas instantané
        self.__root.after(1000, self.displayBoard())

    def displayBoard(self):
        self.__canvas.delete("all")
        self.__images = []
        color = self.__theme.getFirst()
        for i in range(self.__template.getSizeTemplate() + 1):
            for j in range(self.__template.getSizeTemplate() + 1):
                self.__canvas.create_rectangle(i * self.__caseSize, j * self.__caseSize, i * self.__caseSize + self.__caseSize, j * self.__caseSize + self.__caseSize, fill=color)
                color = self.__theme.getFirst() if color == self.__theme.getSecond()  else self.__theme.getSecond()
        for i in range(self.__template.getSizeTemplate()):
            for j in range(self.__template.getSizeTemplate()):
                value = self.getGameCore().getBoard()[j][i].getState()
                if value == "0" and not self.__gameCore.getSelectedPawn() is None and self.__gameCore.isReachable(self.__gameCore.getSelectedPawn().getX(), self.__gameCore.getSelectedPawn().getY(), i, j):

                    #permet de créer les ronds de prévisualisation des coups selon la taille des cases
                    padding = self.__caseSize // 4
                    diameter = self.__caseSize // 2
                    self.__canvas.create_oval(
                        i * self.__caseSize + padding,
                        j * self.__caseSize + padding,
                        i * self.__caseSize + padding + diameter,
                        j * self.__caseSize + padding + diameter,
                        fill="white",
                        width=1
                    )

                if value == "1" or value == "2":
                    img = self.convertImage(self.getGameCore().getBoard()[j][i].getColor())
                    self.__images.append(img)


                    self.__canvas.create_image(i*self.__caseSize + self.__caseSize//2, j*self.__caseSize + self.__caseSize//2, image=img)

                elif value == "3":
                    img = self.convertImage("../assets/arrows/" + self.__arrowIcon + ".png")
                    self.__images.append(img)

                    self.__canvas.create_image(i*self.__caseSize + self.__caseSize//2, j*self.__caseSize + self.__caseSize//2, image=img)

                self.__canvas.bind('<Button-1>', self.getGameCore().select)
        self.__canvas.update()

    def endGame(self):
        if messagebox.askretrycancel("Game Over", self.getGameCore().getCurrentPlayer().getName() + " wins !"):
            Display(self.__playerList, self.__arrowIcon, self.__templateName, self.__theme, self.__mode, self.__caseSize)
            self.__root.destroy()
        else:
            self.__root.destroy()