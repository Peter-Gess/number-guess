import random

def guessing():
    secret_num = random.randint(1, 10)
    count = 3
    for count in range(3):
      try:
        # get a number guess from the player
        guess = int(input('Guess a number between 1 and 10: '))
      except ValueError:
          print("That is not a number!")
          continue
      if guess == secret_num:
          print("You got it! My number was {}".format(secret_num))
          again = str(input("Do you want to play again?  YES or NO "))
          if again == "NO":
            break
          if again == "YES":
            guessing()
      else:
          if guess > secret_num:
              print("Thats too high!")
          elif guess < secret_num:
              print("Thats too low!")

    else:
        print("You ran out of guesses!")
        again = str(input("Do you want to play again?  Type YES or NO : "))
        if again.upper() == "NO":
            return
        if again.upper()  == "YES":
            guessing()

guessing()   
