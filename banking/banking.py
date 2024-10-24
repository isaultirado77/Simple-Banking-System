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


def generate_pin() -> str:
    return ''.join(str(randint(0, 9)) for _ in range(4))


def create_card():
    pass


class Card:
    def __init__(self, id: str, pin: str):
        self.id = id
        self.pin = pin


def log_into_account():
    pass


def main() -> None:
    pin = generate_pin()
    print(pin)
    pass


if __name__ == '__main__':
    main()
    pass
