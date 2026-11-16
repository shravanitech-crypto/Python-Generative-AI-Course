import streamlit as st
import pandas as pd
import numpy as np
## Title of application
st.title("My Streamlit App")

## Simple text
st.write("This is a simple Streamlit application.")

## create simple dataframe
df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

## Display dataframe
st.write("Here is a simple dataframe:")
st.dataframe(df)

## Create a simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=["a","b","c"]
)
st.line_chart(chart_data)