package DailyProblems;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Utils {

  static long[] readProgramFromFile(String filename) {
    try {
      File inputFile = new File(filename);
      Scanner myReader = new Scanner(inputFile);
      String data = myReader.nextLine();
      myReader.close();
      String[] strInstructions = data.split(",");
      long[] program = new long[strInstructions.length];
      for (int i = 0; i < strInstructions.length; i++) {
        program[i] = Long.parseLong(strInstructions[i]);
      }
      return program;
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    return new long[]{};
  }
}
