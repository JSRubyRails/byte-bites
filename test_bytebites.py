# Tests for the ByteBites object model. Run with: python3 -m pytest test_bytebites.py
# (or simply: python3 test_bytebites.py to run the lightweight fallback runner.)

from models import Item, Menu, Order, Customer


def make_menu():
    """Helper: a small menu used across several tests."""
    menu = Menu()
    menu.add_item(Item("Spicy Burger", 8.50, "Mains", 4.7))
    menu.add_item(Item("Large Soda", 2.00, "Drinks", 3.9))
    menu.add_item(Item("Iced Tea", 2.50, "Drinks", 4.2))
    menu.add_item(Item("Brownie", 3.75, "Desserts", 4.8))
    return menu


def test_order_total():
    """Total is the sum of the prices of the items in the order."""
    order = Order()
    order.add_item(Item("Spicy Burger", 8.50, "Mains", 4.7))
    order.add_item(Item("Large Soda", 2.00, "Drinks", 3.9))
    assert order.compute_total() == 10.50


def test_empty_order_total():
    """An order with no items has a total of zero."""
    order = Order()
    assert order.compute_total() == 0


def test_filter_by_category():
    """Filtering returns only the items in the requested category."""
    menu = make_menu()
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 2
    assert {item.name for item in drinks} == {"Large Soda", "Iced Tea"}


def test_filter_by_missing_category():
    """Filtering on a category with no items returns an empty list."""
    menu = make_menu()
    assert menu.filter_by_category("Sides") == []


def test_sort_by_popularity():
    """Sorting returns items ordered by popularity, highest first by default."""
    menu = make_menu()
    ranked = [item.name for item in menu.sort_by_popularity()]
    assert ranked == ["Brownie", "Spicy Burger", "Iced Tea", "Large Soda"]


def test_remove_item_updates_total():
    """Removing an item is reflected in a recomputed total."""
    order = Order()
    burger = Item("Spicy Burger", 8.50, "Mains", 4.7)
    soda = Item("Large Soda", 2.00, "Drinks", 3.9)
    order.add_item(burger)
    order.add_item(soda)
    order.remove_item(soda)
    assert order.compute_total() == 8.50


def test_customer_verification():
    """A customer is unverified until they have at least one past order."""
    customer = Customer("Ada")
    assert customer.is_verified() is False
    customer.add_purchase(Order())
    assert customer.is_verified() is True


if __name__ == "__main__":
    # Lightweight fallback runner so the file works without pytest installed.
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {test.__name__}: {exc}")
    print(f"\n{len(tests) - failures}/{len(tests)} passed")