import pytest
from _pytest.monkeypatch import MonkeyPatch

from pay.order import Order, LineItem
from pay.payment import pay_order
from pay.processor import PaymentProcessor


def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    def charge_mock(self: PaymentProcessor, card: str, month: int, year: int, amount: int) -> None:
        pass

    inputs = ["1249190007575069", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
    monkeypatch.setattr(PaymentProcessor, "charge", charge_mock)
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order)


def test_pay_order_invalid_order_no_line_items(monkeypatch: MonkeyPatch) -> None:
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", "12", "2024"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
        order = Order()
        pay_order(order)




