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