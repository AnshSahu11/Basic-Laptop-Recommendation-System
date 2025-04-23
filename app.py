import streamlit as st
import numpy as np
import pandas as pd

#load dataset
df = pd.read_csv('laptops.csv')

st.title("💻 Laptop Recommendation System")

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")
budget = st.sidebar.slider("Select Budget", min_value=int(df['price'].min()), max_value=int(df['price'].max()), value=(30000, 70000))
processor = st.sidebar.selectbox("Select Processor", options=df["processor_brand"].unique())
ram = st.sidebar.selectbox("Select RAM (GB)", options=sorted(df["ram_num"].unique()))


# Apply Filters
filtered_df = df[(df["price"] >= budget[0]) &
                 (df["price"] <= budget[1]) &
                 (df["processor_brand"] == processor) &
                 (df["ram_num"] == ram)]

# Sort by rating
filtered_df = filtered_df.sort_values(by="rating", ascending=False)

# Display Recommended Laptops
st.subheader("🎯 Recommended Laptops")
st.write(f"Showing {len(filtered_df)} laptops that match your preferences:")

if not filtered_df.empty:
    st.dataframe(filtered_df[["brand_name", "processor_brand", "ram_num", "price", "rating"]], use_container_width=True, height = 600)
else:
    st.warning("No laptops found for the selected criteria. Try adjusting your filters!")
