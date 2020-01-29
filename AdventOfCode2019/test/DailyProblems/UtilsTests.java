package DailyProblems;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class UtilsTests {

  @Test
  public void readProgramFromFileTest() {
    long[] program = Utils.readProgramFromFile("../inputs/testInput.txt");
    assert(Arrays.equals(program, new long[]{39L, 43, 1, 5, 43, 47, 1, 5, 0}));
  }

  @Test
  public void permutationsOfIntTest() {
    Integer list[] = new Integer[]{1,2,3};
    ArrayList<ArrayList<Integer>> permutations = Utils.permutations(list);
    ArrayList<List<Integer>> realPermutations = new ArrayList<>();
    realPermutations.add(Arrays.asList(1,2,3));
    realPermutations.add(Arrays.asList(1,3,2));
    realPermutations.add(Arrays.asList(2,1,3));
    realPermutations.add(Arrays.asList(2,3,1));
    realPermutations.add(Arrays.asList(3,1,2));
    realPermutations.add(Arrays.asList(3,2,1));
    assert permutations.containsAll(realPermutations);
    assert permutations.size() == realPermutations.size();
    assert realPermutations.containsAll(permutations);
  }

  @Test
  public void permutationsOfLongTest() {
    Long list[] = new Long[]{1L,2L,3L};
    ArrayList<ArrayList<Long>> permutations = Utils.permutations(list);
    ArrayList<List<Long>> realPermutations = new ArrayList<>();
    realPermutations.add(Arrays.asList(1L,2L,3L));
    realPermutations.add(Arrays.asList(1L,3L,2L));
    realPermutations.add(Arrays.asList(2L,1L,3L));
    realPermutations.add(Arrays.asList(2L,3L,1L));
    realPermutations.add(Arrays.asList(3L,1L,2L));
    realPermutations.add(Arrays.asList(3L,2L,1L));
    assert permutations.containsAll(realPermutations);
    assert permutations.size() == realPermutations.size();
    assert realPermutations.containsAll(permutations);
  }
}
