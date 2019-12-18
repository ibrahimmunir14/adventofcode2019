package DailyProblems;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
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

  public static <T> ArrayList<ArrayList<T>> permutations(T[] list) {
    // Start with result = empty list
    ArrayList<ArrayList<T>> result = new ArrayList<>();
    result.add(new ArrayList<>());

    // Iterate through each member, adding it to different positions in each possible permutation so far
    for (int i = 0; i < list.length; i++) {
      ArrayList<ArrayList<T>> current = new ArrayList<>();
      // For each permutation so far, add the element to all different positions in the permutation
      for (ArrayList<T> perm : result) {
        // Element can be added at index 0, 1, 2, ..., n
        for (int j = 0; j < perm.size()+1; j++) {
          perm.add(j, list[i]);                 // put the element at position j
          current.add(new ArrayList<>(perm));   // add new permutation to current
          perm.remove(j);                       // remove the element again
        }
      }
      result = new ArrayList<>(current);        // update result to be the new current list of permutations
    }
    return result;
  }

}
