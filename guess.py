import random

print('Hello! What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

randomNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guessedNumber = int(input())
spam =
    if guessedNumber < randomNumber:
        print('Your guess is too low. Try again')
        
    elif guessedNumber > randomNumber:
        print('Your guess is too high. Try again')

    else:
        break
if guessedNumber == randomNumber:
    print('Great job ' + name + '!' + ' You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(randomNumber) )
    


    
#print('You took ' + guessesTaken + ' guesses.')
    
    #guessedNumber = int(input())

#while guessedNumber != randomNumber:
 #   print('Take a guess.')
  #  if guessedNumber > randomNumber:
   #     print('Your guess is too high. Try again')
   # elif guessedNumber < randomNumber:
    #    print('Your guess is too low. Try again')
    #else:
       # break
#if guessedNumber == randomNumber:
  #  print('Great job ' + name + '!')
