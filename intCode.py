# Extract parameter modes from an instruction, for up to three parameters
def get_modes(instr):
    c_mode = instr // 10000
    b_mode = (instr % 10000) // 1000
    a_mode = (instr % 1000)  // 100
    return (a_mode, b_mode, c_mode)

class intCodeMachine:
    def __init__(self, program):
        self.size = len(program)
        self.memory = list(x for x in program)
        self.pos = 0
        self.inputs = []
        self.outputs = []
        self.waitingForInput = False

    # Get 'num' parameters give the parameters modes
    def __get_ops(self, num, modes):
        (a_mode, b_mode, c_mode) = modes
        a = (self.memory[self.pos+1] if a_mode == 1 else self.memory[self.memory[self.pos+1]]) if num >= 1 else None
        b = (self.memory[self.pos+2] if b_mode == 1 else self.memory[self.memory[self.pos+2]]) if num >= 2 else None
        c = (self.memory[self.pos+3] if c_mode == 1 else self.memory[self.memory[self.pos+3]]) if num >= 3 else None
        return (a, b, c)

    def expand_memory(self, size):
        to_add = size - len(self.memory)
        for i in range(to_add): self.memory.append(0)
        
    def mem_get(self, position):
        if position > len(self.memory): self.expand_memory(position+1)
        return self.memory[position]

    def mem_set(self, position, value):
        if position > len(self.memory): self.expand_memory(position+1)
        self.memory[position] = value
        
    # Begin/Continue Running the machine
    def run(self, debug = False):
        if debug: print("Length", len(self.memory))
        
        while (self.pos != self.size and self.mem_get(self.pos) != 99):
            opcode = self.mem_get(self.pos) % 100
            (a_mode, b_mode, c_mode) = get_modes(self.mem_get(self.pos))
            modes = (a_mode, b_mode, 1)

            if opcode not in range(1,8+1):
                print("ERROR: unsupported opcode: " + str(opcode))
                break

            if (opcode == 1):
                (a, b, c) = self.__get_ops(3, modes)
                self.mem_set(c, a + b)
                self.pos += 4
                if debug: print("add", a, "+", b, "into", c)
            elif (opcode == 2):
                (a, b, c) = self.__get_ops(3, modes)
                self.mem_set(c, a * b)
                self.pos += 4
                if debug: print("mul", a, "*", b, "into", c)
            elif (opcode == 3):
                modes = (1, 1, 1)
                (a, _, _) = self.__get_ops(1, modes)
                if (len(self.inputs) == 0):
                    self.waitingForInput = True
                    return False
                self.mem_set(a, self.inputs.pop())
                self.pos += 2
                if debug: print("input into", a)
            elif (opcode == 4):
                (a, _, _) = self.__get_ops(1, modes)
                if debug: print(a)
                self.outputs.append(a)
                self.pos += 2
                if debug: print("output from", a)
            elif (opcode == 5):
                (a, b, _) = self.__get_ops(2, modes)
                self.pos = b if a != 0 else self.pos + 3
                if debug: print("jump non-zero to", b)
            elif (opcode == 6):
                (a, b, _) = self.__get_ops(2, modes)
                self.pos = b if a == 0 else self.pos + 3
                if debug: print("jump zero to", b)
            elif (opcode == 7):
                (a, b, c) = self.__get_ops(3, modes)
                self.mem_set(c, 1 if a < b else 0)
                self.pos += 4
                if debug: print("ly", a, "<", b, "into", c)
            elif (opcode == 8):
                (a, b, c) = self.__get_ops(3, modes)
                self.mem_set(c, 1 if a == b else 0)
                self.pos += 4
                if debug: print("eq", a, "==", b, "into", c)

        return True
