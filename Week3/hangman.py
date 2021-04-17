import random
import os

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'muskmelon', 'elonmusk', 'rick', 'morty']

def printHangman(tries):
    if tries == 1:
            print(""" 
      * *
    *     *
    *     *
     *****  
             """)
    elif tries == 2:
        print(""" 
      * *
    *     *
    *     *
     *****
       |
       |
       |

             """)
    elif tries == 3:
        print(""" 
      * *
    *     *
    *     *
     *****
      /|
     / |
       |

             """)
    elif tries == 4:
        print(r""" 
      * *
    *     *
    *     *
     *****
      /|\
     / | \   
       |  
             """)
    elif tries == 5:
        print(r""" 
      * *
    *     *
    *     *
     *****
      /|\
     / | \   
       |  
      /   
     /       
     """)
    elif tries == 6:
        print(r""" 
      * *
    *     *
    *     *
     *****
      /|\
     / | \   
       |  
      / \  
     /   \    
     """)
    else:
        print("")    
         


def gameScreen(tries):
    print("----------------")
    print("       |        ")
    print("       |        ")
    printHangman(tries)

def start():
    tries = 0
    question = random.choice(words) 
    hiddenQuestion = {}
    answer = {}
    ans = ''
    for i in range(len(question)):
        hiddenQuestion[i] = '_ '
        answer[i] = f'{question[i]} '    
    for i in answer:
        ans+=answer[i]

    while tries < 6:
        win = 0
        flag = 0  
        os.system('cls' if os.name == 'nt' else 'clear')
        gameScreen(tries)
        print('\n\nGuess the word : ', end=' ')
        for i in range(len(question)):
            print(hiddenQuestion[i], end='')
        print(f'({len(question)})')    
        letter = input("\nEnter one letter or the whole word : ")
        if len(letter) == len(question):
            if letter.lower() == question:
                win = 1
                print("\nGG BRO U GOT IT")
                break
            else: tries+=1
        elif len(letter) == 1:
            for i in range(len(question)):
                if question[i] == letter.lower():
                    hiddenQuestion[i] = f'{letter} '
                    flag+=1
                    hq = ''
                    for j in hiddenQuestion:
                        hq += hiddenQuestion[j]
                    if hq == ans:        
                        print("Well done you guessed it correctly")
                        tries = 100
                        win = 1
                        break
            if(flag == 0):
                tries+=1
    
    if not win:
        printHangman(6)
        print("Try again and beat it this time")
    print(f'The word was {ans}')
start()