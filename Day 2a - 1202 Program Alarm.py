import intCode

def main():
    f = open("input2.txt", "r")
    program = f.read().split(",")[:-1]
    program = list(int(x) for x in program)

    program[1] = 12
    program[2] = 2

    machine = intCode.intCodeMachine(program)
    halted = machine.run()
    
    if (halted):
        print("memory[0] =", machine.memory[0])
    else:
        print("Error: the machine did not halt successfully!")

main()
