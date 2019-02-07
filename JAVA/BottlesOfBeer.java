
public class BottlesOfBeer {
  public static void main(String args[]) {
  
    int beers;

    for (beers = 99; beers > 0; beers--) {
      System.out.println(beers + " bottle(s) of beer on the wall, " + beers + " bottle(s) of beer,");
      System.out.println("Take one down, pass it around, " + (beers-1) + " bottle(s) of beer on the wall.\n");
    }
    System.out.println(beers + " bottle(s) of beer on the wall, " + beers + " bottle(s) of beer,");
    System.out.println("Go to the store, buy some more, 99 bottles of beer on the wall.\n");
  }
}

