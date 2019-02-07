
beers = 99
while beers > 0:
    if beers == 1:
        print(beers, "bottle of beer on the wall, ", beers, " bottle of beer,")
    else:
        print(beers, "bottles of beer on the wall, ", beers, " bottles of beer,")
    if beers == 2:
        print("Take one down, pass it around, ", beers-1, "bottle of beer on the wall. \n")
    else:
        print("Take one down, pass it around, ", beers-1, "bottles of beer on the wall. \n")
    beers = beers-1
print(beers, "bottles of beer on the wall, ", beers, " bottles of beer,")
print("Go to the store, buy some more, 99 bottles of beer on the wall.")
