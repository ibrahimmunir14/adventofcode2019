import intCode

def main():
    print_result("test_opcodes_1_2:", test_opcodes_1_2())
    print_result("test_opcodes_3_4:", test_opcodes_3_4())
    print_result("test_parameter_modes:", test_parameter_modes())
    print_result("test_opcodes_5_6:", test_opcodes_5_6())
    print_result("test_opcode_7:", test_opcode_7())
    print_result("test_opcode_8:", test_opcode_8())
    print_result("test_opcodes_5_6_7_8:", test_opcodes_5_6_7_8())
    print_result("test_day5_diagnostic_a:", test_day5_diagnostic_a())
    print_result("test_day5_diagnostic_b:", test_day5_diagnostic_b())
    print_result("test_opcode_9_and_large_mem:", test_opcode_9_and_large_mem())
    print_result("test_large_number", test_large_number())
    print()

def print_result(name, result):
    passed, total = result
    print('{:>30}  {:>2} / {:>2} Passed'.format(name, passed, total))

def final_memory_match(program, final_memory):
    machine = intCode.intCodeMachine(program)
    if (not machine.run()): return False
    return final_memory == machine.memory

def compare_memories(program_states):
    passed = 0
    for (program, program_end) in program_states:
        if final_memory_match(program, program_end): passed += 1
    return passed, len(program_states)

def test_opcodes_1_2():
    program_states = [([1,9,10,3,2,3,11,0,99,30,40,50],[3500,9,10,70,2,3,11,0,99,30,40,50]),
                      ([1,0,0,0,99],[2,0,0,0,99]),
                      ([2,3,0,3,99],[2,3,0,6,99]),
                      ([2,4,4,5,99,0],[2,4,4,5,99,9801]),
                      ([1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99])]
    return compare_memories(program_states)
    
def input_output_match(program, inputs, expected_outputs):
    machine = intCode.intCodeMachine(program)
    machine.inputs = inputs
    if (not machine.run()): return False
    return machine.outputs == expected_outputs

def compare_inputs_outputs(pios):
    passed = 0
    for (program, inputs, outputs) in pios:
        if input_output_match(program, inputs, outputs): passed += 1
    return passed, len(pios)
    
def test_opcodes_3_4():
    pios = []
    for i in range(10):
        pios.append(([3,0,4,0,99], [i], [i]))
    return compare_inputs_outputs(pios)

def test_parameter_modes():
    program_states = [([1002,4,3,4,33],[1002,4,3,4,99]),
                      ([1101,100,-1,4,0],[1101,100,-1,4,99])]
    return compare_memories(program_states)

def test_opcodes_5_6():
    program_zero_a = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    program_zero_b = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    pios = []
    for i in range(-10, 0):
        pios.append( (program_zero_a, [i], [1]) )
        pios.append( (program_zero_b, [i], [1]) )
    for i in range(1, 10):
        pios.append( (program_zero_a, [i], [1]) )
        pios.append( (program_zero_b, [i], [1]) )
    pios.append( (program_zero_a, [0], [0]) )
    pios.append( (program_zero_b, [0], [0]) )
    return compare_inputs_outputs(pios)
    
def test_opcode_7():
    program_lt_8_a = [3,9,7,9,10,9,4,9,99,-1,8]
    program_lt_8_b = [3,3,1107,-1,8,3,4,3,99]
    pios = []
    for i in range(-4, 8):
        pios.append( (program_lt_8_a, [i], [1]) )
        pios.append( (program_lt_8_b, [i], [1]) )
    for i in range(8, 16):
        pios.append( (program_lt_8_a, [i], [0]) )
        pios.append( (program_lt_8_b, [i], [0]) )
    return compare_inputs_outputs(pios)

def test_opcode_8():
    program_equal_8_a = [3,9,8,9,10,9,4,9,99,-1,8]
    program_equal_8_b = [3,3,1108,-1,8,3,4,3,99]
    pios = []
    for i in range(-4, 8):
        pios.append( (program_equal_8_a, [i], [0]) )
        pios.append( (program_equal_8_b, [i], [0]) )
    for i in range(9, 16):
        pios.append( (program_equal_8_a, [i], [0]) )
        pios.append( (program_equal_8_b, [i], [0]) )
    pios.append( (program_equal_8_a, [8], [1]) )
    pios.append( (program_equal_8_b, [8], [1]) )
    return compare_inputs_outputs(pios)

def test_opcodes_5_6_7_8():
    program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    pios = []
    for i in range(-16, 8):
        pios.append( (program, [i], [999]) )
    for i in range(9, 24):
        pios.append( (program, [i], [1001]) )
    pios.append( (program, [8], [1000]) )
    return compare_inputs_outputs(pios)

def test_day5_diagnostic_a():
    f = open("input5.txt", "r")
    program = f.read().split(",")
    program = list(int(x) for x in program)
    machine = intCode.intCodeMachine(program)
    machine.inputs = [1]
    passed = 0
    if machine.run():
        for o in machine.outputs[:-1]:
            if (o == 0): passed += 1
        if (machine.outputs[-1] == 15259545): passed += 1
    return passed, len(machine.outputs)

def test_day5_diagnostic_b():
    f = open("input5.txt", "r")
    program = f.read().split(",")
    program = list(int(x) for x in program)
    machine = intCode.intCodeMachine(program)
    machine.inputs = [5]
    passed = 0
    if machine.run():
        passed = int(machine.outputs[-1] == 7616021)
    return passed, 1

def test_opcode_9_and_large_mem():
    quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    machine = intCode.intCodeMachine(quine)
    if (not machine.run()): return "Error"
    return int(machine.outputs == quine), 1

def test_large_number():
    program = [1102,34915192,34915192,7,4,7,99,0]
    machine = intCode.intCodeMachine(program)
    if (machine.run() and len(machine.outputs) == 1):
        passed = int(len(str(machine.outputs[0])) == 16)
    program = [104,1125899906842624,99]
    machine = intCode.intCodeMachine(program)
    if (machine.run() and len(machine.outputs) == 1):
        passed += int(machine.outputs[0] == 1125899906842624)
    return passed, 2
    
main()
