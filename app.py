import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('model.pkl')

st.title("Random Forest Regression with RFE")

# Input fields
st.write("Enter the feature values:")

# Example: If you have 10 selected features
feature_1 = st.number_input("Feature 1")
feature_2 = st.number_input("Feature 2")
# ... repeat for all selected features

# Collect inputs into a DataFrame
input_df = pd.DataFrame([[feature_1, feature_2]], columns=['Feature 1', 'Feature 2'])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Value: {prediction[0]}")
