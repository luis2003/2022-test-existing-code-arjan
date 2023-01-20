from typing import Protocol

from pay.credit_card import CreditCard
from pay.order import Order
from pay.processor import PaymentProcessor


class PaymentProcessor(Protocol):
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        """Charges the card with the amount."""


def pay_order(order: Order, card: CreditCard, processor: PaymentProcessor):
    if order.total == 0:
        raise ValueError("Can't pay an order with total of 0.")
    processor.charge(card.number, card.expiry_month, card.expiry_year, amount=order.total)
    order.pay()
