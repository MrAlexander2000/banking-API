import random

def unique_id():
    return str("".join([random.randint(0,9) for i in range(10)]))

def validate_keys(data:dict , list_of_keys:list) -> bool:
    """_summary_

    Args:
        data (dict): _description_
        list_of_keys (list): _description_

    Returns:
        bool: _description_
    """
    for key in data:
        if key not in list_of_keys:
            return False
    return True