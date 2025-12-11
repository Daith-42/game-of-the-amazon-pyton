from math import floor
from V1.impl.player import *
from V1.impl.template import *
from V1.impl.pawn import *


class GameCore:
    def __init__(self, display, template, playerList):
        self.__template = template
        self.__display = display
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

    def loadTemplate(self):
        template = self.__template.getFormatedTemplate()
        for i in range(self.__template.getSizeTemplate()):
            for j in range(self.__template.getSizeTemplate()):
                self.__board[i][j].setState(template[i][j])

    def isInBounds(self, x, y):
        """Vérifie si les coordonnées sont dans les limites du plateau"""
        size = self.__template.getSizeTemplate()
        return 0 <= x < size and 0 <= y < size

    def isReachable(self, x0, y0, x1, y1):
        log("X:" + str(x0) + " Y:" + str(y0) + " X1:" + str(x1) + " Y1:" + str(y1))

        if not self.isLocationAvailable(x1, y1):
            return False

        if x0 == x1 and y0 == y1:
            log("same coords")
            return False

        dx = x1 - x0
        dy = y1 - y0

        distance = max(abs(dx), abs(dy))
        direction = (dx // distance, dy // distance)

        current_x = x0 + direction[0]
        current_y = y0 + direction[1]

        while (current_x, current_y) != (x1, y1):
            if not self.isInBounds(current_x, current_y):
                log("Path goes out of the board")
                return False
            if not self.isLocationAvailable(current_x, current_y):
                log("Obstacle at: " + str(current_x) + ", " + str(current_y))
                return False
            current_x += direction[0]
            current_y += direction[1]

        log("move possible: " + str((x0, y0)) + " to " + str((x1, y1)))
        return True


    def switchAction(self):
        self.__action = "move" if self.__action == "shoot" else "shoot"

    def move(self, i, j):
        self.__board[i][j].setState(self.__selectedPawn.getState())
        self.__selectedPawn.setState("0")
        self.__selectedPawn = self.__board[i][j]
        self.switchAction()


    def shoot(self, i, j):
        self.__board[i][j].setState("3")
        self.__selectedPawn = None
        self.switchAction()
        self.nextRound()


    def isLocationAvailable(self, x, y):
        pawn = self.__board[y][x]
        return pawn.getState() == "0"


    def canPlayFrom(self, x, y):
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
        size = self.__template.getSizeTemplate()
        for i in range(size):
            for j in range(size):
                pawn = self.__board[i][j]
                if pawn.getState() == str(self.__playerList.index(self.getCurrentPlayer()) + 1):
                    if self.canPlayFrom(j, i):
                        return True
        return False

    def select(self, event):
        j = floor(event.x / 50)
        i = floor(event.y / 50)
        pawn = self.__board[i][j]
        if self.__selectedPawn is None:
            if not pawn.getState() == str(self.__playerList.index(self.getCurrentPlayer()) + 1):
                return
            self.__selectedPawn = pawn
        else:
            if self.__selectedPawn.getState() == pawn.getState() and self.__action == "move":
                self.__selectedPawn = pawn
                self.__display.displayBoard()
                return
            if not self.isReachable(self.__selectedPawn.getX(), self.__selectedPawn.getY(), j, i):
                return
            if self.__action == "move":
                self.move(i, j)
            else:
                self.shoot(i, j)
        self.__display.displayBoard()

    def nextRound(self):
        self.__round += 1
        self.switchPlayer()
        if not self.canPlay():
            self.__display.endGame()




debugMode = False
def log(string):
    if debugMode:
        print("[DEBUG]" + string)