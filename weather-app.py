# import streamlit as st
# import requests
# import altair as alt
# import pandas as pd

# # OpenWeather API Key
# API_KEY = "PASTE YOUR API KEY HERE.." #CHECK README FILE FOR MORE DETAILS.
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# # Streamlit UI
# st.title("🌤 Weather App")
# st.write("Enter a city name to get current weather details with visualizations.")

# # User input for city
# city = st.text_input("Enter city name", "")

# if st.button("Get Weather"):
#     if city:
#         params = {"q": city, "appid": API_KEY, "units": "metric"}
#         response = requests.get(BASE_URL, params=params)

#         if response.status_code == 200:
#             data = response.json()
#             st.success(f"Weather in {data['name']}, {data['sys']['country']}:")

#             # Extracting weather details
#             temperature = data['main']['temp']
#             feels_like = data['main']['feels_like']
#             humidity = data['main']['humidity']
#             wind_speed = data['wind']['speed']

#             # Display text info
#             st.write(f"🌡 **Temperature**: {temperature}°C")
#             st.write(f"🤔 **Feels Like**: {feels_like}°C")
#             st.write(f"💧 **Humidity**: {humidity}%")
#             st.write(f"🌬 **Wind Speed**: {wind_speed} m/s")
#             st.write(f"🌦 **Condition**: {data['weather'][0]['description'].capitalize()}")

#             # Create Data for Visualization
#             weather_data = pd.DataFrame({
#                 "Parameter": ["Temperature (°C)", "Feels Like (°C)", "Humidity (%)", "Wind Speed (m/s)"],
#                 "Value": [temperature, feels_like, humidity, wind_speed]
#             })

#             # Altair Bar Chart
#             chart = alt.Chart(weather_data).mark_bar().encode(
#                 x="Parameter",
#                 y="Value",
#                 color="Parameter"
#             ).properties(
#                 width=600,
#                 height=400,
#                 title="Weather Parameters Visualization"
#             )

#             # Display Chart
#             st.altair_chart(chart, use_container_width=True)

#         else:
#             st.error("City not found. Please try again.")
#     else:
#         st.warning("Please enter a city name.")


import streamlit as st
import requests
import plotly.graph_objects as go

# OpenWeather API Key
API_KEY = "4a7e1b58e66ee9b0580e65ade4b176cc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Streamlit UI
st.title("🌤 Weather App")
st.write("Enter a city name to get current weather details with circular gauges.")

# User input for city
city = st.text_input("Enter city name", "")

if st.button("Get Weather"):
    if city:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            st.success(f"Weather in {data['name']}, {data['sys']['country']}:")

            # Extract weather data
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Create Circular Gauge Charts
            fig_temp = go.Figure(go.Indicator(
                mode="gauge+number",
                value=temperature,
                title={'text': "Temperature (°C)"},
                gauge={'axis': {'range': [-10, 50]}, 'bar': {'color': "blue"}}
            ))

            fig_humidity = go.Figure(go.Indicator(
                mode="gauge+number",
                value=humidity,
                title={'text': "Humidity (%)"},
                gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "orange"}}
            ))

            fig_wind = go.Figure(go.Indicator(
                mode="gauge+number",
                value=wind_speed,
                title={'text': "Wind Speed (m/s)"},
                gauge={'axis': {'range': [0, 20]}, 'bar': {'color': "green"}}
            ))

            # Display Charts in Columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.plotly_chart(fig_temp)
            with col2:
                st.plotly_chart(fig_humidity)
            with col3:
                st.plotly_chart(fig_wind)

        else:
            st.error("City not found. Please try again.")
    else:
        st.warning("Please enter a city name.")
