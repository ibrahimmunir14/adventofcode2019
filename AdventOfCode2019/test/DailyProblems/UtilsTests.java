package DailyProblems;

import org.junit.Test;

import java.util.Arrays;

public class UtilsTests {

  @Test
  public void readProgramFromFileTest() {
    long[] program = Utils.readProgramFromFile("../inputs/testInput.txt");
    assert(Arrays.equals(program, new long[]{39L, 43, 1, 5, 43, 47, 1, 5, 0}));
  }
}
