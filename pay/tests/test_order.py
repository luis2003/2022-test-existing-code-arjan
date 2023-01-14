from pay.order import Order, LineItem, OrderStatus


def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_total_for_order_w_one_lineitem() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    assert order.total == 100


def test_total_for_order_w_two_lineitems() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    order.line_items.append(LineItem(name="Test", price=100))
    assert order.total == 200


def test_pay() -> None:
    order = Order()
    assert order.status == OrderStatus.OPEN
    order.pay()
    assert order.status == OrderStatus.PAID
