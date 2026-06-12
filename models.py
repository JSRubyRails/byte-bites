# ByteBites backend object model.
#
# Four classes model the domain:
#   Customer - a real user; tracks name and purchase history (list of Orders)
#              to verify identity.
#   Item     - a single food/drink product; has name, price, category, and
#              popularity rating.
#   Menu     - the full collection of Items; holds all items and filters them
#              by category.
#   Order    - a single transaction; holds the selected Items and computes the
#              total cost.
#
# Relationships: a Customer makes many Orders; Menu and Order both aggregate
# (share) Item instances rather than owning copies.


class Item:
    """A single food/drink product, e.g. a 'Spicy Burger' or 'Large Soda'."""

    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return (
            f"Item(name={self.name!r}, price={self.price}, "
            f"category={self.category!r}, popularity_rating={self.popularity_rating})"
        )


class Menu:
    """The full collection of Items; holds all items and filters by category."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self, descending=True):
        return sorted(
            self.items,
            key=lambda item: item.popularity_rating,
            reverse=descending,
        )

    def get_all_items(self):
        return self.items


class Order:
    """A single transaction; holds selected Items and computes the total cost."""

    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def compute_total(self):
        self.total = sum(item.price for item in self.items)
        return self.total

    def get_items(self):
        return self.items


class Customer:
    """A real user; tracks name and past purchase history to verify identity."""

    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, order):
        self.purchase_history.append(order)

    def is_verified(self):
        return len(self.purchase_history) > 0
    