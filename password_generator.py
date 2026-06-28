import random
import string


class WeakPasswordError(Exception):
    pass


def generate_password(length=12):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password


def validate_password(password):

    if len(password) < 8:
        raise WeakPasswordError(
            "Password must be at least 8 characters"
        )

    if not any(c.isupper() for c in password):
        raise WeakPasswordError(
            "Password needs uppercase letter"
        )

    if not any(c.islower() for c in password):
        raise WeakPasswordError(
            "Password needs lowercase letter"
        )

    if not any(c.isdigit() for c in password):
        raise WeakPasswordError(
            "Password needs digit"
        )

    print("Strong Password")


generated = generate_password()
print("Generated Password:", generated)

user_password = input(
    "Enter password to validate: "
)

try:
    validate_password(user_password)

except WeakPasswordError as e:
    print("Error:", e)
