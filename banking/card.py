from random import randint


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
        return Card(id, pin)

    def display_generated_card(self) -> None:
        text = (
            "\nYour card has been created\n"
            f"Your card number:\n{self.id}\n"
            f"Your card PIN:\n{self.pin}\n"
        )
        print(text)

    def __str__(self):
        return f'Your card number:\n{self.id}\nYour card PIN:\n{self.pin}\n'
