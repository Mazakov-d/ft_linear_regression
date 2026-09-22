import sys

class fileManager:

    def checkExtension(self, extensions):
        if not isinstance(self.__filename, str):
            print("Filename should be a string.", file=sys.stderr)
            exit(1)
        if not isinstance(extensions, list) and all(isinstance(e, str) for e in extensions):
            exit(1)
        i_dot = self.__filename.find(".")
        file_extension = self.__filename[i_dot::]
        if file_extension not in extensions:
            print(f"This extension '{file_extension}' is not allowed.")
            exit(1)

    def __init__(self, filename: str, expectedExtension: str, ifNotExistCreateIt: bool):
        self.__filename = filename
        self.checkExtension(expectedExtension)

        print(f"Trying to open '{self.__filename}'.")
        try:
            self.__file = open(self.__filename, "r+")
        except IOError:
            if (not ifNotExistCreateIt) :
                print(f"Can't open the file '{self.__filename}'.", file=sys.stderr)
                exit(1)
            try :
                self.__file = open(filename, "a+")
            except IOError:
                print(f"Can't create the file '{filename}'.", file=sys.stderr)
                exit(1)
        print(f"The file '{self.__filename}' is well opened.")

    def __del__(self):
        if self.__file:
            self.__file.close()

    def writeTetaOnFile(self, teta: str):
        self.__file.seek(0)
        self.__file.write(teta)
        self.__file.truncate()

    def readTetaFile(self) -> float:
        self.__file.seek(0)
        tetaStr = self.__file.readline()
        if not tetaStr:
            return 0
        try:
            return float(tetaStr)
        except ValueError:
            print(f"θ is '{tetaStr}', something went wrong with the conversion.", file=sys.stderr)
            exit(1)

    def readDataFile(self):
        firstLine = self.__file.readline()
        tokens = firstLine[:-1].split(',')
        if len(tokens) != 2:
            print("First line is wrong.", file=sys.stderr)
            exit(1)
        if tokens[0] == "price":
            i_price = 0
            i_milage = 1
        elif tokens[1] == "price":
            i_price = 1
            i_milage = 0
        else :
            print("First line is wrong: should contain price and mileage.", file=sys.stderr)
            exit(1)

        self.__prices = {}
        for line in self.__file:
            tokens = line[:-1].split(",")
            try:
                self.__prices[float(tokens[i_milage])] = float(tokens[i_price])
            except ValueError:
                print("The data parsed should be numbers.", file=sys.stderr)
                exit(1)

    def getPrices(self) -> {int}:
        return self.__prices