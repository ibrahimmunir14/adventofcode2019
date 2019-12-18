package DailyProblems;

import intCode.intCodeMachine;

import java.util.List;

public class Day5 {

  public static void main(String[] args) {
    long[] program = Utils.readProgramFromFile("inputs\\input5.txt");

    /* Part 1 */
    System.out.println("Part 1:");
    List<Long> outputs = runDiagnostics(program, 1);
    System.out.print("Outputs: ");
    for (Long e : outputs) System.out.print(e + " ");
    System.out.println();
    System.out.println();

    /* Part 2 */
    System.out.println("Part 2:");
    outputs = runDiagnostics(program, 5);
    System.out.print("Outputs: ");
    for (Long e : outputs) System.out.print(e + " ");
    System.out.println();
    System.out.println();
  }

  private static List<Long> runDiagnostics(long[] program, long input) {
    intCodeMachine machine = new intCodeMachine(program);
    machine.addInputs(List.of(input));
    boolean halted = machine.run();
    assert(halted);
    return machine.getOutputs();
  }



}

