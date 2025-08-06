import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# List of features used in training
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

st.set_page_config(page_title="EV Purchase Predictor", page_icon="🚗")
st.title("🚗 EV Purchase Prediction App")
st.markdown("👋 **Welcome! Fill out the information below to get a prediction related to electric vehicle purchase behavior.**")

# --- Inputs ---

location_state = st.selectbox("📍 Which Indian state are you from?", [
    'Assam', 'Bihar', 'Delhi', 'Jharkhand', 'Karnataka',
    'Madhya Pradesh', 'Maharashtra', 'Punjab', 'Telangana',
    'Uttar Pradesh', 'West Bengal'
])

urban_rural = st.radio("🏠 What type of area do you live in?", ['Urban', 'Rural'])

vehicle_ownership = st.radio("🛵 Do you currently own a two-wheeler?", ['Yes', 'No'])

ev_awareness = st.selectbox("💡 How aware are you about electric vehicles?", ['High', 'Low', 'Medium'])

charging_access = st.multiselect("🔌 Where do you have EV charging access?", ['Public', 'Work'])

brand_perception = st.selectbox("🏷️ How do you feel about EV brands in India?", ['Positive', 'Neutral', 'Negative'])

import_duty_impact = st.radio("📦 How much does import duty impact your decision?", ['High', 'Low', 'Medium'])

competitor_preference = st.radio("🚘 If not Tesla, which brand would you prefer?", ['Hyundai', 'Other'])

environmental_concern = st.radio("🌱 How concerned are you about the environment?", ['High', 'Low'])

age = st.number_input("🎂 What is your age?", min_value=18, max_value=100)

income = st.number_input("💰 What is your estimated annual income (₹)?", min_value=0)

purchase_intent = st.slider("🛍️ How likely are you to buy an EV? (0 = Not likely, 1 = Very likely)", 0.0, 1.0, 0.5)

price_sensitivity = st.slider("💸 How sensitive are you to price? (0 = Not at all, 1 = Very sensitive)", 0.0, 1.0, 0.5)

daily_commute = st.number_input("🚗 Average daily commute distance (km)", min_value=0.0)

electricity_cost = st.number_input("⚡ What is your local electricity cost (₹ per unit)?", min_value=0.0)

# --- Feature Mapping ---

input_dict = {feature: 0 for feature in selected_features}
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
input_dict['Age'] = age
input_dict['Income_Annual'] = income
input_dict['Purchase_Intent'] = purchase_intent
input_dict['Price_Sensitivity'] = price_sensitivity
input_dict['Daily_Commute_Distance'] = daily_commute
input_dict['Electricity_Cost'] = electricity_cost

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# --- Prediction ---
if st.button("🚀 Predict Now"):
    prediction = model.predict(input_df)
    intent_score = prediction[0]
    st.success(f"🚘 EV Purchase Intent Score: {intent_score:.2f}")
    
    if intent_score >= 0.75:
        st.info("🔥 This user is highly likely to purchase a Tesla EV.")
    elif intent_score >= 0.5:
        st.info("⚡ This user shows moderate interest in purchasing a Tesla EV.")
    else:
        st.info("❄️ This user currently shows low intent to purchase a Tesla EV.")

