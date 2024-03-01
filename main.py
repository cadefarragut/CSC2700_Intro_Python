#hangman
import random 

words = ["computer", "science", "hangman", "python", "program", "variable", "algorithm", "integer", "boolean"]


def Hangman(guesses):        #Pictures of hangman after each wrong guess
  if(guesses == 0):
     print("----| ")
     print("|   |")
     print("|    ")
     print("|    ")
     print("|     ")
     print("|     ")
     print("|______     ")
  if(guesses == 1):  
     print("----| ")
     print("|   |")
     print("|   O")
     print("|    ")
     print("|     ")
     print("|     ")
     print("|______     ")
  if(guesses == 2):
   print("----| ")
   print("|   |")
   print("|   O")
   print("|   |")
   print("|     ")
   print("|     ")
   print("|______     ")
  if(guesses == 3):
     print("----| ")
     print("|   |")
     print("|   O")
     print("|   |__")
     print("|   |  ")
     print("|     ")
     print("|______     ")
  if(guesses == 4):
     print("----| ")
     print("|   |")
     print("|   O")
     print("| __|__")
     print("|   |  ")
     print("|     ")
     print("|______     ")
  if(guesses == 5):
   print("----| ")
   print("|   |")
   print("|   O")
   print("| __|__")
   print("|   |")
   print("|    \ ")
   print("|______     ")
  if(guesses == 6):
   print("----| ")
   print("|   |")
   print("|   O")
   print("| __|__")
   print("|   |")
   print("|  / \ ")
   print("|______     ")

def word_display():        #Function displays the guesses of the user
  display_word = ''
  for letter in word:
    if letter in guessed_letters:
      display_word += letter + ''
    else:
      display_word += '_ '
  return display_word.rstrip()


def is_in_word(word, userin):     #Function checks if the user input is in the word
  global guesses
  if userin == '=':
    print('Thank you for playing, the word was', word)
    exit()
  if userin.isalpha() and len(userin) == 1:
    userin = userin.lower()
    if userin in guessed_letters:
      print('You already guessed that letter')
    elif userin in word:
      guessed_letters.add(userin)
    else:
      guessed_letters.add(userin)
      guesses+=1
    print(word_display())
  else:
    print('Please enter a single letter')
    


def Game():
  global guesses
  print('press = if you want to quit the game')
  while guesses < 6:
    if all(letter in guessed_letters for letter in word):
      print('Congratulations! You guessed the word:', word)
      break
    Hangman(guesses)
    userin = input('Guess a letter: ')
    is_in_word(word, userin)
  if guesses == 6:
    Hangman(guesses)
    print('You lost! The word was:', word)
  
    


guessed_letters = set()

word_select = random.randint(0, len(words) - 1)
word = words[word_select]
guesses = 0

print("Welcome to Hangman!")
print("The word has", len(word), "letters.")
print("You have 6 guesses to guess the word.")
print('Good Luck!')


Game()
  
  
