
import random
from wordlist import word_list 
from stages import logo, stages





chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Testing code--------------------------------------
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guessed = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed:
        print("\033[H\033[J", end="")
        print(f"You have already guessed letter: {guess}")
    else:
        print("\033[H\033[J", end="")
        guessed += guess

        
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
    
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
       
        print(f"{guess} is not in the mysterious word")
        print(f"You lose another life:")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    