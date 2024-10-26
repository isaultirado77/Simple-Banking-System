from card import Card


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

    def display_balance(self) -> None:
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
