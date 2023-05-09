import random


def play():
    user = int(input('Try to figure out the number chosen by computer: '))
    computer = random.choice(range(6))
    print('Computer choose:', computer)

    if user == computer:
        return 'You won!'

    return 'You lost!'


play()
