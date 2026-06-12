┌─────────────────────────────────┐         ┌─────────────────────────────────┐
│            Customer             │         │              Item               │
├─────────────────────────────────┤         ├─────────────────────────────────┤
│ - name: String                  │         │ - name: String                  │
│ - purchaseHistory: List<Order>  │         │ - price: double                 │
├─────────────────────────────────┤         │ - category: String              │
│ + getName(): String             │         │ - popularityRating: double      │
│ + getPurchaseHistory(): List    │         ├─────────────────────────────────┤
│ + isVerified(): boolean         │         │ + getName(): String             │
│ + addPurchase(o: Order): void   │         │ + getPrice(): double            │
└─────────────────────────────────┘         │ + getCategory(): String         │
              │                              │ + getPopularityRating(): double │
              │ makes                        └─────────────────────────────────┘
              │ 1                                          ▲
              ▼ *                                          │ contains *
┌─────────────────────────────────┐                       │
│             Order               │                       │
├─────────────────────────────────┤◇──────────────────────┤
│ - items: List<Item>             │  aggregates *         │
│ - total: double                 │                       │
├─────────────────────────────────┤         ┌─────────────────────────────────┐
│ + addItem(i: Item): void        │         │             Menu                │
│ + removeItem(i: Item): void     │         ├─────────────────────────────────┤
│ + computeTotal(): double        │         │ - items: List<Item>             │
│ + getItems(): List<Item>        │         ├─────────────────────────────────┤
└─────────────────────────────────┘         │ + addItem(i: Item): void        │
                                             │ + filterByCategory(c): List     │
                                             │ + getAllItems(): List<Item>     │
                                             └─────────────────────────────────┘◇───┐
                                                  │ holds *
                                                  ▼
                                                  (Item)
