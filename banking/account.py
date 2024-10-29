import sqlite3

from card import Card
from database import connect, create_table, add_card, get_card_by_number
from typing import Optional


class Account:
    def __init__(self, card: Card, balance: int = 0):
        self.card = card
        self.balance = balance

    def get_card(self) -> 'Card':
        return self.card

    def get_card_number(self) -> str:
        return self.card.number

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
        self.connection = connect()

    def add_account(self, account: Account) -> None:
        try:
            add_card(self.connection, account.get_card_number(), account.get_pin(), account.get_balance())

        except sqlite3.IntegrityError:
            raise AccountRepositoryError("Account with this card ID already exists.")

    def get_account_by_id(self, id: str, pin: str) -> 'Account':
        pass

    def remove_account(self, id: str) -> None:
        pass
