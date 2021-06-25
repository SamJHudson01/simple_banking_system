import random


def start_program():
    print("1. Create an account")
    print("2. Log into account")
    print("3. Exit")


class CreditCard:

    def __init__(self) -> object:
        self.card_no = '400000'
        self.pin = ''
        for _ in range(9):
            digit = random.randint(0, 9)
            self.card_no += str(digit)
        self.card_no += str(random.randint(0, 9))
        for _ in range(4):
            pin_digit = random.randint(0, 9)
            self.pin += str(pin_digit)
        print('Your card has been created')
        print('Your card number:')
        print(self.card_no)
        print('Your card PIN:')
        print(self.pin)


all_cards = []
while True:
    start_program()
    customer_selection = int(input())
    if customer_selection == 1:
        new_card = CreditCard()
        all_cards.append(new_card)
    if customer_selection == 2:
        print('Enter your card number:')
        cust_no = input()
        print('Enter your PIN:')
        cust_pin = input()
        for card in all_cards:
            if cust_no == card.card_no and cust_pin == card.pin:
                print('You have successfully logged in!')
                print('')
                print('1. Balance')
                print('2. Log out')
                print('0. Exit')
                cust_selection = int(input())
                if cust_selection == 1:
                    print('Balance: 0')
                elif cust_selection == 2:
                    print('You have successfully logged out!')
                    break
                else:
                    print('Bye!')
                    customer_selection = 0
                    break
                # need an if statement here for checking balance, logging out and exiting the program
            else:
                print('Wrong card number or PIN!')
    if customer_selection == 0:
        break
