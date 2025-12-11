from math import floor
import os
import random
from datetime import datetime
from V2.impl.template import *
from V2.impl.player import *
from V2.impl.pawn import *

"""game of the amazons - moteur logique"""


class GameCore:
    def __init__(self, display, template, playerList, mode):
        self.__template = template
        self.__display = display
        self.__mode = mode
        self.__board = [[pawn(colunm, row) for colunm in range(template.getSizeTemplate())] for row in range(template.getSizeTemplate())]
        self.__playerList = playerList
        self.__selectedPawn = None

        self.__action = "move" #move ou shoot
        self.__round = 1

        self.loadTemplate()

        self.__currentPlayer = playerList[0]

    def getCurrentPlayer(self):
        return self.__currentPlayer

    def switchPlayer(self):
        #Utlisation du modulo pour switch les joueurs:
        #Si on veut switch de joueur 1 à 2: currentIndex = 0, alors (0+1)%2 = 1, on va donc au joueur d'index 1, qui est le joueur 2
        #Si on veut switch de joueur 2 à 1: currentIndex = 1, alors (1+1)%2 = 0, on va donc au joueur d'index 0, qui est le joueur 1

        currentIndex = self.__playerList.index(self.getCurrentPlayer())
        self.__currentPlayer = self.__playerList[(currentIndex + 1) % 2]

    def getBoard(self):
        return self.__board

    def getFormattedAction(self):
        if self.getAction() == "move":
            if self.__selectedPawn is None:
                return "sélection"
            else:
                return "déplacement"
        else: return "tir"

    def getAction(self):
        return self.__action

    def getSelectedPawn(self):
        return self.__selectedPawn

    def getFormattedCurrentPlayerPosition(self):
        return str(self.__playerList.index(self.getCurrentPlayer()) + 1)

    def saveGame(self):
        """ Sauvegarde sous la forme ./saves/AAAA-MM-JJ_HH-MM-SS.txt """

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #permet le formatage de la date
        filename = os.path.join("../saves/" + timestamp + ".txt")

        file = open(filename, "w")

        size = self.__template.getSizeTemplate()

        for i in range(size):
            line = ""
            for j in range(size):
                state = self.__board[i][j].getState()
                line += str(state)

            file.write(line + ("\n" if i < size - 1 else "")) #on s'arrête à -1 car si retour à la ligne, mauvais format pour le chargement de template

        file.close()

        log("Partie sauvegardée : " + filename)

    def loadTemplate(self):
        """ charge une template"""

        template = self.__template.getFormatedTemplate()
        for i in range(self.__template.getSizeTemplate()):
            for j in range(self.__template.getSizeTemplate()):
                self.__board[i][j].setState(template[i][j])
                if self.__board[i][j].getState() == "1" or self.__board[i][j].getState() == "2":
                    player = self.__playerList[int(self.__board[i][j].getState()) - 1]
                    self.__board[i][j].setIconName(player.getIcon())

    def isInBounds(self, x, y):
        """Vérifie si les coordonnées sont dans les limites du plateau"""
        size = self.__template.getSizeTemplate()
        return 0 <= x < size and 0 <= y < size

    def isReachable(self, x0, y0, x1, y1):
        """check si on trouve un chemin (qui suit les règles du jeu) entre des coords (x0, y0) et des coords (x1, y1)"""
        log("X:" + str(x0) + " Y:" + str(y0) + " X1:" + str(x1) + " Y1:" + str(y1))

        #case non disponible ?
        if not self.isLocationAvailable(x1, y1):
            return False

        #sur place ?
        if x0 == x1 and y0 == y1:
            log("same coords")
            return False

        # calcul de la différence entre les coordonnées de départ et d'arrivée
        dx = x1 - x0 #horizontal
        dy = y1 - y0 #vertical

        # on cherche le nombre de mouvements nécessaires pour aller d'un point à un autre
        # EX: si on veut aller de (0,0) à (5,5):
        # on va avoir max(abs(5-0), abs(5-0)), ce qui revient à:
        # max(5, 5), donc ce qui donne 5 (max renvoit la plus grande valeur entre deux paramètres)
        # https://en.wikipedia.org/wiki/Chebyshev_distance
        distance = max(abs(dx), abs(dy))
        log(str(distance))

        # en divisant dx et dy par la distance, on obtient un vecteur de direction
        # en reprennant l'exemple:
        # on a donc la direction qui vaut: (5 // 5, 5//5) = (1, 1), ce qui équivaut au vecteur diagonale haut droit
        direction = (dx // distance, dy // distance)
        log(str(direction))


        # Parcourir toutes les cases entre start et end pour détecter un obstacle
        current_x = x0 + direction[0]
        current_y = y0 + direction[1]

        while (current_x, current_y) != (x1, y1):
            #case en dehors du plateau ?

            # Exemple de cas qui échoue : (4,5) → (0,0), déplacement impossible selon les règles du jeu
            # distance = max(abs(-4), abs(-5)) = 5
            # direction = (-4//5, -5//5) = (-1, -1)
            # Le parcours : (4,5) → (3,4) → (2,3) → (1,2) → (0,1) → (-1,0)
            # Échec car (-1,0) sort du plateau avant d'atteindre (0,0)
            if not self.isInBounds(current_x, current_y):
                log("Path goes out of the board")
                return False

            #obstacle sur le chemin ?
            if self.__board[current_y][current_x].getState() != "0":
                log("Obstacle at: " + str(current_x) + ", " + str(current_y))
                return False
            #mettre à jour les x et y actuels dans la direction calculée
            current_x += direction[0]
            current_y += direction[1]

        # si toutes les vérifications sont passées, alors le mouvement est possible
        log("move possible: " + str((x0, y0)) + " to " + str((x1, y1)))
        return True


    def switchAction(self):
        self.__action = "move" if self.__action == "shoot" else "shoot"

    def move(self, i, j):
        self.__board[i][j].setState(self.__selectedPawn.getState())
        self.__selectedPawn.setState("0")
        self.__board[i][j].setIconName(self.__selectedPawn.getIconName())
        self.__selectedPawn = self.__board[i][j]
        self.switchAction()
        self.__display.updateBoard()


    def shoot(self, i, j):
        if self.__board[i][j].getState() != "0":
            return
        self.__board[i][j].setState("3")
        self.__selectedPawn = None
        self.__display.updateBoard()
        self.switchAction()
        self.nextRound()


    def isLocationAvailable(self, x, y):
        """retourne si une case est libre ou non"""

        pawn = self.__board[y][x]
        if self.__mode == "basic":
            return pawn.getState() == "0"
        elif self.__mode == "killer":
            currentPlayerState = self.getFormattedCurrentPlayerPosition()
            return pawn.getState() != "3" and pawn.getState() != currentPlayerState



    def canPlayFrom(self, x, y):
        """retourne si on peut jouer depuis une position (x,y)"""

        if not self.isInBounds(x, y):
            return False

        pawn = self.__board[y][x]
        if pawn.getState() == "0" or pawn.getState() == "3":
            return False

        size = self.__template.getSizeTemplate()
        for i in range(size):
            for j in range(size):
                if self.isReachable(x, y, j, i):
                    return True
        return False

    def canPlay(self):
        """check si le joueur actuel peut jouer"""
        size = self.__template.getSizeTemplate()
        for i in range(size):
            for j in range(size):
                pawn = self.__board[i][j]
                if pawn.getState() == self.getFormattedCurrentPlayerPosition():
                    if self.canPlayFrom(j, i):
                        return True
        return False

    def select(self, event):
        """est appelée quand un joueur cliques sur le plateau"""

        j = floor(event.x / self.__display.getCaseSize())
        i = floor(event.y / self.__display.getCaseSize())
        pawn = self.__board[i][j]
        if self.__selectedPawn is None:
            if not pawn.getState() == self.getFormattedCurrentPlayerPosition():
                return
            self.__selectedPawn = pawn
        else:
            if self.__selectedPawn.getState() == pawn.getState() and self.__action == "move":
                self.__selectedPawn = pawn
                self.__display.updateBoard()
                return
            if not self.isReachable(self.__selectedPawn.getX(), self.__selectedPawn.getY(), j, i):
                return
            if self.__action == "move":
                self.move(i, j)
            else:
                self.shoot(i, j)
        self.__display.updateBoard()

    def nextRound(self):
        """bascule entre les manches"""
        self.__round += 1
        self.switchPlayer()
        if not self.canPlay():
            self.switchPlayer()
            self.__display.endGame()
        if self.__currentPlayer.getType() == "Bot":
            self.botRound()

    def botRound(self):
        """gère le round du bot"""

        possibleMoves = []
        for i in range(self.__template.getSizeTemplate()):
            for j in range(self.__template.getSizeTemplate()):
                if not self.__board[i][j].getState() == self.getFormattedCurrentPlayerPosition():
                    continue
                if not self.canPlayFrom(j, i):
                    continue
                possibleMoves.append((j, i))

        random.shuffle(possibleMoves)
        pawn = possibleMoves[0]
        self.__selectedPawn = self.__board[pawn[1]][pawn[0]]
        self.__display.updateBoard()

        possibleMoves.clear()
        for i in range(self.__template.getSizeTemplate()):
            for j in range(self.__template.getSizeTemplate()):
                if self.isReachable(pawn[0], pawn[1], j, i):
                    possibleMoves.append((j, i))

        random.shuffle(possibleMoves)
        target = possibleMoves[0]
        self.move(target[1], target[0])

        possibleMoves.clear()
        for i in range(self.__template.getSizeTemplate()):
            for j in range(self.__template.getSizeTemplate()):
                if self.isReachable(self.__selectedPawn.getX(), self.__selectedPawn.getY(), j, i):
                    possibleMoves.append((j, i))

        random.shuffle(possibleMoves)
        target = possibleMoves[0]
        self.shoot(target[1], target[0])
        self.__display.updateBoard()



debugMode = False
def log(string):
    if debugMode:
        print("[DEBUG]" + string)