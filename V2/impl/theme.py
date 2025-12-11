class theme:
    def __init__(self, name, background, first, second):
        self.__name = name
        self.__background = background
        self.__first = first
        self.__second = second


    def getName(self):
        return self.__name
    def getBackground(self):
        return self.__background
    def getFirst(self):
        return self.__first
    def getSecond(self):
        return self.__second
