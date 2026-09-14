import sys

class fileParser:

	def checkExtension(self, extensions):
		if not isinstance(self.__filename, str):
			print("Filename should be a string.", file=sys.stderr)
			exit(1)
		if not isinstance(extensions, list) and all(isinstance(e, str) for e in extensions):
			exit(1)
		i_dot = self.__filename.find(".")
		file_extension = self.__filename[i_dot::]
		if not file_extension in extensions:
			print(f"This extension '{file_extension}' is not allowed.")
			exit(1)

	def __init__(self):
		self.__filename = input("Enter the filename for the data: ")
		self.checkExtension([".csv"])

		print(f"Trying to open '{self.__filename}'.")
		try:
			self.__file = open(self.__filename)
		except IOError:
			print(f"Can't open the file '{self.__filename}'.", file=sys.stderr)
			exit(1)
		print(f"The file '{self.__filename}' is well opened.")

	def readFile(self):
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