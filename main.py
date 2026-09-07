
import sys
import plotext as plt


def checkExtension(filename, extensions):
	if not isinstance(filename, str):
		print("Filename should be a string.", file=sys.stderr)
		exit(1)
	if not isinstance(extensions, list) and all(isinstance(e, str) for e in extensions):
		exit(1)
	i_dot = filename.find(".")
	file_extension = filename[i_dot::]
	if file_extension not in extensions:
		print(f"This extension '{file_extension}' is not allowed.")
		exit(1)


filename = input("Enter the filename for the data: ")
checkExtension(filename, [".csv"])

print(f"Trying to open '{filename}'.")
try:
	file = open(filename)
except IOError:
	print(f"Can't open the file '{filename}'.", file=sys.stderr)
	exit(1)

print(f"The file '{filename}' is well opened.")
firstLine = file.readline()
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

prices = {}
for line in file:
	tokens = line[:-1].split(",")
	try:
		prices[float(tokens[i_milage])] = float(tokens[i_price])
	except ValueError:
		print("The data parsed should be numbers.", file=sys.stderr)
		exit(1)

labels = list(prices.keys())
values = list(prices.values())

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

slope = ((n * xySum) - (xSum * ySum)) / ((n * xSquareSum) - (xSum * xSum))

pointZero = (ySum - (slope * xSum)) / n

plt.scatter(labels, values)

line = [slope * xi + pointZero for xi in labels]

plt.plot(labels, line)

plt.title("test")
plt.show()

