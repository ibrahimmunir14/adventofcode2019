package intCode;

import java.util.ArrayList;
import java.util.List;

public class intCodeMachine {
  private final int size;
  private final ArrayList<Long> memory = new ArrayList<>();
  private int pos = 0;
  private final ArrayList<Long> inputs = new ArrayList<>();
  private final ArrayList<Long> outputs = new ArrayList<>();
  private boolean waitingForInput = false;
  private int relativeBase = 0;

  public intCodeMachine(long[] program) {
    this.size = program.length;
    for (long e : program) {
      this.memory.add(e);
    }
  }

  public intCodeMachine(ArrayList<Long> program) {
    this.size = program.size();
    this.memory.addAll(program);
  }

  public boolean run(boolean debug) {
    if (debug) System.out.println("Memory Length: " + memory.size());

    while (pos != size && memGet(pos) != 99) {
      int instr = (int) memGet(pos);
      int opCode = Math.floorMod(instr, 100);
      int[] modes = getModes(instr);
      int aMode = modes[0];
      int bMode = modes[1];
      int cMode = modes[2];

      if (opCode == 1 || opCode == 2 || opCode == 7 || opCode == 8) {
        // Arithmetic operation on args 1, 2, result goes in arg 3
        long a = getOperand(1, aMode);
        long b = getOperand(2, bMode);
        int c = getOperandAddress(3, cMode);
        long answer;
        char opChar;
        if (opCode == 1) { answer = a + b; opChar = '+'; }
        else if (opCode == 2) { answer = a * b; opChar = '*'; }
        else if (opCode == 7) { answer = a < b ? 1 : 0; opChar = '<'; }
        else { answer = a == b ? 1 : 0; opChar = '='; }
        memSet(c, answer);
        pos += 4;
        if (debug) System.out.println("arithmetic operation: " + a + " " + opChar + " " + b + " into " + c);
      } else if (opCode == 3) { // input
        int a = getOperandAddress(1, aMode);
        if (inputs.isEmpty()) {
          waitingForInput = true;
          return false;
        }
        memSet(a, inputs.remove(0));
        pos += 2;
        if (debug) System.out.println("input into " + a);
      } else if (opCode == 4) { // output
        long a = getOperand(1, aMode);
        outputs.add(a);
        pos += 2;
        if (debug) System.out.println("output: " + a);
      } else if (opCode == 5 || opCode == 6) {
        // jump if non-zero / zero
        long a = getOperand(1, aMode);
        long b = getOperand(2, bMode);
        boolean doJump = (opCode == 5) == (a != 0);
        pos = doJump ? (int) b : pos + 3;
        if (debug) System.out.println("jump to " + b + " if " + a + " " + (opCode == 5 ? "!=" : "==") + " 0");
      } else if (opCode == 9) {
        long a = getOperand(1, aMode);
        relativeBase += a;
        pos += 2;
        if (debug) System.out.println("change relative base by " + a);
      }
    }
    return true;
  }

  public boolean run() {
    return run(false);
  }

  private long memGet(int index) {
    if (index >= memory.size()) { expandMemory(index + 1); }
    return memory.get(index);
  }

  private void memSet(int index, long value) {
    if (index >= memory.size()) { expandMemory(index + 1); }
    memory.set(index, value);
  }

  private void expandMemory(int size) {
    for (int i = memory.size(); i < size; i++) {
      memory.add(0L);
    }
  }

  protected static int[] getModes(int instr) {
    int c_mode = Math.floorDiv(instr, 10000);
    int b_mode = Math.floorDiv(Math.floorMod(instr, 10000), 1000);
    int a_mode = Math.floorDiv(Math.floorMod(instr, 1000), 100);
    return new int[]{a_mode, b_mode, c_mode};
  }

  private long getOperand(int opNumber, int mode) {
    switch (mode) {
      case 0:
        return memGet((int) memGet(pos + opNumber));
      case 1:
        return memGet(pos + opNumber);
      case 2:
        return memGet((int) memGet(pos + opNumber) + relativeBase);
      default:
        throw new UnsupportedOperationException("Unsupported parameter mode: " + mode);
    }
  }

  private int getOperandAddress(int opNumber, int mode) {
    switch (mode) {
      case 0:
        return (int) memGet(pos + opNumber);
      case 2:
        return (int) memGet(pos + opNumber) + relativeBase;
      default:
        throw new UnsupportedOperationException("Unsupported parameter mode: " + mode);
    }
  }

  public long[] getMemoryArray() {
    long[] mem = new long[memory.size()];
    for (int i = 0; i < memory.size(); i++) {
      mem[i] = memory.get(i);
    }
    return mem;
  }

  public void addInputs(List<Long> inputs) {
    this.inputs.addAll(inputs);
  }

  public void addInput(Long input) {
    this.inputs.add(input);
  }

  public long popOutput() {
    return outputs.remove(0);
  }

  public int outputSize() { return outputs.size(); }

  public boolean isWaitingForInput() {
    return waitingForInput;
  }
}
