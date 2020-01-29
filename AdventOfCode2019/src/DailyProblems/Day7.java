package DailyProblems;

import intCode.intCodeMachine;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day7 {

  public static void main(String[] args) {
    long[] program = Utils.readProgramFromFile("inputs\\input7.txt");

    /* Part 1 */
    System.out.println("Part 1 (phases settings 0-4):");
    AmpCircuitSettings acs1 = findHighestSignal(program, new Long[]{0L,1L,2L,3L,4L});
    System.out.println("Maximum Output to Thrusters: " + acs1.output);
    System.out.println("Phase setting sequence: " + acs1.phases.toString());
    System.out.println();

    /* Part 2 */
    System.out.println("Part 2 (phases settings 5-9):");
    AmpCircuitSettings acs2 = findHighestSignal(program, new Long[]{5L,6L,7L,8L,9L});
    System.out.println("Maximum Output to Thrusters: " + acs2.output);
    System.out.println("Phase setting sequence: " + acs2.phases.toString());
    System.out.println();

  }

  private static AmpCircuitSettings findHighestSignal(long[] program, Long[] phaseSettings) {
    long max_output = -1;
    ArrayList<Long> max_phases = new ArrayList<>();
    ArrayList<ArrayList<Long>> phase_combos = Utils.permutations(phaseSettings);
    for (ArrayList<Long> phases : phase_combos) {
      long output = ampCircuit(program, phases);
      if (output > max_output) {
        max_output = output;
        max_phases = phases;
      }
    }
    return new AmpCircuitSettings(max_output, max_phases);
  }

  private static long ampCircuit(long[] program, ArrayList<Long> phases) {
    int numMachines = phases.size();
    // start machines with their respective phases
    intCodeMachine machines[] = new intCodeMachine[numMachines];
    for (int i = 0; i < numMachines; i++) {
      machines[i] = new intCodeMachine(program);
      machines[i].addInputs(List.of(phases.get(i)));
      machines[i].run();
      assert(machines[i].isWaitingForInput());
    }

    long output = 0;
    int amp = 0;
    boolean halted = false;
    while (!(halted && amp == 0)) {
      intCodeMachine machine = machines[amp];
      machine.addInputs(List.of(output));
      halted = machine.run();
      assert(halted != machine.isWaitingForInput());
      output = machine.popOutput();
      amp = (amp + 1) % numMachines;
    }
    return output;
  }



}

class AmpCircuitSettings {
  final long output;
  final ArrayList<Long> phases;
  AmpCircuitSettings(long output, ArrayList<Long> phases) {
    this.output = output;
    this.phases = phases;
  }
}

