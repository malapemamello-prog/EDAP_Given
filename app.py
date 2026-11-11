import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Data Explorer", layout="wide")
st.title("CSV Data Explorer")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
   df=pd.read_csv(uploaded_file)
st.dataframe(df.head(5))
st.metric("Rows", len(df))
column = st.select_box("Column", df.columns.tolist())

filter_enabled = st.checkbox("Enable filter", default=False
choices = sorted(df[column].dropna().astype(str).unique().tolist())

selected = st.multiselect("Values", options=choices, default=choices)
filtered = df.copy()

filtered = filtered[filtered[column].astype(str).isin(selected)]
st.dataframe(filtered)

st.metric("Filtered rows", filtered.shape[0])
counts = filtered[column].fillna("Missing").astype(str).value_counts()

st.bar_chart(counts)
st.download_button("Download CSV", filtered.to_csv(index=False), filename="filtered.csv")
