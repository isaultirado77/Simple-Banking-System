import sqlite3

CREATE_CARD_TABLE = "CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);"

INSERT_CARD = "INSERT INTO card (id, number, pin, balance) VALUES (?, ?, ?, ?); "

GET_ALL_CARDS = "SELECT * FROM card; "

GET_CARD_BY_NUMBER = "SELECT * FROM card WHERE number = ?; "


def connect():
    return sqlite3.connect('card.s3db')


def create_table(connection):
    with connection:
        connection.execute(CREATE_CARD_TABLE)


def add_card(connection, number, pin, balance=0):
    with connection:
        connection.execute(INSERT_CARD, (number, pin, balance))


def get_all_cards(connection):
    with connection:
        return connection.execute(GET_ALL_CARDS).fetchall()


def get_card_by_number(connection, number):
    with connection:
        return connection.execute(GET_CARD_BY_NUMBER, (number,)).fetchall()
