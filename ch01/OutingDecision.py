print("Oh, you seems to wanna go out")

f = input("How many there are fuels in car?: ")

fuel = int(f)

if fuel > 3:
    print("It's OK")
else:
    m = int(input("then, How much money do you have?: "))
    if m > 10:
        print("You should buy some gas")
    else:
        print("You better stay at home")

print("What's next?")
