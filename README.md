# 🌞 Solar Power Prediction 

# 🌟 Key Features
  - Accurate Predictions: Use weather parameters like temperature, wind speed, sky cover, etc., to predict solar power generation.
  - Dynamic Visualizations: View interactive plots of the dataset and model performance metrics.
  - Model Comparison: Analyze the metrics of different machine learning models used for prediction.
  - Data Exploration: Examine the dataset used for model training directly in the app.
# 📊 Dataset Overview
- The dataset includes the following features:
- Distance to Solar Noon: Time difference from solar noon in hours.
- Temperature: Ambient temperature (°F).
- Wind Direction & Speed: Direction and speed of wind.
- Sky Cover: Cloud cover index.
- Visibility: Distance to the visible horizon (miles).
- Humidity: Atmospheric humidity (%).
- Average Wind Speed: Average wind speed during the period (mph).
- Average Pressure: Average atmospheric pressure during the period (inHg).
# 🌐 How It Works
Model Input:
 - Users provide weather parameters like distance to solar noon, temperature, wind speed, sky cover, visibility, and humidity.
 - Machine Learning Model:
 - The pre-trained regression model (solar_model.pkl) processes the input and predicts the expected solar power generation.
 - Interactive Outputs:
  - Predictions are displayed instantly.
# 📂 Project Structure
- webapp.py                  # Main Streamlit app code
- solar_model.pkl         # Pre-trained machine learning model
- solarpowergeneration.csv# Dataset used for predictions
- metrics.xlsx            # Model performance metrics
# 🛠️ Technologies Used
- Python 🐍
- Streamlit 🌟
- Pandas for data manipulation
- Numpy for numerical computations
- Scikit-learn for model development
- Plotly and Seaborn for visualizations

