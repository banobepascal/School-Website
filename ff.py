import random

print("Welcome to the guessing game")

while True:
    print("Enter a number between 1 and 6")
    usr = int(input())
    values = random.randint(1,6)
    print(values)
    if usr == values:
     print("Nice work, you guessed it")
    else:
     print("Wronggg, try again")
    print("Would you like to try again?")cm
    promp = input()
    if promp == 'Y':
        continue
    else: 
      break