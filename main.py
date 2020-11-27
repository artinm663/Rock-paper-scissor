import random
from config import GAME_CHOICES, RULES


def scores(c_user, c_system):
    """
    show information about final result
    :param c_user:
    :param c_system:
    :return:
    """

    print(f'user score : {c_user}, system score : {c_system}')

    if c_user > c_system:

        print('user won')
    else:
        print('system won')


def get_user_choice():
    """
    get and check user choice
    :return:
    """
    user_choice = input('choose p,r or s : ')

    if user_choice not in GAME_CHOICES:

        print("please enter correct choice : ")
        return get_user_choice()

    return user_choice


def get_system_choice():
    """
    get system choice
    :return:
    """
    system_choice = random.choice(GAME_CHOICES)

    return system_choice


def find_winner(user, system):
    """
    determine who is winner
    :param user:
    :param system:
    :return:
    """
    match = {user, system}

    if len(match) == 1:
        return 'draw'

    return RULES[tuple(sorted(match))]


def play_ground():
    """
    return all function in game here
    :return:
    """

    count_user = 0
    count_sys = 0

    while count_user < 3 and count_sys < 3:

        user = get_user_choice()
        system = get_system_choice()
        winner = find_winner(user, system)

        if winner == system:

            count_sys += 1

        elif winner == user:

            count_user += 1

        print(f'user choice : {user}, system choice : {system}, result : {winner}')

    scores(count_user, count_sys)

    play_again = input('if you want play again enter y : ')

    if play_again == 'y':

        play_ground()


if __name__ == '__main__':

    play_ground()
