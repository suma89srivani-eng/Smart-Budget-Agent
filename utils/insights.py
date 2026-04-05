def generate_insights(category_totals):
    """
    Generates simple spending insights.
    """
    if not category_totals:
        return ["No spending data available."]

    highest_category = max(category_totals, key=category_totals.get)
    highest_amount = category_totals[highest_category]

    insights = [
        f"📌 Highest spending category: {highest_category} (₹{highest_amount:.2f})"
    ]

    if highest_amount > 5000:
        insights.append("💡 Consider reviewing this category to reduce expenses.")

    if "Food" in category_totals and category_totals["Food"] > 3000:
        insights.append("🍔 Your food expenses are relatively high this month.")

    if "Shopping" in category_totals and category_totals["Shopping"] > 4000:
        insights.append("🛍️ Shopping expenses are above average. Consider limiting impulse purchases.")

    return insights
