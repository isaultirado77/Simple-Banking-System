from account import Account, AccountRepository
from exceptions import AccountRepositoryError, MenuError


class BankManager:
    def __init__(self):
        self.repository = AccountRepository()

    def create_account(self) -> None:
        try:
            account = Account.generate_account()
            self.repository.add_account(account)
            text = (
                "Your card has been created\n"
                f"Your card number: {account.card.id}\n"
                f"Your card PIN: {account.card.pin}"
            )
            print(text)
        except AccountRepositoryError as are:
            print(f'Error: {are.message}')

    def log_into_account(self) -> None:
        try:
            id = input('Enter your card number:')
            pin = input('Enter your PIN:')
            account = self.repository.get_account_by_id(id, pin)
            self.logged(account)
        except ValueError:
            print("Error: Enter a valid number.")
        except AccountRepositoryError as ace:
            print(f"Error: {ace.message}")

    @classmethod
    def logged(cls, account: Account) -> None:
        print('\nYou have successfully logged in!\n')
        menu_text = '1. Balance\n2. Log Out\n0. Exit'

        while True:
            try:
                option = int(input(menu_text))

                if option == 0:
                    break
                elif option == 1:
                    account.display_balance()
                elif option == 2:
                    break
                else:
                    raise MenuError("Option must be 0, 1 or 2.")

            except ValueError:
                print("\nError: Enter a valid number.\n")
            except MenuError as me:
                print(f'Error: {me.message}')


def read_main_menu_option() -> int:
    menu_text = '1. Create an account\n2. Log into account\n0. Exit'
    while True:
        try:
            option = int(input(menu_text))
            if option in (0, 1, 2):
                return option
            else:
                raise MenuError("Option must be 0, 1 or 2.")
        except ValueError:
            print("\nError: Enter a valid number.\n")
        except MenuError as me:
            print(f'Error: {me.message}')


def main() -> None:
    pass


if __name__ == '__main__':
    main()
    pass
