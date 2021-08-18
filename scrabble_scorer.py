# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:
            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
    word = str(input("Let's play some Scrabble!\nPlease enter a word to score: "))
    return word 

def simple_scorer(word):
    word = word.upper()
    points = 0
    for char in word:
        points += 1
    return points            

def vowel_bonus_scorer(word):
    word = word.upper()
    points = 0
    for char in word:
        if char in ['A', 'E', 'I', 'O', 'U']:
            points += 3
        else: points += 1
    return points

def scrabble_scorer(word):
    score = 0
    
    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]
            
    return score

# scoring_algorithms = {
#     1: '1: Simple Score. \nDescription: Each letter is worth 1 point\n',
#     2: '2: Bonus Vowel. \nDescription: Vowels are 3 pts, consonants are 1pt.\n',
#     3: '3: Scrabble. \nDescription: The traditional scoring algorithm.\n'
# }

scoring_algorithms = (
    {
        'name': 'Simple Score',
        'description': 'Each letter is worth 1 point',
        'scoring_function': simple_scorer},
    {
        'name': 'Bonus Vowels',
        'description': 'Vowels are 3 pts, consonants are 1 pt',
        'scoring_function': vowel_bonus_scorer},
    {
        'name': 'Scrabble',
        'description': 'The traditional scoring algorithm',
        'scoring_function': scrabble_scorer}
)

def scorer_prompt():
    user_input = int(input('Which scoring alogrithm would you like to use?\n\n0 - Simple: One point per character\n1 - Vowel Bonus: Vowels are worth 3 points\n2 - Scrabble: Uses scrabble point system\nEnter 0, 1, or 2: '))
    scoring_algorithm_dict = scoring_algorithms[user_input]
    return scoring_algorithm_dict

def transform(provided_dict):
    new_dict = {}
    
    for (key, value) in provided_dict.items():
        #print(key, value)
        for letter in value:
            new_dict[letter.lower()] = key
    return(new_dict)

new_point_structure = transform(OLD_POINT_STRUCTURE)

def run_program():
    word = initial_prompt()    
    scoring_algorithm_dict = scorer_prompt()    
    score = scoring_algorithm_dict['scoring_function'](word)
        
    print(score)

