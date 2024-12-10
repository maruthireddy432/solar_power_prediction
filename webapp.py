import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px


# loading model
with open('solar_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Streamlit UI Configuration
st.set_page_config(page_title="Power Prediction Generator", page_icon="⚡", layout="wide")

# Sidebar Configuration
with st.sidebar.header("🗂️ Navigation"):
    sidebar_options = [ "🧑‍💻 Prediction","💾 About"]
    selected_option = st.sidebar.radio("Select a Section", sidebar_options)
# st.sidebar.image("solar logo.png", use_column_width=True) 

def prediction(distance_to_solar_noon,temperature,wind_direction,wind_speed,sky_cover,visibility,humidity,average_wind_speed,average_pressure):

    data=pd.DataFrame({'distance-to-solar-noon':[distance_to_solar_noon],
          'temperature':[temperature],
          'wind-direction':[wind_direction],
          'wind-speed':[wind_speed],
          'sky-cover':[sky_cover],
          'visibility':[visibility],
          'humidity':[humidity],
          'average-wind-speed-(period)':[average_wind_speed],
          'average-pressure-(period)':[average_pressure]
          })

    return np.exp(loaded_model.predict(data))


if selected_option=='🧑‍💻 Prediction':
   # Title
    st.markdown("<h1 style='color: orange; text-align: center;'>🌞 Solar Power Prediction</h1>", unsafe_allow_html=True)
    # Description
    st.markdown("<h2> Welcome to the Solar Power Prediction Dashboard!</h2>",unsafe_allow_html=True)
    st.markdown("<h5>Use this tool to predict solar power generation based on weather data.</h5>",unsafe_allow_html=True) 

    distance_to_solar_noon=float(st.number_input(label='Enter the Distance to solar noon',min_value=0.0,max_value=10.0))
    temperature=st.number_input(label='Enter the Temprature',min_value=40,max_value=80)
    wind_direction=st.number_input(label='Enter the Wind direction',min_value=20,max_value=35)
    wind_speed=st.number_input(label='Enter the Wind Speed ',min_value=1,max_value=23)
    sky_cover=st.slider("select sky Cover value",0,4)
    st.text(f'Selected:{sky_cover}')
    visibility=st.number_input(label='Enter the Visibility',min_value=7,max_value=10)
    humidity= st.number_input(label='Enter the Humiditity value',min_value=36,max_value=100)
    average_wind_speed=st.number_input(label='Enter the Average Wind Speed value',min_value=0,max_value=30)
    average_pressure=st.number_input(label='Enter the Average Pressure Value',min_value=25,max_value=32)

    if st.button("Predict"):
        result=prediction(distance_to_solar_noon,temperature,wind_direction,wind_speed,sky_cover,visibility,humidity,average_wind_speed,average_pressure)
        st.success(f'Prediction: {np.round(result[0])} joules')



if selected_option=="💾 About":
    # loading dataset
    df=pd.read_csv('solarpowergeneration.csv')
    # loading metrics df
    metrics=pd.read_excel('metrics.xlsx')

    # About Section
    st.title(":orange[About]")
    st.markdown(
        """
        ### Solar Power Prediction Dashboard
        This app provides accurate **solar power predictions** based on weather data using advanced **machine learning models**.  
        
        #### Model Description:
        - A XGBoost regression model is utilized to forecast power generation.
        - The model incorporates feature importance and early stopping techniques to optimize performance and prevent overfitting.
        - It performs very well and gives atmost accuracy.
        - You can find the data set and relevant model metrics below. 


        #### Key Features:
        - Upload weather information to generate predictions.
        - Get the accurate power output.
        - Examine datset used to train the model.
        - Diferent plots and metrics are avaliable.

        #### Use Cases:
        - **Solar Farm Operators**: Optimize energy output and resource planning.
        - **Energy Analysts**: Gain insights into renewable energy trends.
        - **Research**: Study the impact of weather patterns on solar generation.

        #### Built With:
        - Python 🐍
        - Streamlit 🌟
        - Machine Learning 🤖

        *Empowering clean energy with data-driven solutions!* ☀️⚡
        """
    )
    options = ['Select option','Data set', 'Visualization', 'Metrics']
    # dropdown menu
    selected_option = st.selectbox('Click Here For more:', options)
    # Display the selected option
    if selected_option=='Data set':
        # Display dataframe
        st.title(" :orange[Dataset]")
        st.markdown('''
        ### 📊 Dataset Overview
        - Distance to Solar Noon: Time difference from solar noon in hours.
        - Temperature: Ambient temperature (°F).
        - Wind Direction & Speed: Direction and speed of wind.
        - Sky Cover: Cloud cover index.
        - Visibility: Distance to the visible horizon (miles).
        - Humidity: Atmospheric humidity (%).
        - Average Wind Speed: Average wind speed during the period (mph).
        - Average Pressure: Average atmospheric pressure during the period (inHg).
                    ''')
        st.dataframe(df, use_container_width=True)
    if selected_option== 'Visualization':
        # Display plots
        st.title(" :orange[Interactive Histograms]")
        for column in df.columns:
            fig = px.histogram(df, x=column, title=f"{column} Distribution")
            st.plotly_chart(fig)
    if selected_option=='Metrics':
        # Display metrics
        st.title(" :orange[Metrics of Different Models]" )
        st.dataframe(metrics)  
