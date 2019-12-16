import intCode
import itertools

def main():
    f = open("input9.txt", "r")
    program = f.read().split(",")
    program = list(int(x) for x in program)

    # Part One
    print("---------------------------------------------\nPart One")
    print("---------------------------------------------")
    machine = intCode.intCodeMachine(program)
    machine.inputs = [1]
    if machine.run():
        print("Outputs:", machine.outputs)
    else:
        print("Error: program did not halt successfully!")
    print("---------------------------------------------\n\n")

    # Part Two
    print("---------------------------------------------\nPart Two")
    print("---------------------------------------------")
    machine = intCode.intCodeMachine(program)
    machine.inputs = [2]
    if machine.run():
        print("Outputs:", machine.outputs)
    else:
        print("Error: program did not halt successfully!")
    print("---------------------------------------------")

    
main()
