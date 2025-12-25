import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Healthcare Patient Risk Dashboard")

df = pd.read_csv("heart.csv")

fig = px.histogram(df, x="age", color="target", title="Patient Risk Distribution")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(df.head())
