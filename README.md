# Real-Estate-project
# Real Estate Price Prediction and Recommendation System

This repository contains a comprehensive machine learning project focused on predicting property prices and recommending similar properties based on location and features. The project uses real estate data from Gurgaon and includes all steps from data preprocessing to model deployment preparation.

## Table of Contents

- Introduction
- Objectives
- Project Structure
- Features
- Datasets
- How to Run the Project
- Results and Findings
- Technologies Used
- Author
- License

## Introduction

This project simulates a real-world machine learning pipeline. The goal is to build a reliable system for predicting house prices and recommending similar properties based on a user's input. It also includes extensive data cleaning, feature selection, and exploratory data analysis steps to improve model accuracy and usability.

## Objectives

- Clean and preprocess real-world property datasets
- Perform exploratory data analysis and visualizations
- Select and engineer relevant features for modeling
- Train multiple regression models for price prediction
- Implement a content-based property recommendation system
- Save and reuse models and pipelines for deployment

## Project Structure
Capstone_project_1/
│
├── datasets/
│ ├── data files (.csv, .xls)
│ ├── similarity matrices (.pkl)
│ ├── location and distance data
│
├── Pages/
│ ├── 1_Price_prediction.py
│ ├── 2_Analysis_app.py
│ └── Recommendation_system.py
│
├── pipeline.pkl
├── pipeline1.pkl
├── df.pkl
├── home.py
├── output_report.html
└── README.md

## Features

- End-to-end data processing and cleaning
- Outlier detection and treatment
- Missing value imputation
- Feature engineering and selection
- Model training and evaluation
- Recommendation system using cosine similarity
- Serialization of models and pipelines for future use

## Datasets

The project uses multiple versions of cleaned datasets, including:

- flats_cleaned.csv
- house_cleaned.csv
- gurgaon_properties_cleaned_v1.csv
- gurgaon_properties_cleaned_v2.csv
- gurgaon_properties_outlier_treated.csv
- gurgaon_properties_missing_value_imputation.csv
- gurgaon_properties_post_feature_selection.csv
- latlong.csv
- data_viz1.csv to data_viz4.csv
- cosine similarity matrices in pickle format
- location_distance.pkl
- feature_text.pkl

These datasets contain property features such as size, number of bedrooms, location coordinates, amenities, and price


## Results and Findings

- Data preprocessing significantly improved model accuracy.
- Feature selection helped reduce overfitting and increased model interpretability.
- Property price prediction models were evaluated using RMSE and R2 metrics.
- Cosine similarity provided intuitive recommendations for similar properties based on user input.
- Modular codebase allows easy extension or integration with web frameworks.

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Pickle
- Matplotlib, Seaborn, Plotly
- Streamlit (optional)
- Jupyter Notebooks

Sakshi Dubey  
Email: sakshidubey0101104@gmail.com  
GitHub: [github.com/Sakshidubey205](https://github.com/Sakshidubey205)  
LinkedIn: [linkedin.com/in/sakshi-dubey-ab2309289](https://www.linkedin.com/in/sakshi-dubey-ab2309289)
