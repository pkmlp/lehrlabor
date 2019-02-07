
#include <stdio.h>

int beers;

main() {
  for (beers = 99; beers > 0; beers--) { 
    printf("%d bottle(s) of beer on the wall, %d bottle(s) of beer,\n", beers, beers);
    printf("Take one down, pass it around, %d bottle(s) of beer on the wall. \n\n", (beers-1));
  }
  printf("%d bottle(s) of beer on the wall, %d bottle(s) of beer,\n", beers, beers);
  printf("Go to the store, buy some more, 99 bottles of beer on the wall.\n\n");
}

