class template:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__file = open("../templates/" + fileName, "r")
        self.__fileContent = self.__file.read()

    def getContent(self):
        return self.__fileContent

    def getFormatedTemplate(self):
        return [line.strip() for line in self.getContent().split("\n")]

    def getSizeTemplate(self):
        return len(self.getFormatedTemplate())