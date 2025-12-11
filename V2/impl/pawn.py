class pawn:
    def __init__(self, x, y, state = 0, iconName= "icon"):
        self.__x = x
        self.__y = y
        self.__state = state
        self.__iconName = iconName

    def getColor(self):
        if self.getState() == "0":
            return "black"
        if self.getState() == "3":
            return "green"
        else: return "../assets/pawns/" + self.__iconName + ".png"

    def getIconName(self):
        return self.__iconName
    def setIconName(self, iconName):
        self.__iconName = iconName
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
