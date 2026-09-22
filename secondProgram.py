import sys
from fileParser import fileParser

learningRate = 0.1

def main():
    fp = fileParser(input("Please, can you provide the file path for the data file (should end with '.csv'): "), ".csv", False)
    

if __name__ == "__main__":
    sys.exit(main())