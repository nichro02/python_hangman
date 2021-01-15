# Overview
A console hangman game where the user guesses letters until they spell the word or create a hangman with too many incorrect guesses

# Structure
- This app takes an object oriented approach, with a Word class.
- Making guesses:
    - If a user guesses a letter contained in the word, that letter should populate in the word
    - The user is informed they have guessed a letter correctly
    - The game is over if the user guesses all of the letters in the word
    - The user is informed if they guess a letter incorrectly
    - The user loses the game if they have no remaining guesses and there are blank spaces on the board
    