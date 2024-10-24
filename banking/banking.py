from random import randint


class MenuError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def read_main_menu_option() -> int:
    while True:
        try:
            menu_text = '1. Create an account\n2. Log into account\n0. Exit'
            option = int(input(menu_text))
            if option in (0, 1, 2):
                return option
            else:
                raise MenuError("Option must be 0, 1 or 2. ")
        except ValueError:
            print("\nError: Enter a valid number.\n")
        except MenuError as me:
            print(f'Error: {me.message}')


def generate_random_int_sequence(n: int = 5) -> str:
    return ''.join(str(randint(0, 9)) for _ in range(n))


def generate_card_id() -> str:
    return '400000' + generate_random_int_sequence(10)


def generate_pin() -> str:
    return generate_random_int_sequence(4)


class Card:
    def __init__(self, id: str, pin: str):
        self.id = id
        self.pin = pin

    @staticmethod
    def generate_card() -> 'Card':
        id = generate_card_id()
        pin = generate_pin()
        card = Card(id, pin)
        return card

    def __str__(self):
        return f'id: {self.id}\npin: {self.pin}\n'


class Account:
    def __init__(self, card: Card, balance: int = 0):
        self.card = card
        self.balance = balance

    def get_id(self) -> str:
        return self.card.id

    def get_pin(self) -> str:
        return self.card.pin

    def get_balance(self) -> int:
        return self.balance

    @staticmethod
    def generate_account() -> 'Account':
        card = Card.generate_card()
        return Account(card)

    def display_balance(self):
        print(f'\nBalance: {self.balance}\n')

    def __str__(self):
        return self.card.__str__() + f'Balance: {self.balance}'


class AccountRepositoryError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AccountRepository:
    def __init__(self):
        self.repository = {}

    def add_account(self, account: Account) -> None:
        if account.card.id in self.repository:
            raise AccountRepositoryError("Account with this card ID already exists.")
        self.repository[account.card.id] = account

    def get_account_by_id(self, id: str, pin: str) -> 'Account':
        if id in self.repository:
            if self.repository[id].get_pin() == pin:
                return self.repository[id]
        raise AccountRepositoryError("Wrong card number or PIN!")

    def remove_account(self, id: str) -> None:
        if id in self.repository:
            del self.repository[id]
        else:
            raise AccountRepositoryError("Account not found.")


def create_account() -> 'Account':
    account = Account.generate_account()
    text = (
        "Your card has been created\n"
        f"Your card number: {account.card.id}\n"
        f"Your card PIN: {account.card.pin}"
    )
    print(text)
    return account


def log_into_account() -> None:
    try:
        id = int(input('Enter your card number:'))
        pin = int(input('Enter your PIN:'))
    except ValueError:
        print("Error: Enter a valid number. ")
    except AccountRepositoryError as ace:
        print(f"Error: {ace.message}")


main_menu_options = {
    1: create_account(),
    2: log_into_account()
}


def main() -> None:
    pass


if __name__ == '__main__':
    main()
    pass
