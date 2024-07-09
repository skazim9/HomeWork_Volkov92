def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирующая номер карты."""
    if sum(1 for i in card_number if i.isdigit()) == 16:
        return f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    else:
        return None


def get_mask_account(bank_number: str) -> str:
    """Функция максирующая номер счета банка."""
    account_n = str(bank_number)
    return f"**{account_n[-4:]}"
