# 💻 Laptop Recommendation System

This is a simple **Laptop Recommendation System** built using **Streamlit**, **Pandas**, and **NumPy**. It helps users filter laptops based on their **budget**, **processor type**, and **RAM capacity**, and provides recommendations sorted by **ratings**.

---

## 🚀 Features

- 📊 Load and display laptop dataset (`laptops.csv`)
- 🔍 Sidebar filters:
  - **Budget Range** (Slider)
  - **Processor Brand** (Dropdown)
  - **RAM Size** (Dropdown)
- 📈 Sort filtered results by rating (highest first)
- ✅ Display recommended laptops in a table format
- ⚠️ Warn users when no laptops match the selected criteria

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

---

## 📂 Dataset

The app expects a CSV file named `laptops.csv` with the following relevant columns:

- `brand_name`
- `processor_brand`
- `ram_num` (RAM in GB)
- `price` (Price in INR)
- `rating` (Customer rating)

Make sure your dataset is clean and contains the above columns for the app to function properly.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/laptop-recommendation-app.git
   cd laptop-recommendation-app
