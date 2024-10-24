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


def create_an_account():
    pass


def generate_random_int_sequence(n: int = 5) -> str:
    return ''.join(str(randint(0, 9)) for _ in range(n))


def generate_card_id() -> str:
    return '400000' + generate_random_int_sequence(10)


def generate_pin() -> str:
    return generate_random_int_sequence(4)


def create_card():
    pass


class Card:
    def __init__(self, id: str, pin: str):
        self.id = id
        self.pin = pin


class Account:
    def __init__(self, card: Card):
        self.card = card


def log_into_account():
    pass


def main() -> None:
    print(generate_card_id())
    print(generate_pin())
    pass


if __name__ == '__main__':
    main()
    pass
