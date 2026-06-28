import re


class Account:

    def __init__(
        self,
        account_no,
        balance
    ):
        self.account_no = account_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        pass


class SavingsAccount(Account):

    def withdraw(self, amount):

        if amount <= self.get_balance():

            new_balance = (
                self.get_balance() - amount
            )

            print(
                f"Withdraw Successful\nRemaining Balance: {new_balance}"
            )

        else:
            print(
                "Insufficient Balance"
            )


class CurrentAccount(Account):

    def withdraw(self, amount):

        if amount <= (
            self.get_balance() + 5000
        ):
            print(
                "Withdraw Successful"
            )

        else:
            print(
                "Overdraft Limit Exceeded"
            )


account_number = input(
    "Enter Account Number: "
)

pattern = r"^\d{10}$"

if re.match(pattern, account_number):

    account = SavingsAccount(
        account_number,
        10000
    )

    account.withdraw(3000)

else:
    print(
        "Invalid Account Number"
    )
