import random

#selected_word = ''
word_bank = ['pizza', 'python', 'sleep', 'class']

def get_random_word():
    return random.choice(word_bank)
    
#get_random_word()

class Word():
    def __init__(self, chosen_word=None):
        self.chosen_word = get_random_word()
        pass # this method will split the word up into a list of dictionaries with 2 attributes:
        pass # the letter/character, and a boolean representing whether or not it has been guessed
    
    def print_word(self):
        print('Hit print word', self.chosen_word)

    def check_letter(self):
        print('Hit check letter')

answer = Word()
#print(test.chosen_word)
answer.print_word()

game = {
    'current_word': ' _ ' * len(answer.chosen_word),
    'guessed_letters': [],
    'guesses_left': 8,
    
}

print(game['current_word'])