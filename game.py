import random

def display_rules():
    print("Welcome to Rock-Paper-Scissors-Rat-Spock!")
    print("Rules:")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Rat")
    print("Rat poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Rat")
    print("Rat eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("You and the computer will each choose one of the options above.")
    print("The winner is determined based on the rules above.")
    print("Have fun!\n")


def game():
    # Expand rules matrix.
    # 0: ties, 1: user wins, -1: user loses.
    rules = [[0, -1, 1, 1, -1],  # rock
             [1, 0, -1, -1, 1],  # paper
             [-1, 1, 0, 1, -1],  # scissors
             [-1, 1, -1, 0, 1],  # rat
             [1, -1, 1, -1, 0]]  # spock

    options = ['rock', 'paper', 'scissors', 'rat', 'spock']
    Won = 0
    Lost = 0
    Tie = 0

    play_again = 'yes'

    while play_again.lower() == 'yes':
        if input("Would you like to see the rules of the game? (yes/no): ").lower() == 'yes':
            display_rules()

        CPU = random.choice(options)
        User = input('Choose an option (rock, paper, scissors, rat, spock): ')

        User_idx = options.index(User)
        CPU_idx = options.index(CPU)

        print('\nUser vs CPU')
        print(f'{User} vs {CPU}\n')

        result = rules[User_idx][CPU_idx]

        if result == 0:
            print('Tie!')
            Tie += 1
        elif result == 1:
            print('Won!')
            Won += 1
        elif result == -1:
            print('Lost!')
            Lost += 1

        print(f'\nStats:\nWon: {Won}\nLost: {Lost}\nTie: {Tie}\n')

        play_again = input('Do you want to play again? (yes/no): ')

    print('Thank you for playing. Until next time!')


game()
