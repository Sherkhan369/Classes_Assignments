# app.py

import streamlit as st
from grocery_store import Inventory, SalesManager

# --- Initialize session state ---
if 'inventory' not in st.session_state:
    st.session_state.inventory = Inventory()
if 'sales' not in st.session_state:
    st.session_state.sales = SalesManager()

st.set_page_config(page_title="Grocery Store Management", layout="centered")
st.title("🛒 Grocery Store Management System")

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["➕ Add Items", "📦 Inventory", "💰 Sales"])

# -----------------------------
# ➕ Add New Item
# -----------------------------
with tab1:
    st.subheader("Add New Item to Inventory")
    with st.form("add_item_form"):
        name = st.text_input("Item Name")
        price = st.number_input("Price per unit ($)", min_value=0.0, format="%.2f")
        quantity = st.number_input("Quantity", min_value=1)
        submit = st.form_submit_button("Add / Update Item")

        if submit and name:
            st.session_state.inventory.add_item(name, price, int(quantity))
            st.success(f"'{name}' added or updated successfully!")

# -----------------------------
# 📦 View Inventory
# -----------------------------
with tab2:
    st.subheader("Inventory")
    items = st.session_state.inventory.list_items()

    if not items:
        st.info("Inventory is empty.")
    else:
        for name, item in items.items():
            st.markdown(f"**{name}** - ${item.price:.2f} | Stock: {item.quantity}")

# -----------------------------
# 💰 Sell Items
# -----------------------------
with tab3:
    st.subheader("Sell Item")
    item_names = list(st.session_state.inventory.list_items().keys())

    if not item_names:
        st.warning("No items to sell. Add some first.")
    else:
        selected = st.selectbox("Select Item", item_names)
        qty = st.number_input("Quantity to Sell", min_value=1, value=1)
        if st.button("Sell"):
            result = st.session_state.sales.sell_item(st.session_state.inventory, selected, qty)
            st.info(result)

        # --- Sales Summary ---
        st.divider()
        st.markdown(f"### 📈 Total Sales: **${st.session_state.sales.get_total_sales():.2f}**")
        st.markdown("### 🧾 Sales Log")
        for log in st.session_state.sales.get_sales_log():
            st.markdown(f"- Sold {log[1]} x {log[0]} → ${log[2]:.2f}")
