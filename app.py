import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# List of selected features (in exact order used during training)
selected_features = [
    'Location_State_Assam', 'Location_State_Bihar', 'Location_State_Delhi',
    'Location_State_Jharkhand', 'Location_State_Karnataka',
    'Location_State_Madhya Pradesh', 'Location_State_Maharashtra',
    'Location_State_Punjab', 'Location_State_Telangana',
    'Location_State_Uttar Pradesh', 'Location_State_West Bengal',
    'Urban_Rural_Rural', 'Urban_Rural_Urban',
    'Vehicle_Ownership_Two-Wheeler', 'EV_Awareness_High',
    'EV_Awareness_Low', 'Charging_Access_Public', 'Charging_Access_Work',
    'Brand_Perception_Neutral', 'Brand_Perception_Positive',
    'Import_Duty_Impact_High', 'Import_Duty_Impact_Low',
    'Competitor_Preference_Hyundai', 'Environmental_Concern_High',
    'Age', 'Income_Annual', 'Purchase_Intent', 'Price_Sensitivity',
    'Daily_Commute_Distance', 'Electricity_Cost'
]

st.title("🚗 EV Purchase Prediction App")

# Create input widgets for each feature
st.subheader("Fill in the details below:")

# Binary or categorical inputs converted to one-hot encoding style
location_state = st.selectbox("Select State", [
    'Assam', 'Bihar', 'Delhi', 'Jharkhand', 'Karnataka',
    'Madhya Pradesh', 'Maharashtra', 'Punjab', 'Telangana',
    'Uttar Pradesh', 'West Bengal'
])
urban_rural = st.selectbox("Urban or Rural", ['Urban', 'Rural'])
vehicle_ownership = st.selectbox("Do you own a Two-Wheeler?", ['Yes', 'No'])
ev_awareness = st.selectbox("EV Awareness", ['High', 'Low', 'Medium'])
charging_access = st.multiselect("Charging Access Available at:", ['Public', 'Work'])
brand_perception = st.selectbox("Brand Perception", ['Positive', 'Neutral', 'Negative'])
import_duty_impact = st.selectbox("Impact of Import Duty", ['High', 'Low', 'Medium'])
competitor_preference = st.selectbox("Preferred Competitor", ['Hyundai', 'Other'])
environmental_concern = st.selectbox("Environmental Concern", ['High', 'Low'])

# Numeric inputs
age = st.number_input("Your Age", min_value=18, max_value=100)
income = st.number_input("Annual Income (in ₹)", min_value=0)
purchase_intent = st.slider("Purchase Intent (0 = Low, 1 = High)", 0.0, 1.0, 0.5)
price_sensitivity = st.slider("Price Sensitivity (0 = Low, 1 = High)", 0.0, 1.0, 0.5)
daily_commute = st.number_input("Daily Commute Distance (km)", min_value=0.0)
electricity_cost = st.number_input("Electricity Cost (₹ per unit)", min_value=0.0)

# Prepare a dictionary for the input row
input_dict = {feature: 0 for feature in selected_features}

# Set one-hot values
input_dict[f'Location_State_{location_state}'] = 1
input_dict[f'Urban_Rural_{urban_rural}'] = 1
input_dict['Vehicle_Ownership_Two-Wheeler'] = 1 if vehicle_ownership == 'Yes' else 0
input_dict['EV_Awareness_High'] = 1 if ev_awareness == 'High' else 0
input_dict['EV_Awareness_Low'] = 1 if ev_awareness == 'Low' else 0
input_dict['Charging_Access_Public'] = 1 if 'Public' in charging_access else 0
input_dict['Charging_Access_Work'] = 1 if 'Work' in charging_access else 0
input_dict['Brand_Perception_Positive'] = 1 if brand_perception == 'Positive' else 0
input_dict['Brand_Perception_Neutral'] = 1 if brand_perception == 'Neutral' else 0
input_dict['Import_Duty_Impact_High'] = 1 if import_duty_impact == 'High' else 0
input_dict['Import_Duty_Impact_Low'] = 1 if import_duty_impact == 'Low' else 0
input_dict['Competitor_Preference_Hyundai'] = 1 if competitor_preference == 'Hyundai' else 0
input_dict['Environmental_Concern_High'] = 1 if environmental_concern == 'High' else 0

# Set numeric values
input_dict['Age'] = age
input_dict['Income_Annual'] = income
input_dict['Purchase_Intent'] = purchase_intent
input_dict['Price_Sensitivity'] = price_sensitivity
input_dict['Daily_Commute_Distance'] = daily_commute
input_dict['Electricity_Cost'] = electricity_cost

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Predict and show result
if st.button("🚀 Predict"):
    prediction = model.predict(input_df)
    st.success(f"🎯 Predicted Output: {prediction[0]:.2f}")
