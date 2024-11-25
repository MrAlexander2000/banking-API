import random

def unique_id():
    return str("".join([random.randint(0,9) for i in range(10)]))