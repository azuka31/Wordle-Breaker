from english_words import english_words_set
import re

words = list(i.lower() for i in english_words_set)

def input_information(arr, text):
    print('{} :'.format(text))
    answer = input().split()
    for char in answer:
        arr.append(char)
    print(arr)

def reduce(arr, chars):
    def exclude_false(word):
        if char not in word:
            return True
        else:
            return False
    for char in chars:
        arr = list(filter(exclude_false, arr))
    return arr

def recomend(arr, chars):
    def prioritize(word):
        if char in word:
            return True
        else:
            return False
    for char in chars:
        arr = list(filter(prioritize, arr))
    return arr

def recomend_by_position(arr, pattern):
    def is_match(word):
        if re.match(pattern, word):
            return True
        else:
            return False
    new = list(filter(is_match, arr))
    return new

def is_5character(word):
    if len(word) == 5:
        return True
    else:
        return False
    
class game:
    def __init__(self):
        game.reset(self)
    def main(self):
        exit = False
        while exit == False:
            print('\nChoose number to add \n1. False Character: {}\n2. True Character: {}\n3. Word Pattern: {}\n\nType reset to replay, or exit to stop'.format(self.false_character, self.true_character, self.pattern))
            command = input('Input command : ')
            if command == 'exit':
                exit = True
                break
            elif command == 'reset':
                game.reset(self)
            elif int(command) == 1:
                false_character = list(input('Input your false characters (just split by space) : ').split())
                for char in false_character:
                    self.false_character.append(char)
            elif int(command) == 2:
                true_character = list(input('Input your true characters (just split by space) : ').split())
                for char in true_character:
                    self.true_character.append(char)
            elif int(command) == 3:
                self.pattern = input('Input your pattern(type dot for unknown character) : ')
            else:
                print('The command is invalid')
            game.filter(self)
    def filter(self):
        tmp = reduce(words, self.false_character)
        tmp = recomend(tmp, self.true_character)
        tmp = recomend_by_position(tmp, self.pattern)
        result = list(filter(is_5character, tmp))
        if len(result) > 100:
            result = result[:100]
        print('\n\n\n\nRECOMENDED WORDS :\n{}'.format(result))
    def reset(self):
        self.false_character = []
        self.true_character = []
        self.pattern = '.....'

# play the game
a = game()
a.main()
