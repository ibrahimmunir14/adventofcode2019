package DailyProblems;

import intCode.intCodeMachine;

import java.util.List;

public class Day5 {

  public static void main(String[] args) {
    long[] program = Utils.readProgramFromFile("inputs\\input5.txt");

    /* Part 1 */
    System.out.println("Part 1:");
    Long output = runDiagnostics(program, 1);
    System.out.print("Diagnostic Code: " + output.toString());
    System.out.println();

    /* Part 2 */
    System.out.println("Part 2:");
    output = runDiagnostics(program, 5);
    System.out.print("Diagnostic Code: " + output.toString());
    System.out.println();
  }

  private static Long runDiagnostics(long[] program, long input) {
    intCodeMachine machine = new intCodeMachine(program);
    machine.addInputs(List.of(input));
    boolean halted = machine.run();
    assert(halted);
    while (machine.outputSize() > 1) {
      machine.popOutput();
    }
    return machine.popOutput();
  }



}

