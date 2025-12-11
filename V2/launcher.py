from tkinter import *
from V2.game import *

class Launcher:
    def __init__(self):

        # définition de la page launcher
        self.__playerList = None
        self.__root = Tk()
        self.__root.title("Game of Amazons - Launcher")
        self.__root.config(bg="gray24")
        self.__root.geometry('950x700')
        self.__root.resizable(height=False, width=False)

        # icon de la page launcher
        icon = Image.open("../assets/icon.png")
        icon = ImageTk.PhotoImage(icon)
        self.__root.iconphoto(True, icon)

        # titre principal
        self.__frameTitle = Frame(self.__root)
        self.__frameTitle.grid(row=0,column=0, columnspan=2)
        self.__titleText = StringVar()
        self.__titleText.set("Game of the Amazons - Launcher")
        self.__titleHub = Label(self.__frameTitle, textvariable=self.__titleText, bg="gray24",font=("Robot", 28, "bold"),pady=10, padx=20)
        self.__titleHub.pack()

        # frame contenant la selection de mode de jeu
        self.__frameSelectionGameMode = Frame(self.__root, bg="gray24")
        self.__frameSelectionGameMode.grid(row=1, column=0, sticky="n")

        # sous-titre 1, selection mode de jeu
        self.__selectionText = StringVar()
        self.__selectionText.set("Sélectionner un mode de jeu :")
        self.__titleSelection = Label(self.__frameSelectionGameMode, textvariable=self.__selectionText, bg="gray24",font=("Robot", 20, "bold"),pady=5)
        self.__titleSelection.pack()

        # frame contenant les boutons de la selection de mode de jeu
        self.__frameSelectionButton = Frame(self.__frameSelectionGameMode, bg="gray24")
        self.__frameSelectionButton.pack()

        # définition de la variable temporaire pour la selection du mode de jeu
        self.__selectionModeValue = StringVar(value="basic")

        # fonction pour définir quelle mode de jeu a été selectionner
        def selectionMode():
            self.__selectedMode = self.__selectionModeValue.get()

        # les 3 boutons de selection
        mode1 = Radiobutton(self.__frameSelectionButton, text="Mode base",variable=self.__selectionModeValue,value="basic",command=selectionMode,
                            indicatoron=0, width=15, height=5, bg="gray30", font=("Robot", 10))
        mode2 = Radiobutton(self.__frameSelectionButton, text="Mode killer", variable=self.__selectionModeValue, value="killer",command=selectionMode,
                            indicatoron=0, width=15, height=5, bg="gray30", font=("Robot", 10))

        # placement des 3 boutons
        mode1.grid(row=0, column=0, padx= 15)
        mode2.grid(row=0, column=1, padx= 15)

        # frame contenant la selection de taille
        self.__frameSelectionGameSize = Frame(self.__frameSelectionButton, bg="gray24")
        self.__frameSelectionGameSize.grid(row=2, column=0, columnspan=3)

        # sous-titre 2, selection de la taille de plateau
        self.__sizeText = StringVar()
        self.__sizeText.set("Sélectionner une taille de plateau :")
        self.__titleSize = Label(self.__frameSelectionGameSize, textvariable=self.__sizeText, bg="gray24",font=("Robot SemiBold", 20, "bold"),pady=5)
        self.__titleSize.pack(pady=(25, 0))

        # frame contenant les boutons de la selection de la taille de plateau
        self.__frameSizeButton = Frame(self.__frameSelectionGameSize, bg="gray24")
        self.__frameSizeButton.pack()

        # définition de la variable temporaire pour la selection de la taille de plateau
        self.__selectionSizeValue = StringVar(value="4")

        # fonction pour définir quelle taille du plateau a été selectionner
        def selectionSize():
            self.__selectedSize = self.__selectionSizeValue.get()

        # les 4 boutons de selection
        buttonSize1 = Radiobutton(self.__frameSizeButton, text="4", variable=self.__selectionSizeValue, value="4",command=selectionSize,
                                  indicatoron=0, width=5, height=2, bg="gray30", font=("Robot", 10))
        buttonSize2 = Radiobutton(self.__frameSizeButton, text="6", variable=self.__selectionSizeValue, value="6",command=selectionSize,
                                  indicatoron=0, width=5, height=2, bg="gray30", font=("Robot", 10))
        buttonSize3 = Radiobutton(self.__frameSizeButton, text="8", variable=self.__selectionSizeValue, value="8",command=selectionSize,
                                  indicatoron=0, width=5, height=2, bg="gray30", font=("Robot", 10))
        buttonSize4 = Radiobutton(self.__frameSizeButton, text="10", variable=self.__selectionSizeValue, value="10",command=selectionSize,
                                  indicatoron=0, width=5, height=2, bg="gray30", font=("Robot", 10))
        buttonSize5 = Radiobutton(self.__frameSizeButton, text="12", variable=self.__selectionSizeValue, value="12",command=selectionSize,
                                  indicatoron=0, width=5, height=2, bg="gray30", font=("Robot", 10))

        # placement des 4 boutons
        buttonSize1.grid(row=0, column=0, padx=15)
        buttonSize2.grid(row=0, column=1, padx=15)
        buttonSize3.grid(row=0, column=2, padx=15)
        buttonSize4.grid(row=0, column=3, padx=15)
        buttonSize5.grid(row=0, column=4, padx=15)


        # frame contenant la selection de joueur
        self.__frameSelectionPlayer = Frame(self.__root, bg="gray24")
        self.__frameSelectionPlayer.grid(row=1, column=1)

        # sous-titre 3, selection des joueurs
        self.__playerSelectionText = StringVar()
        self.__playerSelectionText.set("Sélectionner 2 joueur :")
        self.__titleSelectionPlayer = Label(self.__frameSelectionPlayer, textvariable=self.__playerSelectionText, bg="gray24",font=("Robot SemiBold", 20, "bold"),pady=5)
        self.__titleSelectionPlayer.grid(row=0, column=0, columnspan=2)

        # sous-titre, selection joueur 1
        self.__playerOneSelectionText = StringVar()
        self.__playerOneSelectionText.set("Joueur 1")
        self.__titleSelectionPlayerOne = Label(self.__frameSelectionPlayer, textvariable=self.__playerOneSelectionText, bg="gray24",font=("Robot SemiBold", 15, "bold"))
        self.__titleSelectionPlayerOne.grid(row=1, column=0, padx=80)

        # sous-titre, selection joueur 2
        self.__playerTwoSelectionText = StringVar()
        self.__playerTwoSelectionText.set("Joueur 2")
        self.__titleSelectionPlayerTwo = Label(self.__frameSelectionPlayer, textvariable=self.__playerTwoSelectionText, bg="gray24",font=("Robot SemiBold", 15, "bold"))
        self.__titleSelectionPlayerTwo.grid(row=1, column=1, padx=80)

        # variable contenant le nom des joueurs
        self.selectionPlayer1 = StringVar(value="Joueur 1")
        self.selectionPlayer2 = StringVar(value="Joueur 2")

        # zone de saisi du nom du joueur 1
        self.entryPlayerOne = Entry(self.__frameSelectionPlayer,
                                    textvariable=self.selectionPlayer1,
                                    font=("Robot", 10),
                                    width=20,
                                    bg="gray30",
                                    fg="white")
        self.entryPlayerOne.grid(column=0, row=2, pady=0)

        # zone de saisi du nom du joueur 1
        self.entryPlayerTwo = Entry(self.__frameSelectionPlayer,
                                    textvariable=self.selectionPlayer2,
                                    font=("Robot", 10),
                                    width=20,
                                    bg="gray30",
                                    fg="white")
        self.entryPlayerTwo.grid(column=1, row=2, pady=5)

        # variable de selection bot joueur 1
        self.__player1Bot = BooleanVar()
        self.__player1Bot.set(False)

        # zone de selection bot joueur 1
        self.__checkBoxPlayer1Bot = Checkbutton(self.__frameSelectionPlayer, text="Robot", variable=self.__player1Bot)
        self.__checkBoxPlayer1Bot = Checkbutton(
            self.__frameSelectionPlayer,
            text="Robot",
            variable=self.__player1Bot,
            bg="gray24",
            fg="white",
            font=("Robot", 10),
            selectcolor="gray30",
            activebackground="gray24",
            activeforeground="white",
            highlightthickness=0
        )

        # variable de selection bot joueur 2
        self.__player2Bot = BooleanVar()
        self.__player2Bot.set(False)

        # zone de selection bot joueur 2
        self.__checkBoxPlayer2Bot = Checkbutton(self.__frameSelectionPlayer, text="Robot", variable=self.__player2Bot)
        self.__checkBoxPlayer2Bot = Checkbutton(
            self.__frameSelectionPlayer,
            text="Robot",
            variable=self.__player2Bot,
            bg="gray24",
            fg="white",
            font=("Robot", 10),
            selectcolor="gray30",
            activebackground="gray24",
            activeforeground="white",
            highlightthickness=0
        )

        # placement de la zone de selection du bot 1 et du bot 2
        self.__checkBoxPlayer1Bot.grid(column=0, row=4)
        self.__checkBoxPlayer2Bot.grid(column=1, row=4)

        # liste des icônes des pions
        options_list = []
        for file in os.listdir("../assets/pawns"):
            options_list.append(file.title()[:-4])

        # variable contenant le pion du joueur 1
        self.__value_Inside_Player1 = StringVar()
        self.__value_Inside_Player1.set("Villager")

        # menu déroulant pour le choix du pion du joueur 1
        self.__icon_menu_player1 = OptionMenu(
            self.__frameSelectionPlayer,
            self.__value_Inside_Player1,
            *options_list
        )
        self.__icon_menu_player1.config(
            bg="gray30",
            fg="white",
            activebackground="green",
            activeforeground="white",
            font=("Robot", 11),
            highlightthickness=0,
            relief=FLAT
        )
        # placement du menu déroulant du joueur 1
        self.__icon_menu_player1.grid(row=3, column=0)

        # variable contenant le pion du joueur 2
        self.__value_Inside_Player2 = StringVar()
        self.__value_Inside_Player2.set("Zombie")

        # menu déroulant pour le choix du pion du joueur 2
        self.__icon_menu_player2 = OptionMenu(self.__frameSelectionPlayer,
                                              self.__value_Inside_Player2,
                                              *options_list
                                              )
        self.__icon_menu_player2.config(
            bg="gray30",
            fg="white",
            activebackground="green",
            activeforeground="white",
            font=("Robot", 11),
            highlightthickness=0,
            relief=FLAT
        )

        # placement du menu déroulant du joueur 1
        self.__icon_menu_player2.grid(row=3, column=1)

        # bouton pour valider le choix des pions et des noms
        self.btnValidate = Button(self.__frameSelectionPlayer,
                                  text="Valider les joueurs",
                                  command=self.selectionPlayer,
                                  bg="gray40", fg="white", font=("Robot", 10))
        self.btnValidate.grid(row=4, columnspan=2, pady=10)

        # création de la liste contenant les different type de fleches
        arrow_List = []
        for file in os.listdir("../assets/arrows"):
            arrow_List.append(file.title()[:-4])

        # variable du choix du type de fleche
        self.__value_Inside_Arrow= StringVar()
        self.__value_Inside_Arrow.set("Minecraft")

        # bouton déroulant pour le choix des fleches
        self.__icon_menu_arrow = OptionMenu(self.__frameSelectionPlayer, self.__value_Inside_Arrow, *arrow_List)
        self.__icon_menu_arrow.config(
            bg="gray30",
            fg="white",
            activebackground="green",
            activeforeground="white",
            font=("Robot", 11),
            highlightthickness=0,
            relief=FLAT
        )
        self.__icon_menu_arrow.grid(row=5, columnspan=2, pady=(0, 10))

        # frame contenant la selection des joueurs
        self.__frameDisplayPlayers = Frame(self.__frameSelectionPlayer, bg="gray24")
        self.__frameDisplayPlayers.grid(row=6, column=0, columnspan=2)

        self.__player1NameText = StringVar()
        self.__player2NameText = StringVar()

        # affichage de la prévisualisation des noms
        self.__player1NameLabel = Label(self.__frameDisplayPlayers, textvariable=self.__player1NameText, bg="gray24", fg="white")
        self.__player2NameLabel = Label(self.__frameDisplayPlayers, textvariable=self.__player2NameText, bg="gray24", fg="white")
        self.__player1NameLabel.grid(row=1, column=0, pady=10)
        self.__player2NameLabel.grid(row=1, column=2, pady=10)

        # affichage de la prévisualisation des pions et des fleches
        self.__player1Photo = PhotoImage()
        self.__player2Photo = PhotoImage()
        self.__arrowPhoto = PhotoImage()

        # création de la liste des themes
        self.__themeList = self.themeList()
        self.__themeList_Names = []
        for e in self.__themeList:
            self.__themeList_Names.append(e.getName())

        # bouton de selection du theme
        self.__selectedTheme = StringVar()
        self.__selectedTheme.set(self.__themeList[0].getName())
        self.__theme_Menu = OptionMenu(self.__root, self.__selectedTheme, *self.__themeList_Names)
        self.__theme_Menu.config(
            bg="gray30",
            fg="white",
            activebackground="green",
            activeforeground="white",
            font=("Robot", 11),
            highlightthickness=0,
        )
        self.__theme_Menu.grid(row=5, column=0, pady=0, sticky='n')

        # selection de la taille des cases
        self.__selectCaseWith = tk.Scale(self.__root, from_=20, to=100, orient=tk.HORIZONTAL, resolution=10, tickinterval=10,
                                  length=300, bg="gray45", label="Sélectionnez une taille de case")
        self.__selectCaseWith.set(50)

        self.__selectCaseWith.grid(row=7, column=0, pady=10, sticky='n')

        # bouton de démarage
        self.__startButton = Button(self.__root, text="LANCER LA PARTIE", command=self.launchParty,
                                    bg="green", fg="white", font=("Robot", 15, "bold"), width=20, height=2)
        self.__startButton.grid(row=8, column=0, columnspan=2, pady=10)

        # frame contenant les élements pour le chargement d'une save
        self.__frameLoadButton = Frame(self.__root, bg="gray24")
        self.__frameLoadButton.grid(row=9, columnspan=2, column=0)

        # bouton pour lancer une save
        self.__loadButton = Button(self.__frameLoadButton, text="CHARGER LA PARTIE", command=self.launchPartySave,
                                    bg="green", fg="white", font=("Robot", 15, "bold"), width=20, height=2)
        self.__loadButton.grid(row=0, column=0, pady=0)

        # création d'une liste contenant les saves
        savesList = []
        for file in os.listdir("../saves"):
            savesList.append(file.title()[:-4])

        self.__titleSaves = StringVar()
        if not savesList:
            savesList = ["Aucune save disponible"]
            self.__titleSaves.set("Aucune save disponible")
        else:
            self.__titleSaves.set("Sélectionner une save")

        # bouton de selection de save
        self.__menuSaves = OptionMenu(self.__frameLoadButton, self.__titleSaves, *savesList)
        self.__menuSaves.config(
            bg="gray30",
            fg="white",
            activebackground="green",
            activeforeground="white",
            font=("Robot", 11),
            highlightthickness=0,
            relief=FLAT
        )
        self.__menuSaves.grid(row=0, column=1, padx=10)

        self.selectionPlayer()

        self.__root.mainloop()

    def selectionPlayer(self):
        name1 = self.selectionPlayer1.get()
        name2 = self.selectionPlayer2.get()

        if name1 == name2:
            self.selectionPlayer1.set("Joueur 1")
            self.selectionPlayer2.set("Joueur 2")
            name1 = "Joueur 1"
            name2 = "Joueur 2"

        playerOne = name1
        playerTwo = name2


        if self.__value_Inside_Player1.get() == self.__value_Inside_Player2.get():
            self.__value_Inside_Player1.set("Villager")
            self.__value_Inside_Player2.set("Zombie")

        player1 = player(playerOne, self.getFormatedType(self.__player1Bot.get()), self.__value_Inside_Player1.get())
        player2 = player(playerTwo, self.getFormatedType(self.__player2Bot.get()), self.__value_Inside_Player2.get())

        self.__player1NameText.set(player1.getName())
        self.__player2NameText.set(player2.getName())

        self.updatePlayersDisplay()

        self.__playerList = [player1, player2]

    def updatePlayersDisplay(self):
        player1Icon = (Image.open("../assets/pawns/" + self.__value_Inside_Player1.get() + ".png")
                       .resize((50, 50), Image.Resampling.LANCZOS))
        self.__player1Photo = ImageTk.PhotoImage(player1Icon)
        image1 = Label(self.__frameDisplayPlayers, image=self.__player1Photo, borderwidth=0, bg="gray24")
        image1.grid(row=0, column=0)

        player2Icon = (Image.open("../assets/pawns/" + self.__value_Inside_Player2.get() + ".png")
                       .resize((50, 50), Image.Resampling.LANCZOS))
        self.__player2Photo = ImageTk.PhotoImage(player2Icon)
        image2 = Label(self.__frameDisplayPlayers, image=self.__player2Photo, borderwidth=0, bg="gray24")
        image2.grid(row=0, column=2)

        arrowIcon = (Image.open("../assets/arrows/" + self.__value_Inside_Arrow.get() + ".png")
                       .resize((50, 50), Image.Resampling.LANCZOS))
        self.__arrowPhoto = ImageTk.PhotoImage(arrowIcon)
        image2 = Label(self.__frameDisplayPlayers, image=self.__arrowPhoto, borderwidth=0, bg="gray24")
        image2.grid(row=0, column=1, padx=50)

    def themeList(self):
        """ contient tout les themes disponibles"""
        return [
            theme("Sélectionner un theme", "gray24", "azure", "peach puff"),
            theme("Océan", "dark slate gray", "light cyan", "steel blue"),
            theme("Forêt", "dark green", "pale green", "dark olive green"),
            theme("Coucher de soleil", "dark orange", "light salmon", "coral"),
            theme("Lavande", "medium purple", "lavender", "plum"),
            theme("Minuit", "midnight blue", "light steel blue", "slate blue"),
            theme("Automne", "saddle brown", "sandy brown", "dark goldenrod"),
            theme("Menthe", "dark sea green", "mint cream", "aquamarine"),
            theme("Rose", "deep pink", "light pink", "hot pink"),
            theme("Café", "sienna", "wheat", "burlywood"),
            theme("Ardoise", "slate gray", "light gray", "dark gray"),
            theme("Feu", "dark red", "orange red", "tomato"),
            theme("Améthyste", "dark orchid", "thistle", "medium orchid"),
            theme("Citron", "olive drab", "light yellow", "khaki"),
            theme("Turquoise", "dark turquoise", "pale turquoise", "medium turquoise"),
            theme("Terre", "chocolate", "tan", "peru"),
            theme("Glacier", "light steel blue", "alice blue", "powder blue"),
            theme("Cerise", "maroon", "rosy brown", "indian red"),
            theme("Printemps", "lime green", "light green", "yellow green"),
            theme("Nuit étoilée", "navy", "sky blue", "dodger blue")
        ]

    def getFormatedType(self, boolean):
        return "Human" if not boolean else "Bot"

    def formatBoardSize(self, string):
        match string:
            case "4":
                return "quatre"
            case "6":
                return "six"
            case "8":
                return "huit"
            case "10":
                return "dix"
            case "12":
                return "douze"

    def getThemeFromString(self, string):
        for e in self.__themeList:
            if e.getName() == string.get():
                return e
        print("Theme '" + string.get() + "' not found.")
        return self.__themeList[0]

    def launchParty(self):
        print("Launching party")
        Display(self.__playerList, self.__value_Inside_Arrow.get(), "../templates/" + self.formatBoardSize(self.__selectionSizeValue.get()) + ".txt", self.getThemeFromString(self.__selectedTheme), self.__selectionModeValue.get(), self.__selectCaseWith.get())

    def launchPartySave(self):
        if self.__titleSaves.get() == "Sélectionner une save" or self.__titleSaves.get() == "Aucune save disponible":
            return
        print("Launching party")
        print(self.__titleSaves.get()+ ".txt")
        Display(self.__playerList, self.__value_Inside_Arrow.get(), "../saves/"+ self.__titleSaves.get()+ ".txt" , self.getThemeFromString(self.__selectedTheme), self.__selectionModeValue.get(), self.__selectCaseWith.get())


Launcher()
