import intCode

def main():
    f = open("input5.txt", "r")
    program = f.read().split(",")
    program = list(int(x) for x in program)
    #program = [1002,4,3,4,33]
    #program = [3,0,4,0,99]
    #program = [1101,100,-1,4,0]

    print("Part 1 (inputs = [1])")
    machine = intCode.intCodeMachine(program)
    machine.inputs = [1]
    halted = machine.run()
    if (not halted): print("Error: the machine did not halt successfully!")
    print("Outputs:", machine.outputs)
    print("Diagnostic Code:", machine.outputs[-1])
    print()

    print("Part 2 (inputs = [2])")
    machine = intCode.intCodeMachine(program)
    machine.inputs = [5]
    halted = machine.run()
    if (not halted): print("Error: the machine did not halt successfully!")
    print("Outputs:", machine.outputs)
    print("Diagnostic Code:", machine.outputs[-1])
    
main()
