
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Qahwa Corner Sales Dashboard",
    layout="wide"
)

st.title("Qahwa Corner - Sales Dashboard")
st.write("Coffee Chain Sales Analysis")

# Load dataset
df = pd.read_csv("cafe_sales.csv")

# Branch selector
branches = ["All Branches"] + sorted(
    df["branch"].dropna().unique().tolist()
)

selected_branch = st.selectbox(
    "Select Branch",
    branches
)

# Filter data
if selected_branch == "All Branches":
    filtered_df = df.copy()
else:
    filtered_df = df[df["branch"] == selected_branch]

# Total revenue
total_revenue = filtered_df["total_sar"].sum()

st.metric(
    "Total Revenue (SAR)",
    f"{total_revenue:,.2f}"
)

# Revenue by product
product_revenue = (
    filtered_df.groupby("product")["total_sar"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Revenue by Product")
st.bar_chart(product_revenue)

st.subheader("Sales Data")
st.dataframe(filtered_df)
