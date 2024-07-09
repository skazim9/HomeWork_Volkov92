from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_info: str) -> str | None:
    """Функция маскирующая номер карты или счета."""
    if "Счет" in user_info:
        return f'Счет {get_mask_account(user_info)}'
    else:
        return get_mask_card_number(user_info)


def get_data(data_info: str) -> str:
    """Функция преобразования даты"""
    return f"{data_info[8:10]}.{data_info[5:7]}.{data_info[:4]}"
