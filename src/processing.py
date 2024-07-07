from typing import Any


def filter_by_state(list_of_dict: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    '''
    Функция принимает список словарей и возвращает новый список словарей,
    у которых ключ state соответствует указанному значению.
    '''
    return [new_dict for new_dict in list_of_dict if new_dict.get("state") == state]


def sort_by_date(list_of_dict: list[dict[str, Any]], is_reverse: bool = True) -> list[dict[str, Any]]:
    """
    Функция принимает на вход список словарей и возращает новый отсортированный,
    по убыванию даты.
    """
    sorted_list = sorted(list_of_dict, key=lambda new_list_of_dict: new_list_of_dict["date"], reverse=is_reverse)
    return sorted_list
