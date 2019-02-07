
public class BottlesOfBeer_v2 {
  public static void main(String args[]) {
  
    int beers;

    for (beers = 99; beers > 0; beers--) {
      if (beers == 1) {
        System.out.println(beers + " bottle of beer on the wall, " + beers + " bottle of beer,");
        System.out.println("Take one down, pass it around, " + (beers-1) + " bottles of beer on the wall.\n");
      } else {
        if (beers == 2) {
          System.out.println(beers + " bottles of beer on the wall, " + beers + " bottles of beer,");
          System.out.println("Take one down, pass it around, " + (beers-1) + " bottle of beer on the wall.\n");
        } else { 
          System.out.println(beers + " bottles of beer on the wall, " + beers + " bottles of beer,");
          System.out.println("Take one down, pass it around, " + (beers-1) + " bottles of beer on the wall.\n");
        }
      }  
    }
    System.out.println(beers + " bottles of beer on the wall, " + beers + " bottles of beer,");
    System.out.println("Go to the store, buy some more, 99 bottles of beer on the wall.\n");
  }
}

