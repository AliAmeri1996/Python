
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=["alarm","bridge","maze","eiffel"]
chosen_word=random.choice(word_list)
lives=6

display=[]
for i in (chosen_word): 
   display.append("_")
print(display)

end_of_game=False
while not end_of_game:
   guess=input("guess a letter?").lower()
   for position in range(len(chosen_word)):
      letter=chosen_word[position]
      if letter==guess:
         display[position]=letter
   if guess not in chosen_word:
      print(f"you guessed {guess}, that's not in the word. you lose a life.")
      lives-=1
      if lives==0:
         end_of_game=True
         print("you lose")
   print(display)
   if "_" not in display:
      end_of_game=True
      print("You win.")
   print(stages[lives])
