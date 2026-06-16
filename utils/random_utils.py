import random
import string


def generate_assignment_code():
    characters = string.ascii_uppercase + string.digits

    random_code = ""

    for i in range(4):
        random_character = random.choice(characters)
        random_code += random_character

    assignment_code = "PY-" + random_code

    return assignment_code