class player:
    def __init__(self, name = "DefaultPlayer", type="Human"):
        self.__name = name
        self.__type = type

    def getName(self):
        return self.__name
    def getType(self):
        return self.__type
