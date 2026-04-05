def check_budget_status(monthly_budget, total_expenses):
    """
    Compares total expenses against budget.
    """
    remaining = monthly_budget - total_expenses

    if remaining < 0:
        return f"🔴 Budget exceeded by ₹{abs(remaining):.2f}"
    elif remaining < monthly_budget * 0.2:
        return f"🟠 Warning: Only ₹{remaining:.2f} left in your budget"
    else:
        return f"🟢 Good! You still have ₹{remaining:.2f} remaining"
