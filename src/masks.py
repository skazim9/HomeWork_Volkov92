import logging

logger = logging.getLogger("mask")
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name) - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирующая номер карты."""
    if sum(1 for i in card_number if i.isdigit()) == 16:
        logger.info(f"Маска карты: {card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}")
        return f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    else:
        return None


def get_mask_account(bank_number: str) -> str:
    """Функция максирующая номер счета банка."""
    account_n = str(bank_number)
    logger.info(f"Маска аккаунта: **{account_n[-4:]}")
    return f"**{account_n[-4:]}"
