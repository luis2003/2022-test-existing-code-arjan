import pytest
from _pytest.monkeypatch import MonkeyPatch

from pay.credit_card import CreditCard
from pay.order import Order, LineItem
from pay.payment import pay_order
from datetime import date


class PaymentProcessorMock:
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        print(f"Charging {card} with amount ${amount/100:.2f}.")


@pytest.fixture
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard("1249190007575069", 12, year)


def test_pay_order(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order, card, PaymentProcessorMock())


def test_pay_order_invalid_order_no_line_items(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        order = Order()
        pay_order(order, card, PaymentProcessorMock())




