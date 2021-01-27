import random

#instantiate word in game class

class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.chosen_word_info = []
        #list interpolation below
        #self.chosen_word_info = [{'letter': letter, 'guessed':False} for letter in chosen_word]

        #equivalent code to list interpolation
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
        #self.game_flow_logic()
        self.greeting()
        #return self.word.chosen_word
    
    #game flow:
    #prompt user to guess letter
    #evaluate if guessed letter is part of word
    #send correct/wrong guess message
    #evaluate if winning criteria is met
    #decrement round by 1
    def game_flow_logic(self):
        #if self.rounds == 8:
            #self.greeting()
        print('ROUNDS REMAINING',self.rounds)
        self.word_at_start_of_round()
        self.guess = input(' Please guess a letter ').upper()
        print(self.guess)
        #self.rounds -= 1
        self.print_word()

    #print greeting and ask if user is ready to play
    def greeting(self):
        print('Welcome to Hangman. Press y to play and n to exit ')
        start_game=input()
        if start_game == 'y':
            #self.word_at_start_of_round()
            self.game_flow_logic()
        else:
            print('bye!')

    #show word at beginning of round
    #populate any letters that have already been guessed
    def word_at_start_of_round(self):
        for item in self.word_info:
            if item['guessed'] == True:
                print(item['letter'], end='')
            else:
                print(' _ ',end='')

        print(' LETTERS GUESSED : ', self.guessed_letters)

    #print updated word after guess has been evaluated
    def print_word(self):
        self.quit_scenario()
        self.give_feedback()
        for item in self.word_info:
            #print(item)
            if self.guess == item['letter']:
                #print(f'Correct! {self.guess} is in the word',end='')
                print(item['letter'], end='')
                item['guessed'] = True
                self.guessed_letter_count += 1
                
            elif item['guessed'] == True:
                print(item['letter'], end='')
            else:
                self.guessed_letters.add(self.guess)
                #print(f'Too bad! {self.guess} is not in the word')
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

    #quit game logic: handle user quitting game
    def quit_scenario(self):
        #end gameflow logic
        if(self.guess == ';'):
            print('see you later!')
            #terminate program
            raise SystemExit

    #tell user if they have guessed correctly or incorrectly
    #subtract a round if incorrect letter is guessed
    def give_feedback(self):
        if(self.guess in self.word):
            print('Nice guess')
            
        else:
            print('Nope nope nope')
            self.rounds -= 1

#instantiate game object    
game = Game()
#get random word to start game
game.get_random_word()