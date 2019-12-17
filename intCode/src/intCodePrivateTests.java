import org.junit.Test;

import java.util.Arrays;

public class intCodePrivateTests {

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
}
