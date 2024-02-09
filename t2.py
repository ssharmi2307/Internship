# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:14:49 2024

@author: Gopinath
"""

import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the train and test datasets
train_data = pd.read_excel("train.xlsx")
test_data = pd.read_excel("test.xlsx")

# Split the train data into features (X) and target (y)
X_train = train_data.drop(columns=["target"])
y_train = train_data["target"]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(test_data)

# Load the trained model
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train_scaled, y_train)

# Function to preprocess the uploaded CSV file
def preprocess_data(file):
    df = pd.read_excel(file)
    df.fillna(0, inplace=True)  # Handle missing values
    return scaler.transform(df)  # Standardize the features

# Main function to run the Streamlit web app
def main():
    st.title("Random Forest Classifier Deployment")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload excel file", type=["xlsx"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Preprocess the uploaded data
        test_data = preprocess_data(uploaded_file)

        # Make predictions
        predictions = rf_classifier.predict(test_data)

        # Display predictions
        st.write("Predictions:")
        st.write(predictions)

        # Save predictions to a CSV file
        predictions_df = pd.DataFrame(predictions, columns=["target"])
        st.write("Download predictions as CSV:")
        st.download_button(label="Download", data=predictions_df.to_csv(), file_name="predictions.csv", mime="text/csv")

        # Calculate accuracy (optional)
        # Note: Since we don't have ground truth labels for the uploaded test data,
        # we cannot calculate accuracy in this deployment.

# Run the app
if __name__ == "__main__":
    main()
