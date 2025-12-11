class pawn:
    def __init__(self, x, y, state = 0):
        self.__x = x
        self.__y = y
        self.__state = state

    def getColor(self):
        if self.getState() == "0":
            return "black"
        elif self.getState() == "1":
            return "blue"
        elif self.getState() == "2":
            return "red"
        else:
            return "green"
    def getState(self):
        return self.__state
    def setState(self, state):
        self.__state = state
    def getX(self):
        return self.__x
    def setX(self, x):
        self.__x = x
    def getY(self):
        return self.__y
    def setY(self, y):
        self.__y = y
