from typing import Any


def filter_by_state(list_of_dict: list[dict[str, any]], state: str = "EXECUTED") -> any:
    '''
    Функция принимает список словарей и возвращает новый список словарей,
    у которых ключ state соответствует указанному значению.
    '''
    return [new_dict for new_dict in list_of_dict if new_dict.get("state") == state]
