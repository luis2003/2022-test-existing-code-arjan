import pytest

from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"  # should not be commited to prod code


@pytest.fixture
def card() -> CreditCard:
    return CreditCard("1249190007575069", 12, 2024)


@pytest.fixture
def invalid_number_and_date_card() -> CreditCard:
    return CreditCard("1249190007575068", 12, 1900)


def test_invalid_api_key(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge(card, 100)


def test_charge_valid_date_card(card: CreditCard) -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge(card, 100)


def test_charge_invalid_date_card(invalid_number_and_date_card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(invalid_number_and_date_card, 100)


def test_luhn_checksum_invalid_card() -> None:
    processor = PaymentProcessor(API_KEY)
    assert not processor.luhn_checksum("1249190007575068")


def test_luhn_checksum_valid_card() -> None:
    processor = PaymentProcessor(API_KEY)
    assert processor.luhn_checksum("1249190007575069")


def test_charge_invalid_card_number(invalid_number_and_date_card) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(invalid_number_and_date_card, 100)
