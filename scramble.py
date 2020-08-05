


import random

def choose():
    words = ["aft", "ahoy", "below", "bow", "bridge", "billet", "brig", "colors", "forward", "helm", "know",
             "overboard", "scuttlebutt"]


    pick  = random.choice(words)# randomly choose from list.

    return pick


def scramble(word):

    random_word = random.sample(word, len(word))


    scramble = ''.join(random_word)
    return scramble



print('Welcome to the word scrambler game, NAVY edition. \n')
print('You will see a scrambled word, and you will have to guess. \n')
print('Whoever scores the most wins!')


def thank(p1n, p2n, p1, p2):
    print(p1n, 'Your score is :', p1)
    print(p2n, 'Your score is :', p2)

    # check_win() function calling
    check_win(p1n, p2n, p1, p2)

    print('Thanks for playing...')


# Function for declaring winner
def check_win(player1, player2, p1score, p2score):
    if p1score > p2score:
        print("winner is :", player1)
    elif p2score > p1score:
        print("winner is :", player2)
    else:
        print("Draw..Well Played guys..")

    # Function for playing the game.


def play():
    # enter player1 and player2 name
    p1name = input("player 1, Please enter your name :")
    p2name = input("Player 2 , Please enter your name: ")

    # variable for counting score.
    pp1 = 0
    pp2 = 0


    turn = 0


    while True:


        picked_word = choose()


        qn = scramble(picked_word)
        print("scrambled word is :", qn)


        if turn % 2 == 0:


            print(p1name, 'Your Turn.')

            ans = input("what is your guess? ")


            if ans == picked_word:


                pp1 += 1

                print('Your score is :', pp1)
                turn += 1

            else:
                print("Better luck next time ..")


                print(p2name, 'Your turn.')

                ans = input('what is in your mind? ')

                if ans == picked_word:
                    pp2 += 1
                    print("Your Score is :", pp2)

                else:
                    print("Better luck next time...correct word is :", picked_word)

                c = int(input("press 1 to continue and 0 to quit :"))


                if c == 0:
                    # thank() function calling
                    thank(p1name, p2name, pp1, pp2)
                    break

        else:


            print(p2name, 'Your turn.')
            ans = input('what is in your mind? ')

            if ans == picked_word:
                pp2 += 1
                print("Your Score is :", pp2)
                turn += 1

            else:
                print("Better luck next time.. :")
                print(p1name, 'Your turn.')
                ans = input('what is in your mind? ')

                if ans == picked_word:
                    pp1 += 1
                    print("Your Score is :", pp1)

                else:
                    print("Better luck next time...correct word is :", picked_word)

                    c = int(input("press 1 to continue and 0 to quit :"))

                    if c == 0:
                        # thank() function calling
                        thank(p1name, p2name, pp1, pp2)
                        break

            c = int(input("press 1 to continue and 0 to quit :"))
            if c == 0:
                # thank() function calling
                thank(p1name, p2name, pp1, pp2)
                break



if __name__ == '__main__':

    play()