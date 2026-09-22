import streamlit as st
import pandas as pd
from datetime import date
from src.predict import predict_aqi, get_aqi_category
from src.preprocessing import encode_city, encode_day, encode_season

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------
st.set_page_config(
    page_title="AI Air Quality Intelligence",
    page_icon="🌿",
    layout="wide"
)

# --------------------------------------------------------
# Custom CSS
# --------------------------------------------------------
st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:700;
    color:#2ECC71;
}

.subtitle{
    font-size:17px;
    color:#BFC9CA;
}

.result-box{
    padding:22px;
    border-radius:16px;
    background:#101820;
    border:1px solid #1F618D;
}

.category{
    padding:10px 18px;
    border-radius:25px;
    color:white;
    font-weight:600;
    display:inline-block;
    margin-top:10px;
}

.good{background:#27AE60;}
.satisfactory{background:#2ECC71;}
.moderate{background:#F39C12;}
.poor{background:#E67E22;}
.verypoor{background:#E74C3C;}
.severe{background:#8E44AD;}

footer{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# Header
# --------------------------------------------------------
st.markdown('<p class="main-title">🌿 AI Air Quality Intelligence</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Machine Learning based Air Quality Index (AQI) Prediction using Random Forest Regressor.</p>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------------
# Sidebar
# --------------------------------------------------------
st.sidebar.title("📊 Project Information")

st.sidebar.markdown("""
### Model Used
**Random Forest Regressor**

### Dataset
Air Quality Dataset (India)

### Features
17 Engineered Features

### Target Variable
Air Quality Index (AQI)
""")

st.sidebar.success(
    "Developed using Python, Scikit-learn, Streamlit and Plotly."
)

# --------------------------------------------------------
# Input Section
# --------------------------------------------------------
st.header("📍 Enter Air Pollution Details")

cities = [
    "Ahmedabad","Aizawl","Amaravati","Bengaluru","Bhopal",
    "Brajrajnagar","Chandigarh","Chennai","Coimbatore","Delhi",
    "Ernakulam","Gurugram","Guwahati","Hyderabad","Jaipur",
    "Jorapokhar","Kochi","Kolkata","Lucknow","Mumbai",
    "Patna","Shillong","Talcher","Thiruvananthapuram","Visakhapatnam"
]

left, right = st.columns(2)

with left:

    city = st.selectbox(
        "🏙 Select City",
        cities,
        index=13
    )

    selected_date = st.date_input(
        "📅 Select Date",
        value=date(2020,10,13)
    )

    season = st.selectbox(
        "🌤 Season",
        ["Winter","Summer","Monsoon","Post-Monsoon"]
    )

    day_name = selected_date.strftime("%A")

    st.markdown(f"**Day of Week:** {day_name}")

with right:

    PM25 = st.number_input("PM2.5",0.0,500.0,90.01)
    PM10 = st.number_input("PM10",0.0,600.0,120.03)
    NO = st.number_input("NO",0.0,200.0,14.04)
    NO2 = st.number_input("NO₂",0.0,300.0,28.02)
    NOx = st.number_input("NOx",0.0,500.0,40.02)

st.divider()

st.header("🧪 Additional Pollutants")

c1,c2 = st.columns(2)

with c1:
    NH3 = st.number_input("NH₃",0.0,300.0,18.00)
    CO = st.number_input("CO",0.0,20.0,1.20)
    SO2 = st.number_input("SO₂",0.0,300.0,21.00)

with c2:
    O3 = st.number_input("O₃",0.0,300.0,46.50)
    Benzene = st.number_input("Benzene",0.0,20.0,2.50)
    Toluene = st.number_input("Toluene",0.0,30.0,6.70)

st.divider()

# --------------------------------------------------------
# Prediction
# --------------------------------------------------------
if st.button("🚀 Predict Air Quality Index", use_container_width=True):

    city_encoded = encode_city(city)
    season_encoded = encode_season(season)
    day_encoded = encode_day(day_name)

    prediction = predict_aqi(
        PM25,PM10,NO,NO2,NOx,NH3,
        CO,SO2,O3,Benzene,Toluene,
        selected_date.year,
        selected_date.month,
        selected_date.day,
        city_encoded,
        season_encoded,
        day_encoded
    )

    prediction = round(float(prediction),2)

    category = get_aqi_category(prediction)

    st.success("Prediction completed successfully!")

    # AQI Progress Bar
    progress = min(prediction/500,1.0)
    st.progress(progress)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.subheader("🎯 Predicted AQI")

    st.metric("Air Quality Index", prediction)

    st.subheader("Air Quality Category")

    if category=="Good":
        style="good"

    elif category=="Satisfactory":
        style="satisfactory"

    elif category=="Moderate":
        style="moderate"

    elif category=="Poor":
        style="poor"

    elif category=="Very Poor":
        style="verypoor"

    else:
        style="severe"

    st.markdown(
        f'<div class="category {style}">{category}</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # ----------------------------------------------------
    # Health Recommendation
    # ----------------------------------------------------
    st.header("💡 Health Recommendation")

    if prediction <= 50:

        st.success("""
        **Good Air Quality**

        - Safe for outdoor activities.
        - Fresh air conditions.
        - No health risk for most people.
        """)

    elif prediction <=100:

        st.info("""
        **Satisfactory Air Quality**

        - Air quality is acceptable.
        - Sensitive individuals may experience mild discomfort.
        - Outdoor activities are generally safe.
        """)

    elif prediction <=200:

        st.warning("""
        **Moderate Air Quality**

        - Sensitive groups should reduce prolonged outdoor exposure.
        - Children and elderly should avoid strenuous outdoor exercise.
        - Consider wearing a mask during peak pollution hours.
        """)

    elif prediction <=300:

        st.warning("""
        **Poor Air Quality**

        - Limit outdoor activities.
        - Wear an N95 mask if staying outside.
        - Keep windows closed during heavy traffic hours.
        """)

    elif prediction <=400:

        st.error("""
        **Very Poor Air Quality**

        - Avoid outdoor activities whenever possible.
        - Use air purifiers indoors if available.
        - People with asthma or respiratory conditions should stay indoors.
        """)

    else:

        st.error("""
        **Severe Air Quality**

        - Stay indoors as much as possible.
        - Avoid physical activity outdoors.
        - Wear an N95/N99 mask if going outside.
        - Follow local air quality advisories.
        """)

# --------------------------------------------------------
# Footer
# --------------------------------------------------------
st.divider()

st.markdown("""
## 📘 About This Project

This application predicts the **Air Quality Index (AQI)** using a trained **Random Forest Regressor** model built on India's air pollution dataset.

### Project Workflow

- Data Understanding
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training & Evaluation
- Streamlit Application Development

**Tech Stack:** Python • Pandas • Scikit-learn • Streamlit • Plotly
""")