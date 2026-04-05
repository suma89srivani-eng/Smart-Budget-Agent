import streamlit as st
from utils.expense_analyzer import analyze_expenses
from utils.budget_tracker import check_budget_status
from utils.insights import generate_insights

st.set_page_config(page_title="Smart Budget Agent", page_icon="💰", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        .main-title {
            font-size: 3rem;
            font-weight: 800;
            color: white;
        }
        .hero-box {
            background: linear-gradient(90deg, #1e3c72, #2a5298);
            padding: 2rem;
            border-radius: 25px;
            color: white;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.12);
        }
        .feature-card {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 20px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
            border: 1px solid #e8edf5;
            min-height: 220px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class="hero-box">
    <div class="main-title">💰 Smart Budget Agent</div>
    <p style="font-size: 1.2rem; margin-top: 1rem;">
        A smart budgeting assistant that helps users track expenses,
        manage spending, analyze budgets, and build better financial habits.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# --- Features ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h2>💸 Expense Tracking</h2>
        <p>Record and organize daily spending with category-based tracking.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h2>📊 Budget Monitoring</h2>
        <p>Track how much of your monthly budget has been used.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h2>🧠 Spending Insights</h2>
        <p>Get useful financial observations and money-saving suggestions.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# --- Input Section ---
st.subheader("📝 Add Expense Details")

monthly_budget = st.number_input("Enter Monthly Budget (₹)", min_value=0.0, step=500.0)

expenses = []

num_entries = st.number_input("How many expense entries?", min_value=1, max_value=20, step=1)

for i in range(num_entries):
    st.markdown(f"### Expense {i+1}")
    category = st.selectbox(
        f"Category {i+1}",
        ["Food", "Transport", "Shopping", "Bills", "Health", "Entertainment", "Other"],
        key=f"category_{i}"
    )
    amount = st.number_input(f"Amount {i+1} (₹)", min_value=0.0, step=100.0, key=f"amount_{i}")
    expenses.append({"category": category, "amount": amount})

if st.button("Analyze Budget"):
    total_expenses, category_totals = analyze_expenses(expenses)
    budget_status = check_budget_status(monthly_budget, total_expenses)
    insights = generate_insights(category_totals)

    st.subheader("📋 Budget Report")
    st.write(f"### Total Expenses: ₹{total_expenses:.2f}")

    st.write("### Category-wise Spending")
    for category, amount in category_totals.items():
        st.write(f"- {category}: ₹{amount:.2f}")

    st.write("### Budget Status")
    st.success(budget_status)

    st.write("### Smart Insights")
    for insight in insights:
        st.info(insight)
