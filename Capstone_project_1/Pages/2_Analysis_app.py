import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(page_title='Plotting Demo', layout='wide')

# ✅ Custom CSS for Design (Only UI Styling)
st.markdown("""
    <style>
        /* Set clean background */
        body {
            background-color: #f8fbff;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Header styling */
        h1, h2, h3, .stSelectbox label {
            color: #1f3b4d;
        }

        /* Enhance charts with soft card feel */
        .stPlotlyChart {
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
            padding: 10px;
        }

        /* Word cloud padding */
        .element-container:has(> .stImage) {
            padding: 15px;
        }

        /* Input components */
        .stSelectbox, .stRadio, .stButton {
            font-size: 16px;
        }

        /* Section spacing */
        .block-container {
            padding: 2rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Dashboard Title
st.title('📍 Real Estate Sector Analytics')

# Load CSV data
new_df = pd.read_csv('datasets/data_viz4.xls', encoding='cp1252')  # or encoding='utf-8' if cp1252 doesn't work
feature_text = pickle.load(open('datasets/feature_text.pkl','rb'))

# Columns to convert to numeric types
cols_to_convert = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']

# Convert columns to numeric, coercing errors
for col in cols_to_convert:
    new_df[col] = pd.to_numeric(new_df[col], errors='coerce')

# Drop rows with missing latitude or longitude
new_df = new_df.dropna(subset=['latitude', 'longitude'])

# Group by sector and calculate average values
group_df = new_df.groupby('sector')[cols_to_convert].mean().reset_index()

# Create a Mapbox scatter plot
fig = px.scatter_mapbox(
    group_df,
    lat='latitude',
    lon='longitude',
    color='price_per_sqft',
    size='built_up_area',
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    hover_name='sector',
    text='sector',
    width=1200,
    height=700
)
# Display the interactive map
st.plotly_chart(fig, use_container_width=True, key="map_chart")

# Feature Word Cloud
st.title('Feature Word Cloud')

# Set font for matplotlib
plt.rcParams["font.family"] = "Arial"

# Generate word cloud
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    stopwords=set(['s']),
    min_font_size=10,
    colormap='plasma'  # Changed color combination
).generate(feature_text)

# Display the word cloud
plt.figure(figsize=(6, 6), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
st.pyplot()

# Area vs Price
st.title('Area Vs Price')
property_type = st.selectbox('Select property type', ['flat', 'house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, use_container_width=True, key="house_price")
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, use_container_width=True, key="flat_price")

# BHK Pie Chart
st.title('BHK Pie Chart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')
selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True, key="overall_bhk")
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True, key="sector_bhk")

# Side-by-side BHK Price Comparison
st.title('Side by Side BHK Price Comparison')
fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True, key="bhk_boxplot")

# Distplot for property types
st.title('Side by Side Distplot for Property Type')
fig4 = plt.figure(figsize=(10, 4))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'], kde=True, label='house', color='skyblue')
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], kde=True, label='flat', color='salmon')
plt.legend()
st.pyplot(fig4)
