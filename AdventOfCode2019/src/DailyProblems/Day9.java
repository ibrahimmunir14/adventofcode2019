package DailyProblems;

import intCode.intCodeMachine;

import java.util.List;

public class Day9 {

  public static void main(String[] args) {
    long[] program = Utils.readProgramFromFile("inputs\\input9.txt");

    /* Part 1 */
    System.out.println("Part 1:");
    Long output = runBoostProgram(program, 1);
    System.out.print("BOOST keycode: " + output.toString());
    System.out.println();

    /* Part 2 */
    System.out.println("Part 2:");
    output = runBoostProgram(program, 2);
    System.out.print("Distress signal coordinates: " + output.toString());
    System.out.println();
  }

  private static Long runBoostProgram(long[] program, long input) {
    intCodeMachine machine = new intCodeMachine(program);
    machine.addInputs(List.of(input));
    boolean halted = machine.run();
    assert(halted);
    assert(machine.outputSize() == 1);
    return machine.popOutput();
  }



}

