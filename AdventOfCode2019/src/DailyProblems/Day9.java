package DailyProblems;

import intCode.intCodeMachine;

import java.util.List;

public class Day9 {

  public static void main(String[] args) {
    long[] program = Utils.readProgramFromFile("inputs\\input9.txt");

    /* Part 1 */
    System.out.println("Part 1 (BOOST keycode):");
    List<Long> outputs = runBoostProgram(program, 1);
    System.out.print("Outputs: " + outputs.toString());
    System.out.println();

    /* Part 2 */
    System.out.println("Part 2 (distress signal coordinates):");
    outputs = runBoostProgram(program, 2);
    System.out.print("Outputs: " + outputs.toString());
    System.out.println();
  }

  private static List<Long> runBoostProgram(long[] program, long input) {
    intCodeMachine machine = new intCodeMachine(program);
    machine.addInputs(List.of(input));
    boolean halted = machine.run();
    assert(halted);
    return machine.getOutputs();
  }



}

