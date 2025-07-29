import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Real Estate App", layout="centered")

# --- Homepage Title ---
st.markdown("<h1 style='text-align: center; color:#1f3b4d;'>Welcome to the Real Estate Insights Platform 🏡</h1>", unsafe_allow_html=True)

# --- Detailed Home Description ---
st.markdown("""
Welcome to an interactive real estate platform designed to help you **analyze** and **predict property prices** effortlessly.

This tool is ideal for:
- 🏘️ Home buyers who want to check if a property is reasonably priced
- 📈 Real estate agents seeking to understand market trends
- 🧑‍💻 Data enthusiasts curious about real estate patterns

---

### 🔍 What You Can Do Here:

#### 1. **Price Predictor**
> Go to the “Price Predictor” page from the sidebar.  
> Fill out property details like:
- Property Type (Flat or House)
- Sector/Location
- Number of bedrooms, bathrooms, balconies
- Built-up area (in sq. ft)
- Age of the property
- Furnishing and luxury category  
🎯 The model will give you an estimated price range using a trained machine learning pipeline.

---

#### 2. **Analysis App**
> Head over to the “Analysis App” section to explore beautiful visuals:
- 🗺️ **Interactive Maps**: See prices and sizes by location  
- 📊 **Scatter Plots**: Compare area vs. price  
- 🧁 **Pie Charts**: Understand BHK distribution across sectors  
- 📦 **Boxplots**: Price comparison for 1BHK to 4BHK  
- ☁️ **Word Cloud**: Highlights most frequent features

---

### 🚀 How to Navigate:
Use the **left-hand sidebar** to choose between:
- 🏠 Home (you're here)
- 💰 Price Predictor
- 📈 Analysis App

Explore. Learn. Decide wisely.
""", unsafe_allow_html=True)

# --- Footer (Fixed Position) ---
st.markdown("""
    <div style='position: fixed; bottom: 10px; left: 10px; background-color: #1f3b4d; padding: 10px 15px; border-radius: 8px; color: white; font-size: 14px;'>
        Developed by Sakshi
    </div>
""", unsafe_allow_html=True)

# --- Footer Credit ---
st.markdown("<div style='text-align: center; color: gray; margin-top: 30px;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
