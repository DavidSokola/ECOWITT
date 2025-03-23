import streamlit as st
import requests

# --- API URL ---
url = "https://api.ecowitt.net/api/v3/device/real_time?application_key=777802CD9F85466F23B26776CD4F5248&api_key=ff02cabd-d15c-4044-9cc0-727c876627cf&mac=BC:FF:4d:f8:3d:76&call_back=all&temp_unitid=1&pressure_unitid=3&wind_speed_unitid=6&rainfall_unitid=12&solar_irradiance_unitid=16"

# --- Fetch Data ---
r = requests.get(url)
data = r.json().get("data", {})

# --- Extract All Fields Safely ---
outdoor = data.get("outdoor", {})
indoor = data.get("indoor", {})
wind = data.get("wind", {})
pressure = data.get("pressure", {})
solar = data.get("solar_and_uvi", {}).get("solar", {})
uvi = data.get("solar_and_uvi", {}).get("uvi", {})
rain = data.get("rainfall", {})

# --- Streamlit Display ---
st.title("🌤️ Live Weather Dashboard (Ecowitt)")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🌡️ Outdoor Temp (°C)", outdoor.get("temperature", {}).get("value", "N/A"))
    st.metric("💧 Outdoor Humidity (%)", outdoor.get("humidity", {}).get("value", "N/A"))
    st.metric("🌡️ Dew Point (°C)", outdoor.get("dew_point", {}).get("value", "N/A"))

with col2:
    st.metric("🌬️ Wind Speed (m/s)", wind.get("wind_speed", {}).get("value", "N/A"))
    st.metric("💨 Wind Gust (m/s)", wind.get("wind_gust", {}).get("value", "N/A"))
    st.metric("🧭 Wind Direction (°)", wind.get("wind_direction", {}).get("value", "N/A"))

with col3:
    st.metric("📟 Pressure (hPa)", pressure.get("relative", {}).get("value", "N/A"))
    st.metric("☀️ Solar Irradiance (W/m²)", solar.get("value", "N/A"))
    st.metric("🔆 UVI", uvi.get("value", "N/A"))

st.markdown("---")
st.subheader("🌧️ Rainfall Stats")
st.write({
    "Hourly": rain.get("hourly", {}).get("value", "N/A"),
    "Daily": rain.get("daily", {}).get("value", "N/A"),
    "Weekly": rain.get("weekly", {}).get("value", "N/A"),
    "Monthly": rain.get("monthly", {}).get("value", "N/A"),
    "Yearly": rain.get("yearly", {}).get("value", "N/A"),
})

st.markdown("---")
st.subheader("🏠 Indoor Conditions")
st.metric("🌡️ Indoor Temp (°C)", indoor.get("temperature", {}).get("value", "N/A"))
st.metric("💧 Indoor Humidity (%)", indoor.get("humidity", {}).get("value", "N/A"))
