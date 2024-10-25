class MenuError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AccountRepositoryError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
