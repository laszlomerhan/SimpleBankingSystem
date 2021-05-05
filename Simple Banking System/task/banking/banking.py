import random


def main():

    card_num = random.randint(0000000000, 9999999999)
    pin = random.randint(0000, 9999)
    card_id = '400000' + str(card_num)
    balance = 0

    choice = int(input('''
1. Create an account
2. Log into account
0. Exit\n'''))
    print(choice)
    if choice == 1:
        create()
    elif choice == 2:
        login()
    elif choice == 0:
        print('\nBye!')
        exit()


def create():

    print(f'''
Your card has been created
Your card number:
{card_id}
Your card PIN:
{pin}
''')
    main()


def login():

    a = input('Enter your card number: ')
    b = int(input('Enter your PIN: '))
    if a == card_id and b == pin:
        print('\nYou have successfully logged in!')
        login_menu()
    else:
        print('\nWrong card number or PIN!')


def login_menu():

    menu = int(input('''
1. Balance
2. Log out
0. Exit\n'''))

    if menu == 1:
        print(f'Balance: {balance}')
        login_menu()
    elif menu == 2:
        print('\nYou have successfully logged out!')
        login()
    elif menu == 0:
        print('\nBye!')
        exit()


main()
