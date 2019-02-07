
#include <stdio.h>

int beers;

main() {
  for (beers = 99; beers > 0; beers--) {
    if (beers == 1) {
      printf("%d bottle of beer on the wall, %d bottle of beer,\n", beers, beers);
      printf("Take one down, pass it around, %d bottles of beer on the wall. \n\n", (beers-1));
    } else {
      if (beers == 2) {
        printf("%d bottles of beer on the wall, %d bottles of beer,\n", beers, beers);
        printf("Take one down, pass it around, %d bottle of beer on the wall. \n\n", (beers-1));
      } else {
        printf("%d bottles of beer on the wall, %d bottles of beer,\n", beers, beers);
        printf("Take one down, pass it around, %d bottles of beer on the wall. \n\n", (beers-1));
      }        
    }
  }
  printf("%d bottles of beer on the wall, %d bottles of beer,\n", beers, beers);
  printf("Go to the store, buy some more, 99 bottles of beer on the wall.\n\n");
}

