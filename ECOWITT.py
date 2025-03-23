import streamlit as st
import requests

# --- Ecowitt API URL ---
url = "https://api.ecowitt.net/api/v3/device/real_time?application_key=777802CD9F85466F23B26776CD4F5248&api_key=ff02cabd-d15c-4044-9cc0-727c876627cf&mac=BC:FF:4d:f8:3d:76&call_back=all&temp_unitid=1&pressure_unitid=3&wind_speed_unitid=6&rainfall_unitid=12&solar_irradiance_unitid=16"

# --- Fetch Data ---
r = requests.get(url)
data = r.json()
outdoor = data.get("data", {}).get("outdoor", {})
barometer = data.get("data", {}).get("barometer", {})
wind = data.get("data", {}).get("wind", {})

# --- Display ---
st.title("🌤️ Live Weather Dashboard (Ecowitt)")

st.metric("🌡️ Temperature (°C)", outdoor.get("temperature", {}).get("value", "N/A"))
st.metric("💧 Humidity (%)", outdoor.get("humidity", {}).get("value", "N/A"))
st.metric("🌬️ Wind Speed (m/s)", wind.get("speed", {}).get("value", "N/A"))
st.metric("🌡️ Pressure (hPa)", barometer.get("value", "N/A"))
st.metric("☀️ Solar Irradiance (W/m²)", data.get("data", {}).get("solar", {}).get("radiation", {}).get("value", "N/A"))

st.line_chart({
    "Temperature (°C)": [outdoor.get("temperature", {}).get("value", 0)],
    "Humidity (%)": [outdoor.get("humidity", {}).get("value", 0)],
})
