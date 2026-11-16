import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")
options = ["java","python","c++"]
choices = st.selectbox("Select your favorite programming language:", options)
st.write(f"Your favorite programming language is: {choices}")
if name:
    st.write(f"Hello, {name}!")

data={
    "Name" : ["John","Alice","Bob"],
    "Age" : [25,30,22],
    "city" : ["New York","Los Angeles","Chicago"]
}

df = pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)



