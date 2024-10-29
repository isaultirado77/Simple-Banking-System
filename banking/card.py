from random import randint


def generate_random_int_sequence(n: int = 5) -> str:
    return ''.join(str(randint(0, 9)) for _ in range(n))


def calculate_luhn_sum(uncompleted_id: str) -> int:
    total_sum = 0
    reversed_id = uncompleted_id[::-1]
    for index, digit in enumerate(reversed_id):
        digit = int(digit)
        if index % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit
    return total_sum


def get_control_number(uncompleted_number: str) -> int:
    total_sum = calculate_luhn_sum(uncompleted_number)
    return (10 - (total_sum % 10)) % 10


def generate_card_number() -> str:
    base_id = '400000' + generate_random_int_sequence(9)
    control_number = get_control_number(base_id)
    return base_id + str(control_number)


def generate_pin() -> str:
    return generate_random_int_sequence(4)


class Card:
    def __init__(self, number: str, pin: str):
        self.number = number
        self.pin = pin

    @staticmethod
    def generate_card() -> 'Card':
        number = generate_card_number()
        pin = generate_pin()
        return Card(number, pin)

    def display_generated_card(self) -> None:
        text = (
            "\nYour card has been created\n"
            f"Your card number:\n{self.number}\n"
            f"Your card PIN:\n{self.pin}\n"
        )
        print(text)

    def __str__(self):
        return f'Your card number:\n{self.number}\nYour card PIN:\n{self.pin}\n'
