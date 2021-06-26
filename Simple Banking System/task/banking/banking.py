import random


def start_program():
    print("1. Create an account")
    print("2. Log into account")
    print("3. Exit")


class CreditCard:

    def __init__(self):
        self.card_no = [4, 0, 0, 0, 0, 0] + random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
        luhn_card = self.card_no.copy()
        self.pin = ''
        for index, value in enumerate(luhn_card):
            if index % 2 == 0:
                luhn_card[index] = value * 2
        for index, value in enumerate(luhn_card):
            if value > 9:
                luhn_card[index] = value - 9
        luhn_digit = 0
        if sum(luhn_card) % 10 != 0:
            luhn_digit = 10 - sum(luhn_card) % 10
        self.card_no.append(luhn_digit)
        self.card_no = ''.join([str(elem) for elem in self.card_no])


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
            else:
                print('Wrong card number or PIN!')
    if customer_selection == 0:
        break
