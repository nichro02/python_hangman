import random

#selected_word = ''
word_bank = ['pizza', 'python', 'sleep', 'class']

#get random word
def get_random_word():
    return random.choice(word_bank).upper()
    
#DECLARE WORD CLASS -----------------------------
class Word():
    def __init__(self, chosen_word=None):
        self.chosen_word = get_random_word()
        pass # this method will split the word up into a list of dictionaries with 2 attributes:
        pass # the letter/character, and a boolean representing whether or not it has been guessed
    
    def split_string(self):
        word_to_list = list(self.chosen_word)
        print(word_to_list)

    def print_word(self):
        print('Hit print word', self.chosen_word)

    def check_letter(self):
        print('Hit check letter')

answer = Word()
#test that random word gets selected and split into list
answer.print_word()
answer.split_string()

#FUNCTIONS -------------------------------------
def decrement_round():
    print('starting round', game['guesses_left'])
    game['guesses_left'] -= 1
    print('rounds left,', game['guesses_left'])

def game_flow_logic():
    pass #inset game flow here
    if game['guesses_left'] > 0:
        guess = input('Please guess a letter ').upper()
        #evaluate if guessed letter is in word
        print(guess)
        win_scenario()
    else:
        print('Too bad! You ran out of guesses before you could spell the word')


def win_scenario():
    if game['current_word'] == answer.chosen_word:
        print('You have won the game')

#GAME OBJECT -------------------------------------
game = {
    'current_word': ' _ ' * len(answer.chosen_word),
    'guessed_letters': [],
    'guesses_left': 8
    #'decrement_round': decrement_round
}



#decrement_round()
game_flow_logic()