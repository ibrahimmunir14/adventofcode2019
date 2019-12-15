import intCode
import itertools

def main():
    f = open("input7.txt", "r")
    program = f.read().split(",")
    program = list(int(x) for x in program)
    #program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,
    #           4,27,1001,28,-1,28,1005,28,6,99,0,0,5] # 139629729, (9,8,7,6,5)
    #program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
    #            -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
    #            53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10] # 18216 (9,7,8,5,6)

    print("Part One (phases settings 0-4)")
    phasecombos = itertools.permutations(range(5,10))
    max_output = 0
    max_phases = None
    for phases in phasecombos:
        output = amp_circuit(program, phases)
        if (output > max_output):
            max_output = output
            max_phases = phases
    print("Maximum Output to Thrusters:", max_output)
    print("Phase setting sequence:", max_phases)
    print()

    print("Part Two (phases settings 5-9)")
    phasecombos = itertools.permutations(range(5))
    max_output = 0
    max_phases = None
    for phases in phasecombos:
        output = amp_circuit(program, phases)
        if (output > max_output):
            max_output = output
            max_phases = phases
    print("Maximum Output to Thrusters:", max_output)
    print("Phase setting sequence:", max_phases)
    print()

def amp_circuit(program, phases):
    machines = list(intCode.intCodeMachine(program) for i in range(5))
    phases = list(phases)
    # start all amplifiers with their phases
    for i in range(5):
        machines[i].inputs = [phases[i]]
        machines[i].run()

    output = 0
    amp = 0
    while (True):
        # run an amplifier providing it the last amp's output as its input
        # the amplifier will output a value and then wait for further input
        # we carry the output over for the next amp
        machine = machines[amp]
        machine.inputs = [output]
        halted = machine.run()
        output = machine.outputs.pop(0)
        # if amplifier E has halted, exit the feedback loop, return the final output
        if (halted and amp == 4): return output
        # there are 5 amps, go to next amp
        amp = (amp + 1) % 5



main()
