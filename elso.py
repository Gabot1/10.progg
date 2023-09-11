#x = int(input("Adjál egy egész számot = "))
nem = True

while nem:
    x = input("Adjál egy egész számot = ")
    if x .isdecimal():
        nem = False
        szam=int(x)


if szam < 3:
    print("A megadot szám kisebb mint 3")
elif szam > 3:
    print("A megadot szám naggyob mint 3")
