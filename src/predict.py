import pandas as pd
import joblib

# Load model and scaler
rf_model = joblib.load("models/best_aqi_model.pkl")
scaler = joblib.load("models/aqi_scaler.pkl")

# Feature names (same order used during training)
FEATURE_COLUMNS = [
    "PM2.5", "PM10", "NO", "NO2", "NOx", "NH3",
    "CO", "SO2", "O3", "Benzene", "Toluene",
    "Year", "Month", "Day",
    "City_Encoded", "Season_Encoded", "DayOfWeek_Encoded"
]

def predict_aqi(
    pm25, pm10, no, no2, nox, nh3,
    co, so2, o3, benzene, toluene,
    year, month, day,
    city_encoded, season_encoded, day_encoded
):

    # Create DataFrame with feature names
    input_df = pd.DataFrame([[
        pm25, pm10, no, no2, nox, nh3,
        co, so2, o3, benzene, toluene,
        year, month, day,
        city_encoded, season_encoded, day_encoded
    ]], columns=FEATURE_COLUMNS)

    # Scale features
    input_scaled = scaler.transform(input_df)

    # Predict AQI
    prediction = rf_model.predict(input_scaled)[0]

    return round(float(prediction), 2)


def get_aqi_category(aqi):

    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"