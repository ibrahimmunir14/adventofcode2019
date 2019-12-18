package intCode;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class intCodeMachineTests {

  @Test
  public void getModesTest() {
    assert(Arrays.equals(intCodeMachine.getModes(   11), new int[]{0, 0, 0}));
    assert(Arrays.equals(intCodeMachine.getModes(  100), new int[]{1, 0, 0}));
    assert(Arrays.equals(intCodeMachine.getModes( 1000), new int[]{0, 1, 0}));
    assert(Arrays.equals(intCodeMachine.getModes(10000), new int[]{0, 0, 1}));
    assert(Arrays.equals(intCodeMachine.getModes(10134), new int[]{1, 0, 1}));
    assert(Arrays.equals(intCodeMachine.getModes(20100), new int[]{1, 0, 2}));
    assert(Arrays.equals(intCodeMachine.getModes( 2233), new int[]{2, 2, 0}));
    assert(Arrays.equals(intCodeMachine.getModes(32145), new int[]{1, 2, 3}));
  }

  private boolean finalMemoryMatch(long[] program, long[] expectedMemory) {
    intCodeMachine machine = new intCodeMachine(program);
    if (!machine.run()) { return false; }
    return Arrays.equals(machine.getMemoryArray(), expectedMemory);
  }

  private boolean inputOutputMatch(long[] program, List<Long> inputs, List<Long> expectedOutputs) {
    intCodeMachine machine = new intCodeMachine(program);
    machine.addInputs(inputs);
    if (!machine.run(true)) { return false; }
    return machine.getOutputs().equals(expectedOutputs);
  }

  /* Test that opCode 1 (Add) and 2 (Multiply) work as expected */
  @Test
  public void testOperationsAddMul() {
    long[][] programs = new long[5][];
    long[][] memories = new long[5][];
    programs[0] = new long[]{1,9,10,3,2,3,11,0,99,30,40,50};
    memories[0] = new long[]{3500,9,10,70,2,3,11,0,99,30,40,50};
    programs[1] = new long[]{1,0,0,0,99};
    memories[1] = new long[]{2,0,0,0,99};
    programs[2] = new long[]{2,3,0,3,99};
    memories[2] = new long[]{2,3,0,6,99};
    programs[3] = new long[]{2,4,4,5,99,0};
    memories[3] = new long[]{2,4,4,5,99,9801};
    programs[4] = new long[]{1,1,1,4,99,5,6,0,99};
    memories[4] = new long[]{30,1,1,4,2,5,6,0,99};

    for (int i = 0; i < programs.length; i++) {
      assert(finalMemoryMatch(programs[i], memories[i]));
    }
  }

  /* Test that opCode 3 (Input) and 4 (Output) work as expected */
  @Test
  public void testOperationsInputOutput() {
    long[] program = new long[]{3,0,4,0,99};
    for (long i = 0; i < 10; i++) {
      assert(inputOutputMatch(program, List.of(i), List.of(i)));
    }
  }

  /* Test that both position and absolute parameter modes work as expected
     Relies on working implementation of opCode 1 (Add) and 2 (Multiply)  */
  @Test
  public void testPositionAndAbsoluteModes() {
    assert finalMemoryMatch(new long[]{1002, 4, 3, 4, 33}, new long[]{1002, 4, 3, 4, 99});
    assert finalMemoryMatch(new long[]{1101, 100, -1, 4, 0}, new long[]{1101, 100, -1, 4, 99});
  }

  /* Test that opCode 5 (Jump If Non-Zero) and 6 (Jump If Zero) work as expected
     Relies on working implementation of opCode 1 (Add), 3 (Input) and 4 (Output)
     Relies on working implementation of position mode */
  @Test
  public void testOperationsJumpInPosMode() {
    long[] programPos = new long[]{3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9};
    for (long i = -10; i < 10; i++) {
      assert(inputOutputMatch(programPos, List.of(i), List.of(i == 0 ? 0 : 1L)));
    }
  }

  /* Test that opCode 5 (Jump If Non-Zero) and 6 (Jump If Zero) work as expected
     Relies on working implementation of opCode 1 (Add), 3 (Input) and 4 (Output)
     Relies on working implementation of absolute mode */
  @Test
  public void testOperationsJumpInAbsMode() {
    long[] programAbs = new long[]{3,3,1105,-1,9,1101,0,0,12,4,12,99,1};
    for (long i = -10; i < 10; i++) {
      assert(inputOutputMatch(programAbs, List.of(i), List.of(i == 0 ? 0 : 1L)));
    }
  }

  /* Test that opCode 7 (Less Than) works as expected
     Relies on working implementation of opCode 3 (Input) and 4 (Output)
     Relies on working implementation of position mode */
  @Test
  public void testOperationLessThanInPosMode() {
    long[] programLt8Pos = new long[]{3,9,7,9,10,9,4,9,99,-1,8};
    for (long i = 8-10; i < 8+10; i++) {
      assert(inputOutputMatch(programLt8Pos, List.of(i), List.of(i < 8 ? 1L : 0)));
    }
  }

  /* Test that opCode 7 (Less Than) works as expected
     Relies on working implementation of opCode 3 (Input) and 4 (Output)
     Relies on working implementation of absolute mode */
  @Test
  public void testOperationLessThanInAbsMode() {
    long[] programLt8Abs = new long[]{3,3,1107,-1,8,3,4,3,99};
    for (long i = 8-10; i < 8+10; i++) {
      assert(inputOutputMatch(programLt8Abs, List.of(i), List.of(i < 8 ? 1L : 0)));
    }
  }

  /* Test that opCode 8 (Equals)) works as expected
     Relies on working implementation of opCode 3 (Input) and 4 (Output)
     Relies on working implementation of position mode */
  @Test
  public void testOperationEqualsInPosMode() {
    long[] programEq8Pos = new long[]{3,9,8,9,10,9,4,9,99,-1,8};
    for (long i = 8-10; i < 8+10; i++) {
      assert(inputOutputMatch(programEq8Pos, List.of(i), List.of(i == 8 ? 1L : 0)));
    }
  }

  /* Test that opCode 8 (Equals) works as expected
     Relies on working implementation of opCode 3 (Input) and 4 (Output)
     Relies on working implementation of absolute mode */
  @Test
  public void testOperationEqualsInAbsMode() {
    long[] programEq8Abs = new long[]{3,3,1108,-1,8,3,4,3,99};
    for (long i = 8-10; i < 8+10; i++) {
      assert(inputOutputMatch(programEq8Abs, List.of(i), List.of(i == 8 ? 1L : 0)));
    }
  }

  /* Test that opCodes 5 (Jump If Non-Zero), 6 (Jump If Zero), 7 (Less Than), 8 (Equals) work
     Relies on working implementation of opCode 3 (Input) and 4 (Output)
     Relies on working implementation of absolute mode and position mode */
  @Test
  public void testOperations5678JumpLtAndEquals() {
    long[] program = new long[]{3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                                1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                                999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99};
    for (long i = 8-10; i < 8+10; i++) {
      long expectedOut = i == 8 ? 1000 : (i < 8 ? 999 : 1001);
      assert(inputOutputMatch(program, List.of(i), List.of(expectedOut)));
    }
  }

  /* Test the ability to use large numbers in the program and memory
     Relies on working implementation of opCode 2 (Multiply) and 4 (Output)
     Relies on working implementation of absolute mode and position mode */
  @Test
  public void testLargeNumbers() {
    long[] programProduce16DigitNumber = new long[]{1102, 34915192, 34915192, 7, 4, 7, 99, 0};
    intCodeMachine machine = new intCodeMachine(programProduce16DigitNumber);
    assert(machine.run(true));
    assert(machine.getOutputs().size() == 1);
    assert(machine.getOutputs().get(0).toString().length() == 16);

    long[] programOutputLargeNumber= new long[]{104,1125899906842624L,99};
    machine = new intCodeMachine(programOutputLargeNumber);
    assert(machine.run(true));
    assert(machine.getOutputs().size() == 1);
    assert(machine.getOutputs().get(0) == 1125899906842624L);
  }

  /* Test that opCode 9 (Modify Relative Base) works as expected
     Relies on working implementation of opCode 1 (Add) and 4 (Output)
     Relies on working implementation of absolute mode and position mode */
  @Test
  public void testOperation9AndRelativeMode() {
    // relative_base += absolute 3
    // multiply 7 by relative 0, i.e. address 3, i.e. 7
    // put answer in address 0 (memory[0] = 49)
    // output address 0
    long[] program = new long[]{109, 3, 2102, 7, 0, 0, 4, 0};
    assert(inputOutputMatch(program, new ArrayList<Long>(), List.of(49L)));
  }

  @Test
  public void testLargeMemory() {
    long[] quine = new long[]{109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99};
    intCodeMachine machine = new intCodeMachine(quine);
    assert(inputOutputMatch(quine, new ArrayList<>(),
        new ArrayList<Long>() {{ for (long i : quine) add(i); }}));
  }



}
