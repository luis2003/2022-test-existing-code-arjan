from datetime import datetime


class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _check_api_key(self) -> bool:
        return self.api_key == '6cfb67f3-6281-4031-b893-ea85db0dce20'

    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        pass

    def validate_card(self, card: str, month: int, year: int) -> bool:
        pass

    def luhn_checksum(self, card_number: str) -> bool:
        def digits_of(card_nr: str):
            return [int(d) for d in card_nr]

        pass


