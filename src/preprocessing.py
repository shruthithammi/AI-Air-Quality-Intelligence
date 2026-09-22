
"""
Preprocessing utilities for AQI Prediction App.
"""

# City Encoding (same mapping used during training)
city_mapping = {
    "Ahmedabad": 0,
    "Aizawl": 1,
    "Amaravati": 2,
    "Bengaluru": 3,
    "Bhopal": 4,
    "Brajrajnagar": 5,
    "Chandigarh": 6,
    "Chennai": 7,
    "Coimbatore": 8,
    "Delhi": 9,
    "Ernakulam": 10,
    "Gurugram": 11,
    "Guwahati": 12,
    "Hyderabad": 13,
    "Jaipur": 14,
    "Jorapokhar": 15,
    "Kochi": 16,
    "Kolkata": 17,
    "Lucknow": 18,
    "Mumbai": 19,
    "Patna": 20,
    "Shillong": 21,
    "Talcher": 22,
    "Thiruvananthapuram": 23,
    "Visakhapatnam": 24
}

season_mapping = {
    "Winter": 3,
    "Summer": 2,
    "Monsoon": 0,
    "Post-Monsoon": 1
}

day_mapping = {
    "Monday": 1,
    "Tuesday": 5,
    "Wednesday": 6,
    "Thursday": 4,
    "Friday": 0,
    "Saturday": 2,
    "Sunday": 3
}


def encode_city(city):
    return city_mapping[city]


def encode_season(season):
    return season_mapping[season]


def encode_day(day):
    return day_mapping[day]