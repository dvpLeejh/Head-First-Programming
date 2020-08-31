from random import randint

secret = randint(1,10)
count = 0

print("hello")

guess = 0

while guess != secret and count != 3:
    chance = 3- count
    print("Chance:" + str(chance))
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("You win!")
    else:
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
    count += 1

print("Game over")
