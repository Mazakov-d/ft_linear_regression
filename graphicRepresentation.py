import plotext as plt

class graphicRepresentation:
	def __init__(self, labels, values, line):
		self.__labels = labels
		self.__values = values
		self.__line = line

	def printGraph(self):
		print("\n\n")
		plt.scatter(self.__labels, self.__values)
		plt.plot(self.__labels, self.__line)
		plt.title("Linear Regression")
		plt.show()
		print("\n\n")