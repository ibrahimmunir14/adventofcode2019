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
        self.relative_base = 0

    # Get an operand given the op number and mode
    def __get_op(self, opno, mode):
        if mode == 0:   # position mode
            return self.mem_get(self.mem_get(self.pos+opno))
        elif mode == 1: # absolute mode
            return self.mem_get(self.pos + opno)
        elif mode == 2: # relative mode
            return self.mem_get(self.mem_get(self.pos+opno) + self.relative_base)
        else:
            self.memory[len(self.memory) + 1]

    # Get the address of an operand, given the op number and mode
    def __get_op_addr(self, opno, mode):
        if mode == 0:   # position mode
            return self.mem_get(self.pos+opno)
        elif mode == 2: # relative mode
            return self.mem_get(self.pos+opno) + self.relative_base
        else:
            self.memory[len(self.memory) + 1]
            
    # Get 'num' parameters give the parameters modes
    def __get_ops(self, num, modes):
        (a_mode, b_mode) = modes
        a = self.__get_op(1, a_mode) if num >= 1 else None
        b = self.__get_op(2, b_mode) if num >= 2 else None
        return (a, b)

    # Expand memory to the give new size
    def expand_memory(self, size):
        to_add = size - len(self.memory)
        for i in range(to_add): self.memory.append(0)

    # Get the value at some position in memory
    def mem_get(self, position):
        if position > len(self.memory): self.expand_memory(position+1)
        return self.memory[position]

    # Set the value at some position in memory
    def mem_set(self, position, value):
        if position >= len(self.memory): self.expand_memory(position+1)
        self.memory[position] = value
        
    # Begin/Continue Running the machine
    def run(self, debug = False):
        if debug: print("Length", len(self.memory))
        
        while (self.pos != self.size and self.mem_get(self.pos) != 99):
            opcode = self.mem_get(self.pos) % 100
            (a_mode, b_mode, c_mode) = get_modes(self.mem_get(self.pos))
            modes = (a_mode, b_mode)

            if opcode not in range(1, 9+1):
                print("ERROR: unsupported opcode: " + str(opcode))
                break

            if (opcode == 1):
                (a, b) = self.__get_ops(2, modes)
                c = self.__get_op_addr(3, c_mode)
                self.mem_set(c, a + b)
                self.pos += 4
                if debug: print("add", a, "+", b, "into", c)
            elif (opcode == 2):
                (a, b) = self.__get_ops(2, modes)
                c = self.__get_op_addr(3, c_mode)
                self.mem_set(c, a * b)
                self.pos += 4
                if debug: print("mul", a, "*", b, "into", c)
            elif (opcode == 3):
                a = self.__get_op_addr(1, a_mode)
                if (len(self.inputs) == 0):
                    self.waitingForInput = True
                    return False
                self.mem_set(a, self.inputs.pop())
                self.pos += 2
                if debug: print("input into", a)
            elif (opcode == 4):
                (a, _) = self.__get_ops(1, modes)
                if debug: print(a)
                self.outputs.append(a)
                self.pos += 2
                if debug: print("output from", a)
            elif (opcode == 5):
                (a, b) = self.__get_ops(2, modes)
                self.pos = b if a != 0 else self.pos + 3
                if debug: print("jump non-zero to", b)
            elif (opcode == 6):
                (a, b) = self.__get_ops(2, modes)
                self.pos = b if a == 0 else self.pos + 3
                if debug: print("jump zero to", b)
            elif (opcode == 7):
                (a, b) = self.__get_ops(2, modes)
                c = self.__get_op_addr(3, c_mode)
                self.mem_set(c, 1 if a < b else 0)
                self.pos += 4
                if debug: print("ly", a, "<", b, "into", c)
            elif (opcode == 8):
                (a, b) = self.__get_ops(2, modes)
                c = self.__get_op_addr(3, c_mode)
                self.mem_set(c, 1 if a == b else 0)
                self.pos += 4
                if debug: print("eq", a, "==", b, "into", c)
            elif (opcode == 9):
                (a, _) = self.__get_ops(1, modes)
                self.relative_base += a
                self.pos += 2
                if debug: print("rb adjust by", a)

        return True
