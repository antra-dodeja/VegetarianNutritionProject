import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Vegetarian Food Nutrition Explorer")

# Upload file
uploaded_file = st.file_uploader("Upload your food nutrition file (.csv or .xlsx)", type=["csv", "xlsx"])

if uploaded_file:
    # Detect file type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File loaded successfully!")
    st.write(df)

    # Select nutrient (skip first column)
    nutrient = st.selectbox("Select Nutrient", df.columns[1:])
    top_n = st.slider("Number of Foods to Show", 1, 10, 5)

    # Get top foods
    top_foods = df.sort_values(nutrient, ascending=False).head(top_n)

    st.subheader(f"Top {top_n} Foods by {nutrient}")
    st.write(top_foods)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=nutrient, y=df.columns[0], data=top_foods, ax=ax)
    st.pyplot(fig)

else:
    st.info("Please upload a CSV or Excel file to continue.")
