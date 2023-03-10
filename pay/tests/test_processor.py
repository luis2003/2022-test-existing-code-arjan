import pytest
import os

from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor, luhn_checksum
from datetime import date
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY") or ""

@pytest.fixture
def card() -> CreditCard:
    year_in_future = date.today().year + 2
    return CreditCard("1249190007575069", 12, year_in_future)


@pytest.fixture
def invalid_number_and_date_card() -> CreditCard:
    year_in_past = date.today().year - 100
    return CreditCard("1249190007575068", 12, year_in_past)


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
    assert not luhn_checksum("1249190007575068")


def test_luhn_checksum_valid_card() -> None:
    assert luhn_checksum("1249190007575069")


def test_charge_invalid_card_number(invalid_number_and_date_card) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(invalid_number_and_date_card, 100)
