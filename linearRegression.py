from graphicRepresentation import graphicRepresentation

class linearRegression:
	def __init__(self, prices: {int}):
		ySum = 0
		xSum = 0
		xySum = 0
		xSquareSum = 0

		for x, y in prices.items():
			xSum += x
			xSquareSum += (x * x)
			ySum += y
			xySum += (x * y)

		n = len(prices)

		self.__slope = ((n * xySum) - (xSum * ySum)) / ((n * xSquareSum) - (xSum * xSum))

		self.__pointZero = (ySum - (self.__slope * xSum)) / n

		self.__labels = list(prices.keys())
		self.__values = list(prices.values())
		self.__line = [self.__slope * xi + self.__pointZero for xi in self.__labels]

	def printGraph(self):
		gr = graphicRepresentation(self.__labels, self.__values, self.__line)
		gr.printGraph()
