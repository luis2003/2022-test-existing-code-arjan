import pytest
from _pytest.monkeypatch import MonkeyPatch

from pay.order import Order, LineItem
from pay.payment import pay_order


class PaymentProcessorMock:
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        print(f"Charging {card} with amount ${amount/100:.2f}.")


def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    inputs = ["1249190007575069", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order, PaymentProcessorMock())


def test_pay_order_invalid_order_no_line_items(monkeypatch: MonkeyPatch) -> None:
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", "12", "2024"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        order = Order()
        pay_order(order, PaymentProcessorMock())




