import random

selected_word = ''
word_bank = ['pizza', 'python', 'sleep', 'class']

def get_random_word():
    return random.choice(word_bank)

class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
    
    def check_letter(self):
        print('Hit check letter')




game = {
    'current_word': ' _ ' * len(),
    'guessed_letters': [],
    'guesses_left': 8,
    
    def start_game():
        #initiate game
    

    def show_scoreboard():
        #display remaining letters
        #display remaining turns
    

    def process_user_guess():
        #GAME LOGIC

        #check to see if word has been guessed, game is won

        #check to see if guesses_left > 0

        #else if guesses left = 0, game is over
    
}