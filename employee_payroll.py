from datetime import datetime


def log_salary(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        with open(
            "salary_log.txt",
            "a"
        ) as file:

            file.write(
                f"{datetime.now()} - Salary Calculated: {result}\n"
            )

        return result

    return wrapper


class Employee:

    def __init__(
        self,
        name
    ):
        self.name = name

    @log_salary
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(
        self,
        name,
        monthly_salary
    ):
        super().__init__(name)

        self.monthly_salary = (
            monthly_salary
        )

    @log_salary
    def calculate_salary(self):

        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(
        self,
        name,
        hours,
        rate
    ):
        super().__init__(name)

        self.hours = hours
        self.rate = rate

    @log_salary
    def calculate_salary(self):

        return (
            self.hours *
            self.rate
        )


emp1 = FullTimeEmployee(
    "Rahul",
    50000
)

emp2 = PartTimeEmployee(
    "Aman",
    40,
    500
)

print(
    emp1.name,
    emp1.calculate_salary()
)

print(
    emp2.name,
    emp2.calculate_salary()
)
