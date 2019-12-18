package DailyProblems;

import intCode.intCodeMachine;

public class Day2 {

  public static void main(String[] args) {
    long[] program = Utils.readProgramFromFile("inputs\\input2.txt");

    /* Part 1 */
    System.out.println("Part 1:");
    long res = runProgram(program, 12, 2);
    System.out.println("memory[0] = " + res);
    System.out.println();

    /* Part 2 */
    System.out.println("Part 2:");
    NounVerb nv = findNounVerb(program, 19690720);
    System.out.println("noun = " + nv.noun + ", verb = " + nv.verb);
    System.out.println("100 * noun + verb = " + (100 * nv.noun + nv.verb));
  }

  private static long runProgram(long[] program, long noun, long verb) {
    program[1] = noun;
    program[2] = verb;
    intCodeMachine machine = new intCodeMachine(program);
    boolean halted = machine.run();
    assert(halted);
    return machine.getMemory().get(0);
  }

  private static NounVerb findNounVerb(long[] program, long output) {
    for (long noun = 0; noun < 100; noun++) {
      for (long verb = 0; verb < 100; verb++) {
        long result = runProgram(program, noun, verb);
        if (result == output) return new NounVerb(noun, verb);
      }
    }
    throw new RuntimeException("unable to find noun/verb satisfying criteria");
  }

}


class NounVerb {
  final long noun, verb;
  NounVerb(long noun, long verb) {
    this.noun = noun;
    this.verb = verb;
  }
}
