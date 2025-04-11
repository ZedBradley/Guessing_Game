import random
print(r' _    _  ____  __    ___  _____  __  __  ____      ____  _____       ___  __  __  ____  ___  ___      _    _  _   _  _____      ___    __    ____  ____       ____  ____ ')
print(r'( \/\/ )( ___)(  )  / __)(  _  )(  \/  )( ___)    (_  _)(  _  )     / __)(  )(  )( ___)/ __)/ __)    ( \/\/ )( )_( )(  _  )    / __)  /__\  (_  _)(  _ \     (_  _)(_  _)')
print(r' )    (  )__)  )(__( (__  )(_)(  )    (  )__)       )(   )(_)(     ( (_-. )(__)(  )__) \__ \\__ \     )    (  ) _ (  )(_)(     \__ \ /(__)\  _)(_  )(_) )     _)(_   )(  ')
print(r'(__/\__)(____)(____)\___)(_____)(_/\/\_)(____)     (__) (_____)     \___/(______)(____)(___/(___/    (__/\__)(_) (_)(_____)    (___/(__)(__)(____)(____/     (____) (__) ')

e_history = ["I came, I saw, I conquered",
            "Those who cannot remember the past are condemned to repeat it"]

eha = ['Julius Caesar',
    'George Santayana ']


m_history = ['History is a set of lies agreed upon']

mha = ['Napoleon Bonaparte']


h_history = ['Our greatest glory is not in never falling, but in rising every time we fall',
            'Following the light of the sun, we left the Old World']

hha = ['Confucius',
    'Christopher Columbus']

e_fiction = ["I am your father",
        "Winter is coming"]

efa = ['Darth Vader',
        'Every Stark ever']


m_fict = ['a']


h_fict = ['a']


def number_generator(a,b):
    return random.randint(a,b)

print = 'You will be guessing if the quote is from history or from fiction! Are you ready?'

difficulty = input('easy, medium, hard, or exit: ')
while True:
    if difficulty == 'easy':
        num = number_generator(0,1)
        if number_generator(1,10) % 2 == 0:
            print(e_history[num])
            answer = input('Enter your answer (history or fiction): ')
            if answer == 'history' or answer == 'History':
                print(f'You did it! That one was by {eha[num]}')
        else:
            print(e_fiction[num])
            answer = input('Enter your answer (history or fiction): ')
            if answer == 'fiction' or answer == 'Fiction':
                print(f'You did it! That one was by {efa[num]}')

        
    # if difficulty == 'medium':
        
    # if difficulty == 'hard':

    if difficulty == 'exit':
        print('Thanks for playing')
        break
        
    else:
        print("check your spelling")                                                                                                                                                                                                  
