
from src.predict import predict_aqi, get_aqi_category

predicted = predict_aqi(
    PM25=85,
    PM10=120,
    NO=12,
    NO2=28,
    NOx=35,
    NH3=18,
    CO=1.1,
    SO2=10,
    O3=42,
    Benzene=1.3,
    Toluene=3.2,
    Year=2020,
    Month=10,
    Day=15,
    City_Encoded=13,
    Season_Encoded=1,
    DayOfWeek_Encoded=4
)

print("Predicted AQI :", predicted)
print("AQI Category :", get_aqi_category(predicted))