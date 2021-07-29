import random
import hangman_art
import hangman_word

print(hangman_art.logo)
end_of_game = False
word_list = hangman_word.Word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')


#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    # prompting user for guess
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"you have already guessed this letter, {guess}\n")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    if guess not in chosen_word:
        print(f"your guess {guess}, is not in the chosen word. you loss a life. \n")

    #Join all the elements in the list and turn it into a String.
    # print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])