package DailyProblems;

import intCode.intCodeMachine;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class Day11 {

  public static void main(String[] args) {
    long[] program = Utils.readProgramFromFile("inputs\\input11.txt");

    /* Part 1 */
    System.out.println("Part 1");
    PaintingRobot robot = new PaintingRobot(program);
    robot.run();
    System.out.println("# of painted panels: " + robot.countPaintedPanels());
    System.out.println();

    /* Part 2 */
    System.out.println("Part 2");
    robot = new PaintingRobot(program);
    robot.startOnWhite();
    robot.run();
    robot.printPanels();
    System.out.println();
    System.out.println();

  }
}

class Coordinate {
  final int x;
  final int y;

  Coordinate(int x, int y) {
    this.x = x;
    this.y = y;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Coordinate that = (Coordinate) o;
    return x == that.x &&
        y == that.y;
  }

  @Override
  public int hashCode() {
    return Objects.hash(x, y);
  }

  @Override
  public String toString() {
    return "(" + x + ',' + y + ')';
  }
}

class PaintingRobot {
  private enum Direction {RIGHT, UP, DOWN, LEFT};
  // Colour :: True = White; False = Black

  private final long[] program;
  private final Map<Coordinate, Boolean> paintedPanels;
  private Direction direction;
  private int x;
  private int y;

  public PaintingRobot(long[] program) {
    this.program = program;
    this.paintedPanels = new HashMap<>();
    this.direction = Direction.UP;
    this.x = 0;
    this.y = 0;
  }

  public void run() {
    intCodeMachine machine = new intCodeMachine(program);
    boolean halted = machine.run();
    while (!halted) {
      machine.addInput(detectPanelColour() ? 1L : 0);
      halted = machine.run();
      assert (machine.outputSize() == 2);
      paintPanel(machine.popOutput() == 1);
      changeDirection(machine.popOutput() == 1);
      moveForward();
    }
  }

  private void moveForward() {
    if (this.direction == Direction.UP) this.y += 1;
    else if (this.direction == Direction.DOWN) this.y -= 1;
    else if (this.direction == Direction.LEFT) this.x -= 1;
    else this.x += 1;
  }

  private void changeDirection(boolean turn) {
    if (direction == Direction.UP) direction = turn ? Direction.RIGHT: Direction.LEFT;
    else if (direction == Direction.RIGHT) direction = turn ? Direction.DOWN : Direction.UP;
    else if (direction == Direction.DOWN) direction = turn ? Direction.LEFT : Direction.RIGHT;
    else direction = turn ? Direction.UP : Direction.DOWN;
  }

  private boolean detectPanelColour() {
    return paintedPanels.getOrDefault(new Coordinate(this.x, this.y), false);
  }

  private void paintPanel(boolean colour) {
    paintedPanels.put(new Coordinate(this.x, this.y), colour);
  }

  public int countPaintedPanels() {
    return paintedPanels.size();
  }

  public void printPanels() {
    // calculate range of coordinates
    int minX = 0, maxX = 0, minY = 0, maxY = 0;
    for (Coordinate coord : paintedPanels.keySet()) {
      if (coord.x < minX) minX = coord.x;
      if (coord.x > maxX) maxX = coord.x;
      if (coord.y < minY) minY = coord.y;
      if (coord.y > maxY) maxY = coord.y;
    }
    // print colour of panels
    for (int y = maxY; y >= minY; y--) {
      for (int x = minX; x <= maxX; x++) {
        Boolean colour = paintedPanels.getOrDefault(new Coordinate(x, y), false);
        System.out.print((colour ? "+" : " "));
      }
      System.out.println();
    }
  }

  public void startOnWhite() {
    assert (this.x == 0 && this.y == 0 && paintedPanels.size() == 0);
    paintPanel(true);
  }
}

