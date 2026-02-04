import streamlit as st
import pandas as pd

from src.forecasting import forecast_sales
from src.explanation import explain_decision
from src.data_loader import load_data
from src.shock_detection import detect_shocks
from src.inventory_decision import inventory_action

st.set_page_config(page_title="Supply Chain AI", layout="wide")

st.title("📦 Supply Chain AI Dashboard")
st.write("Real-time demand shock detection & inventory decisions")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
store = st.sidebar.selectbox("Select Store", sorted(df["store_nbr"].unique()))
family = st.sidebar.selectbox("Select Product Family", sorted(df["family"].unique()))

filtered_df = df[(df["store_nbr"] == store) & (df["family"] == family)]

# Detect shocks
filtered_df = detect_shocks(filtered_df)
filtered_df["action"] = filtered_df.apply(inventory_action, axis=1)

# Plot
st.subheader("📈 Sales Trend")
st.subheader("📈 Sales Trend")
chart_df = filtered_df.set_index("date")[["sales"]]
st.line_chart(chart_df)

# Show alerts
st.subheader("🚨 Recent Alerts")
alerts = filtered_df[filtered_df["shock"] == True].tail(5)

if alerts.empty:
    st.success("No demand shocks detected recently")
else:
    st.dataframe(alerts[["date", "sales", "z_score", "action"]])

filtered_df["explanation"] = filtered_df.apply(explain_decision, axis=1)

st.subheader("🧠 AI Explanation")
st.dataframe(
    filtered_df[["date", "sales", "shock", "action", "explanation"]].tail(10)
)

# Show raw data
with st.expander("See raw data"):
    st.dataframe(filtered_df.tail(20))

    st.subheader("🔮 7-Day Sales Forecast")
forecast = forecast_sales(filtered_df)
st.write(forecast)
