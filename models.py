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
        pass  # TODO: readable representation for debugging


class Menu:
    """The full collection of Items; holds all items and filters by category."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        pass  # TODO: add an Item to the menu

    def filter_by_category(self, category):
        pass  # TODO: return the items matching the given category

    def get_all_items(self):
        pass  # TODO: return the full list of items


class Order:
    """A single transaction; holds selected Items and computes the total cost."""

    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, item):
        pass  # TODO: add an Item to this order

    def remove_item(self, item):
        pass  # TODO: remove an Item from this order

    def compute_total(self):
        pass  # TODO: sum item prices, store in self.total, and return it

    def get_items(self):
        pass  # TODO: return the selected items


class Customer:
    """A real user; tracks name and past purchase history to verify identity."""

    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, order):
        pass  # TODO: append a completed Order to purchase_history

    def is_verified(self):
        pass  # TODO: return whether the customer has prior purchase history