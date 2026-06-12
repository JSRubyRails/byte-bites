┌─────────────────────────────────┐              ┌─────────────────────────────────┐
│            Customer             │              │             Menu                │
├─────────────────────────────────┤              ├─────────────────────────────────┤
│ - name: String                  │              │ - items: List<Item>             │
│ - purchaseHistory: List<Order>  │              ├─────────────────────────────────┤
├─────────────────────────────────┤              │ + addItem(i: Item): void        │
│ + getName(): String             │              │ + filterByCategory(c): List     │
│ + getPurchaseHistory(): List    │              │ + getAllItems(): List<Item>     │
│ + isVerified(): boolean         │              └─────────────────────────────────┘
│ + addPurchase(o: Order): void   │                            ◇
└─────────────────────────────────┘                            │ holds *
                 │                                              ▼
                 │ makes 1..*                       ┌─────────────────────────────────┐
                 ▼                                  │              Item               │
┌─────────────────────────────────┐                ├─────────────────────────────────┤
│             Order               │                │ - name: String                  │
├─────────────────────────────────┤      holds *   │ - price: double                 │
│ - items: List<Item>             │ ◇─────────────▶ │ - category: String              │
│ - total: double                 │                │ - popularityRating: double      │
├─────────────────────────────────┤                ├─────────────────────────────────┤
│ + addItem(i: Item): void        │                │ + getName(): String             │
│ + removeItem(i: Item): void     │                │ + getPrice(): double            │
│ + computeTotal(): double        │                │ + getCategory(): String         │
│ + getItems(): List<Item>        │                │ + getPopularityRating(): double │
└─────────────────────────────────┘                └─────────────────────────────────┘
