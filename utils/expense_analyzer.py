def analyze_expenses(expenses):
    """
    Calculates total expenses and category-wise breakdown.
    expenses = list of dictionaries:
    [{"category": "Food", "amount": 250}, ...]
    """
    total = sum(item["amount"] for item in expenses)

    category_totals = {}
    for item in expenses:
        category = item["category"]
        amount = item["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    return total, category_totals
