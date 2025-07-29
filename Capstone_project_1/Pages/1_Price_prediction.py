import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Set Streamlit page configuration
st.set_page_config(page_title="Get Prediction")

# ? CSS Design Block (triple single-quotes used to avoid UnicodeDecodeError)
st.markdown('''
    <style>
        body {
            background-color: #f5faff;
            font-family: 'Segoe UI', sans-serif;
        }

        h1, h2, h3, .stSelectbox label {
            color: #1f3b4d;
        }

        .stButton > button {
            background-color: #1f3b4d;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-size: 16px;
            transition: 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #163447;
            transform: scale(1.02);
        }

        .stDataFrame {
            background-color: white;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 0 12px rgba(0, 0, 0, 0.05);
        }

        .stText {
            font-size: 16px;
            color: #333333;
        }
    </style>
''', unsafe_allow_html=True)

# Load DataFrame and pipeline
with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# Display dataframe
st.title("Real Estate Price Predictor")
st.subheader("Dataset Preview")
st.dataframe(df)

# Input Section
st.header("Enter Your Inputs")

# property_type
property_type = st.selectbox('Property Type', ['flat', 'house'])

# sector
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

# bedroom
bedroom = float(st.selectbox('No. of bedroom', sorted(df['bedRoom'].unique().tolist())))

# bathroom
bathroom = float(st.selectbox('No. of bathroom', sorted(df['bathroom'].unique().tolist())))

# balcony
balcony = st.selectbox('No. of balcony', sorted(df['balcony'].unique().tolist()))

# agePossession
Property_Age = st.selectbox('Age of Property', sorted(df['agePossession'].unique().tolist()))

# built_up_area
built_up_area = float(st.number_input('Built-Up Area (in sq ft)'))

# servant room
servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))

# store room
store_room = float(st.selectbox('Store Room', [0.0, 1.0]))

# furnishing_type
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

# luxury_category
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))

# floor_category
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# Prediction Button
if st.button('Predict'):
    data = [[property_type, sector, bedroom, bathroom, balcony, Property_Age,
             built_up_area, servant_room, store_room, furnishing_type,
             luxury_category, floor_category]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    st.subheader("Prediction Input Summary")
    st.dataframe(one_df)

    # Prediction
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.222

    # Result
    st.success('The estimated price range is:')
    st.markdown(f'''
        <div style="background-color:#d4edda; padding:15px; border-radius:10px; margin-top:10px;">
            <h3 style="color:#155724;">? {round(low, 2)} to ? {round(high, 2)}</h3>
        </div>
    ''', unsafe_allow_html=True)
