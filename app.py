import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SupplySight AI",
    layout="wide"
)

st.title("SupplySight AI")
st.subheader("AI-Powered Supply Chain Forecasting & Insights")

uploaded_file = st.file_uploader("Upload train.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset loaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    df["date"] = pd.to_datetime(df["date"])

    store_id = st.selectbox(
        "Select Store Number",
        sorted(df["store_nbr"].unique())
    )

    family = st.selectbox(
        "Select Product Family",
        sorted(df["family"].unique())
    )

    filtered_df = df[
        (df["store_nbr"] == store_id) &
        (df["family"] == family)
    ].sort_values("date")

    st.subheader("Sales Over Time")

    chart_data = (
        filtered_df
        .set_index("date")[["sales"]]
    )

    st.line_chart(chart_data)

else:
    st.info("Please upload train.csv to begin.")
