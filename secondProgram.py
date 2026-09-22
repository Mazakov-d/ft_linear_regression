import sys
from fileManager import fileManager
from graphicRepresentation import graphicRepresentation

learningRate = 0.01
iterations = 1000

def denormalize(teta0, teta1, mileageMin, mileageMax):
    realTeta1 = teta1 / (mileageMax - mileageMin)
    realTeta0 = teta0 - teta1 * mileageMin / (mileageMax - mileageMin)
    return realTeta0, realTeta1

def plotLine(mileages, prices, teta0, teta1):
    line = [teta1 * mileage + teta0 for mileage in mileages]
    gr = graphicRepresentation(mileages, list(prices.values()), line)
    gr.printGraph()

def main():
    fp = fileManager(input("Please, can you provide the file path for the data file (should end with '.csv'): "), [".csv"], False)
    fp0 = fileManager("θ0.txt", [".txt"], True)
    fp1 = fileManager("θ1.txt", [".txt"], True)
    fp.readDataFile()
    prices = fp.getPrices()

    mileages = list(prices.keys())
    mileageMin = min(mileages)
    mileageMax = max(mileages)
    normalizedPrices = {(mileage - mileageMin) / (mileageMax - mileageMin): price for mileage, price in prices.items()}

    teta0 = fp0.readTetaFile()
    teta1 = fp1.readTetaFile()

    plotLine(mileages, prices, teta0, teta1)

    for _ in range(iterations):
        sum0 = 0
        sum1 = 0
        for mileage, price in normalizedPrices.items():
            error = (teta0 + teta1 * mileage) - price
            sum0 += error
            sum1 += error * mileage
        teta0 -= learningRate * (1/len(normalizedPrices)) * sum0
        teta1 -= learningRate * (1/len(normalizedPrices)) * sum1

    realTeta0, realTeta1 = denormalize(teta0, teta1, mileageMin, mileageMax)
    fp0.writeTetaOnFile(str(realTeta0))
    fp1.writeTetaOnFile(str(realTeta1))

    plotLine(mileages, prices, realTeta0, realTeta1)

if __name__ == "__main__":
    sys.exit(main())