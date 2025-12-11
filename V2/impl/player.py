class player:
    def __init__(self, name="DefaultPlayer", type="Human", icon="icon"):
        self.__name = name
        self.__type = type
        self.__icon = icon

    def getIcon(self):
        return self.__icon

    def setIcon(self, icon):
        self.__icon = icon

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type