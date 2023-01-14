import pytest
from pay.processor import PaymentProcessor

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"  # should not be commited to prod code


def test_invalid_api_key() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge("1249190007575069", 12, 2024, 100)


def test_charge_valid_date_card() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("1249190007575069", 12, 2024, 100)


def test_charge_invalid_date_card() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("1249190007575069", 12, 1900, 100)


def test_luhn_checksum_invalid_card() -> None:
    processor = PaymentProcessor(API_KEY)
    assert not processor.luhn_checksum("1249190007575068")


def test_luhn_checksum_valid_card() -> None:
    processor = PaymentProcessor(API_KEY)
    assert processor.luhn_checksum("1249190007575069")


def test_charge_invalid_card_number() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("1249190007575068", 12, 1900, 100)
