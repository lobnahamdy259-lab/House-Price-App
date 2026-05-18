import streamlit as st
import pandas as pd
import joblib

# --- App Configuration ---
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# --- UI Styling & Header ---
st.title("🏠 House Price Prediction App")
st.markdown("""
Welcome to the House Price Predictor! 
Please provide the property details in the sidebar, and we will estimate its value using an advanced Machine Learning model.
""")

# --- Model Loading ---
@st.cache_resource
def load_model():
    try:
        # Load the Scikit-learn Pipeline
        model = joblib.load("house_price_model.pkl")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# --- Sidebar Inputs ---
st.sidebar.header("🏡 Enter House Details")

# Group 1: General Quality & Size
st.sidebar.subheader("General Quality & Size")
overall_qual = st.sidebar.slider(
    "Overall Quality (1-10)", 
    min_value=1, max_value=10, value=5, step=1,
    help="Rates the overall material and finish of the house"
)
gr_liv_area = st.sidebar.number_input(
    "Above Ground Living Area (sq ft)", 
    min_value=300, max_value=6000, value=1500, step=50
)

# Group 2: Basement Features
st.sidebar.subheader("Basement Features")
total_bsmt_sf = st.sidebar.number_input(
    "Total Basement Area (sq ft)", 
    min_value=0, max_value=6500, value=1000, step=50
)
bsmt_fin_sf1 = st.sidebar.number_input(
    "Finished Basement Area (sq ft)", 
    min_value=0, max_value=6000, value=500, step=50
)

# Group 3: Other Features
st.sidebar.subheader("Other Features")
first_flr_sf = st.sidebar.number_input(
    "First Floor Area (sq ft)", 
    min_value=300, max_value=5000, value=1000, step=50
)
garage_area = st.sidebar.number_input(
    "Garage Area (sq ft)", 
    min_value=0, max_value=1500, value=400, step=50
)


# --- Prediction Section ---
st.markdown("---")
st.subheader("Predict Price")

# Use columns for better layout of the prediction button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    predict_btn = st.button("Estimate Price", type="primary", use_container_width=True)

if predict_btn:
    if model is not None:
        # Create input dataframe exactly matching expected features
        input_data = pd.DataFrame({
            'OverallQual': [overall_qual],
            'GrLivArea': [gr_liv_area],
            'TotalBsmtSF': [total_bsmt_sf],
            'BsmtFinSF1': [bsmt_fin_sf1],
            '1stFlrSF': [first_flr_sf],
            'GarageArea': [garage_area]
        })
        
        try:
            # Predict using the loaded pipeline
            # The model pipeline already handles preprocessing (imputing, scaling, encoding)
            prediction = model.predict(input_data)
            estimated_price = prediction[0]
            
            # Display results
            st.success("Prediction successful! 🎉")
            st.metric(label="Estimated House Price", value=f"${estimated_price:,.2f}")
            st.balloons()
            
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.error("Model not loaded. Cannot make prediction. Please check if 'house_price_model.pkl' exists in the directory.")
