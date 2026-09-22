# MODEL DEPLOYMENT PREPARATION

After selecting the Random Forest Regressor as the best-performing model, the trained model and feature scaler are saved using Joblib. These saved files are reused during deployment to predict AQI for new user inputs without retraining the model.

The deployment phase includes:

- Loading the trained model (`best_aqi_model.pkl`).
- Loading the fitted feature scaler (`aqi_scaler.pkl`).
- Encoding categorical inputs such as City, Season, and Day of Week.
- Predicting AQI from real-time user inputs.
- Displaying the predicted AQI along with its corresponding air quality category.