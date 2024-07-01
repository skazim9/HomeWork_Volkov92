def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирующая номер карты."""
    if sum(1 for i in card_number if i.isdigit()) == 16:
        return f"{card_number[:-12]} {card_number[-11:-9]}** **** {card_number[-4:]}"
    else:
        return None


def get_mask_account(bank_number: str) -> str | None:
    """Функция максирующая номер счета банка."""
    if "Счет" in bank_number:
        return f"Счет {'*' * 2}{bank_number[-4::]}"
    else:
        return None
