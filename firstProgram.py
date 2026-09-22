import sys
from fileParser import fileParser


def main() -> int:
    fp0 = fileParser("θ0.txt",".txt", True)
    fp1 = fileParser("θ1.txt",".txt", True)
    mileage = -1
    while 1:
        teta0 = fp0.readTetaFile()
        teta1 = fp1.readTetaFile()
        while mileage < 0:
            userInput = input("\nYou want to know the price of which mileage: ")
            try:
                mileage = float(userInput)
                if mileage < 0:
                    raise ValueError
            except ValueError:
                print("Mileage should be a positive number.")
        estimatedPrice = teta0 + (teta1 * mileage)
        print(f"\n\nEstimated price of {userInput} is {estimatedPrice}.\n\n")
        while 1:
            userInput = input("Do you want to estimate an other mileage [y: yes, n: no]: ")
            if userInput == "y":
                mileage = -1
                print("We will update the θ's Values.")
                break
            elif userInput == "n":
                exit(0)
            else:
                print("Please write 'y' for yes and 'n' for no.")

if __name__ == "__main__":
    sys.exit(main())