from random import randint


def generate_random_int_sequence(n: int = 5) -> str:
    return ''.join(str(randint(0, 9)) for _ in range(n))


def drop_last_digit(num: int) -> int:
    if num < 10:
        return num
    return num // 10


def multiply_by_two(num: int) -> int:
    if num % 2 == 0:
        return num * 2
    return num


def subtract_nine(num: int) -> int:
    if num > 9:
        return num - 9
    return num


def get_uncompleted_id_sum(uncompleted_id: str) -> int:
    summ = 0
    for digit in uncompleted_id:
        digit = int(digit)
        digit = drop_last_digit(digit)
        digit = multiply_by_two(digit)
        digit = subtract_nine(digit)
        summ += digit
    return summ


def get_control_number(uncompleted_id: str) -> int:
    summ = get_uncompleted_id_sum(uncompleted_id)
    if summ % 10 == 0:
        return 0
    last_digit = 0
    while True:
        if (summ + last_digit) % 10 == 0:
            break
        last_digit += 1
    return last_digit


def generate_card_id() -> str:
    card_id = '400000' + generate_random_int_sequence(9)
    control_number = get_control_number(card_id)
    return card_id + str(control_number)


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
