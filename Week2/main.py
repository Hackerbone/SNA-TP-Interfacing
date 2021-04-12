from random import randint
print('=================================================================')
print('Welcome to a text-based Snakes and Ladders ~ Made by S. Sitaraman')
print('=================================================================\n')
players = []
square = []
num_of_players = int(input("Enter Number of players : "))

for i in range(num_of_players):
    players.append(input(f'Enter your name Player {i+1} : '))
    square.append(0)

won = 0

ladders = {
    2: 23,
    8: 34,
    20: 77,
    32: 68,
    41: 79,
    74: 88,
    82: 100,
    85: 95
}

snakes = {
    29: 9,
    38: 15,
    47: 5,
    53: 33,
    62: 37,
    86: 54,
    92: 70,
    97: 25
}
def check_ladder(cursquare):
    temp = 0
    if cursquare in ladders:
        print(f'You got a ladder opening')
        print(r"""
               || __   ||
               ||=\_`\=||
               || (__/ ||
               ||  | | :-\"""-
               ||==| \/-=-   \
               ||  |(_|o o/   |_
               ||   \/ "  \   ,_)
               ||====\ U  /__/
               ||     ;--'  `-
               ||    /      .  \
               ||===;        \  \
               ||   |         | |
              _______\"""'   _/_/
             (~|_______ |  (_  \
               /  .' ( | )   \\_/
              |_ /     |||  |\\
             /  _)=====|||  | ||
            /  /|      ||/  / //
            \_/||      ( `-/ ||
               ||======/  /  \\ .-.
               ||      \_/    \'-'/
               ||      ||      `"`
               ||======||
               ||      ||
                
        """)

        print(f'Climbing up to {ladders[cursquare]}')
        cursquare = ladders[cursquare]
    return cursquare

def check_snake(cursquare):
    if cursquare in snakes:
        print(r"""
           /^\/^\
         _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                 /      /                    \
                /     /                       \\
              /      /                         \ \
             /     /                            \  \
           /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
              """)
        print(f'Oops, a snake bit you and you\'re going down with it at {snakes[cursquare]}')
        cursquare = snakes[cursquare]
    return cursquare

def ask_user(currplayer, cursquare):
    win = 0
    print('\n=================================================================')
    for key in range(num_of_players):
        print(f'{players[key]} is on square {square[key]}')

    print(f'\n{currplayer}\'s turn')
    roll = input('Type \'r\' to roll the dice , Type \'h\' to show all upcoming ladders and snakes : ')
    if roll == 'r':
        dice = randint(1, 6)
        print(f'{currplayer} rolled {dice}')
        if cursquare + dice > 100:
            print(f'Cannot move you need {100 - cursquare} to win')
        else:
            cursquare += dice
            cursquare = check_ladder(cursquare)
            cursquare = check_snake(cursquare)
            print(f'\n{currplayer} is on {cursquare}')
        if cursquare == 100:
            print(f'{currplayer} has won ! Now give yourself a pat on the back {cursquare}')
            win = 1
    elif roll == 'h':
        print('Ladders : ')
        for key in ladders:
            print(key, end=' ')


        print('\nSnakes : ')
        for key in snakes:
            print(key, end=' ')

        currplayer, cursquare, temp = ask_user(currplayer, cursquare)

    else:
        print(f'Enter valid input, don\'t mess it up again')
        currplayer, cursquare, temp = ask_user(currplayer,cursquare)

    return currplayer, cursquare, win


while won != 1:

    for key in range(num_of_players):
        players[int(key)], square[int(key)], won = ask_user(players[int(key)], square[int(key)])
        if(won == 1):
            print(r"""
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                """)
            break

print('\nHope you liked the game')