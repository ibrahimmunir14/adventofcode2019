def main():
    f = open("input1.txt", "r")
    masses = f.read().split("\n")[:-1]
    masses = list(int(x) for x in masses)
    
    total = 0
    for mass in masses:
        total += calculateFuel(mass)
    print("Part 1 Total Fuel Requirement:", total)
    total = 0
    for mass in masses:
        total += calcFuelRecursive(mass)
    print("Part 2 Total Fuel Requirement:", total)

def calculateFuel(mass):
    fuel = (mass // 3) - 2
    return max(0, fuel)

def calcFuelRecursive(mass):
    if (mass == 0): return 0
    fuel = calculateFuel(mass)
    return fuel + calcFuelRecursive(fuel)

main()
