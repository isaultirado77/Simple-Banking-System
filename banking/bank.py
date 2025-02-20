from enum import Enum

from account import Account, AccountRepository, AccountRepositoryError
from card import is_valid_luhn_number


class MenuError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def read_menu_options(text: str = None, options: tuple = None) -> int:
    while True:
        try:
            option = int(input(text))
            if option in options:
                return option
            else:
                raise MenuError(f"Option must be in {options}")
        except ValueError:
            print("\nError: Enter a valid number.\n")
        except MenuError as me:
            print(f'Error: {me.message}')


class BankState(Enum):
    MAIN_MENU = 'main_menu'
    ACCOUNT_LOGGED_IN = 'account_logged_in'
    EXIT = 'exit'


class BankManager:
    def __init__(self):
        self.repository = AccountRepository()
        self.bank_state = BankState.MAIN_MENU

    def run(self) -> None:
        menu_text = '1. Create an account\n2. Log into account\n0. Exit\n'
        while self.bank_state != BankState.EXIT:
            option = read_menu_options(menu_text, (0, 1, 2))

            if option == 1:
                self.create_account()
            elif option == 2:
                self.log_into_account()
            elif option == 0:
                self.exit_application()

    def create_account(self) -> None:
        try:
            account = Account.generate_account()
            self.repository.add_account(account)
            account.get_card().display_generated_card()

        except AccountRepositoryError as are:
            print(f'Error: {are.message}')

    def log_into_account(self) -> None:
        try:
            card_number = input('\nEnter your card number: ')
            pin = input('Enter your PIN: ')
            account = self.repository.get_account_by_card_number(card_number, pin)
            self.bank_state = BankState.ACCOUNT_LOGGED_IN
            self.logged(account)
        except ValueError:
            print("Error: Enter a valid number.")
        except AccountRepositoryError as ace:
            print(f"\nError: {ace.message}\n")

    def logged(self, account: Account) -> None:
        print('\nYou have successfully logged in!')
        menu_text = '\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log Out\n0. Exit\n'

        while self.bank_state == BankState.ACCOUNT_LOGGED_IN:
            option = read_menu_options(menu_text, (0, 1, 2, 3, 4, 5))

            if option == 0:
                self.exit_application()
            elif option == 1:
                account.display_balance()
            elif option == 2:
                self.add_income(account)
            elif option == 3:
                self.do_transfer(account)
            elif option == 4:
                self.close_account(account)
            elif option == 5:
                print('\nYou have successfully logged out!\n')
                self.bank_state = BankState.MAIN_MENU

    def exit_application(self) -> None:
        print('Bye!')
        self.bank_state = BankState.EXIT

    def add_income(self, account: 'Account') -> None:
        try:
            income = int(input('\nEnter income: \n'))
            self.repository.add_income_to_card(account.get_card_number(), income)
            print("Income was added!")
        except ValueError:
            print("\nError: Enter a valid income.\n")

    def do_transfer(self, account: 'Account') -> None:
        print('\nTransfer')
        while True:
            receiver_number = input('Enter card number: \n')


            if receiver_number == account.get_card_number():
                print('You can\'t transfer money to the same account!\n')
                return
            elif not is_valid_luhn_number(receiver_number):
                print('\nProbably you made a mistake in the card number. Please try again!\n')
                break
            elif not self.repository.card_exists(receiver_number):
                print('Such a card does not exist.')
                return
            else:
                transfer = int(input('Enter how much money you want to transfer:\n'))
                updated_account = self.repository.get_account_by_card_number(account.get_card_number(), account.get_pin())
                if transfer > updated_account.get_balance():
                    print('\nNot enough money!')
                    return
                self.repository.add_income_to_card(receiver_number, transfer)
                self.repository.withdraw_from_card(account.get_card_number(), transfer)
                print('Success!')
                return

    def close_account(self, account: 'Account') -> None:
        self.repository.remove_account(account.get_card_number())
