import intCode

def main():
    f = open("input2.txt", "r")
    program = f.read().split(",")[:-1]
    program = list(int(x) for x in program)

    noun, verb = findNounVerb(program, 19690720)
    
    print("Noun:", noun, "; Verb:", verb)
    print("100 * noun + verb =", 100 * noun + verb)
            
    
def run_program(program, noun, verb):
    machine = intCode.intCodeMachine(program)
    machine.memory[1] = noun
    machine.memory[2] = verb
    halted = machine.run()
    if (not halted): print ("Error: the machine did not halt successfully!")
    return machine.memory[0]

def findNounVerb(program, output):
    for noun in range(0,99):
        for verb in range(0,99):
            res = run_program(program, noun,verb)
            if (res == output):
                return noun, verb
main()
