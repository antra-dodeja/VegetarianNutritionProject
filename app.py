import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv('vegetarian_foods.csv')


st.title("Vegetarian Food Nutrition Explorer")


# User selects nutrient
nutrient = st.selectbox("Select Nutrient", df.columns[1:])
top_n = st.slider("Number of Foods to Show", 1, 10, 5)


# Display top foods
top_foods = df.sort_values(nutrient, ascending=False).head(top_n)
st.write(top_foods)


# Bar chart
plt.figure(figsize=(10,5))
sns.barplot(x=nutrient, y='Food Item', data=top_foods)
st.pyplot(plt)