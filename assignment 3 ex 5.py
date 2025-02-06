def bottle_verse(b):
    print(f"""{b} Bottles of beer on the wall
{b} Bottles of beer
Take one down, pass it around""")
    b = b - 1
    if b == 0:
        print("There's no more beer!")
    else:
        bottle_verse()

b = int(input("How many bottles!: "))

bottle_verse(b)