import random

#instantiate word in game class

class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.chosen_word_info = []
        for letter in chosen_word:
            #create dictionary to hold letters of chosen word and a status to indicate whether word has been guessed
            chosen_word_dictionary = {}
            chosen_word_dictionary['letter'] = letter
            chosen_word_dictionary['guessed'] = False
            self.chosen_word_info.append(chosen_word_dictionary)

    def get_chosen_word(self):
        return self.chosen_word_info



class Game():
    #initialize game
    def __init__(self):
        self.rounds = 8
        self.word_bank = ['pizza', 'python', 'sleep', 'class']
        self.word = ''
        self.word_info = []
        self.guess = ''
        self.guessed_letters = set()
        self.guessed_letter_count = 0
    #get word to be guessed
    def get_random_word(self):
        #instatiate Word class with random word from with word_bank
        get_word = Word(random.choice(self.word_bank).upper())
        #store word_info dictionary to use to evaluate guesses
        self.word_info = get_word.chosen_word_info
        
        #print('WORD INFO DICTIONARY: ',get_word.chosen_word_info)
        
        #store the string
        self.word = get_word.chosen_word
        
        #print('THE WORD IS...',self.word)
        
        #start game
        self.game_flow_logic()
        #return self.word.chosen_word
    
    #game flow:
    #prompt user to guess letter
    #evaluate if guessed letter is part of word
    #send correct/wrong guess message
    #evaluate if winning criteria is met
    #decrement round by 1
    def game_flow_logic(self):
        self.word_at_start_of_round()
        self.guess = input(' Please guess a letter ').upper()
        print(self.guess)
        self.rounds -= 1
        print('ROUNDS REMAINING',self.rounds)
        self.print_word()

    #show word at beginning of round
    #populate any letters that have already been guessed
    def word_at_start_of_round(self):
        for item in self.word_info:
            if item['guessed'] == True:
                print(item['letter'], end='')
            else:
                print(' _ ',end='')

        print(' GUESSED LETTERS: ', self.guessed_letters)

    #print updated word after guess has been evaluated
    def print_word(self):
        for item in self.word_info:
            #print(item)
            if self.guess == item['letter']:
                print(item['letter'], end='')
                item['guessed'] = True
                self.guessed_letter_count += 1
                
            elif item['guessed'] == True:
                print(item['letter'], end='')
            else:
                self.guessed_letters.add(self.guess)
                print(' _ ',end='')
        print(' # OF GUESSED LETTERS:', self.guessed_letter_count)
        #evaluate win scenario
        self.win_scenario()

    #win game logic: # of guessed letters equals length of word being guessed
    def win_scenario(self):
        if self.guessed_letter_count == len(self.word):
            print('Congrats! You won the game')
        elif self.rounds > 0:
            self.game_flow_logic()
        else:
            print('You lost the game. The word was', self.word)


#instantiate game object    
game = Game()
#get random word to start game
game.get_random_word()