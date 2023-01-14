from pay.order import LineItem


def test_total_with_default_quantity() -> None:
    line_item = LineItem("Test", 100)
    assert line_item.total == 100


def test_total_with_qty_more_than_one() -> None:
    line_item = LineItem("Test", 200, 5)
    assert line_item.total == 1000
