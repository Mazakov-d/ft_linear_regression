import sys
from fileParser import fileParser
from linearRegression import linearRegression

def main() -> int:
	fp = fileParser()
	fp.readFile()
	lr = linearRegression(fp.getPrices())
	lr.printGraph()
	return 0

if __name__ == "__main__":
	sys.exit(main())