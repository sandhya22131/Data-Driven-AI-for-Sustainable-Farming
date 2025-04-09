import streamlit as st

# Page Config
st.set_page_config(page_title="Sustainable Farming AI", layout="wide")

st.title("🌾 Data-Driven AI for Sustainable Farming")
st.markdown("Leverage real-time data to optimize crop yield, irrigation, and sustainability.")

# Sidebar for sensor inputs
st.sidebar.header("🌿 Input Sensor Readings")
temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 26)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 60)
soil_moisture = st.sidebar.slider("Soil Moisture (%)", 0, 100, 40)
rainfall = st.sidebar.slider("Rainfall (mm)", 0, 300, 80)
ph_level = st.sidebar.slider("Soil pH", 3.0, 10.0, 6.5)

crop = st.sidebar.selectbox("Choose Crop", ["Wheat", "Rice", "Maize", "Tomato", "Onion", "Potato"])
auto_irrigation = st.sidebar.checkbox("Auto-Irrigation Enabled", value=True)

# Data summary
st.subheader("📊 Sensor Data Summary")
col1, col2, col3 = st.columns(3)
col1.metric("🌡️ Temperature", f"{temperature} °C")
col2.metric("💧 Soil Moisture", f"{soil_moisture}%")
col3.metric("☁️ Humidity", f"{humidity}%")

col4, col5 = st.columns(2)
col4.metric("🌧️ Rainfall", f"{rainfall} mm")
col5.metric("🧪 Soil pH", f"{ph_level}")

st.markdown("---")

# Decision Logic
st.subheader("🧠 AI Recommendation System")
if soil_moisture < 30:
    st.warning("⚠️ Low soil moisture. Irrigation required.")
    if auto_irrigation:
        st.success("✅ Auto-Irrigation Activated.")
else:
    st.success("Soil moisture is sufficient. No irrigation needed.")

if ph_level < 5.5 or ph_level > 7.5:
    st.error("⚠️ Soil pH not optimal. Consider soil treatment.")
else:
    st.info("Soil pH is within optimal range.")

if temperature > 40:
    st.error("🔥 Temperature too high. Provide shade or water spray.")
elif temperature < 10:
    st.warning("❄️ Temperature too low. Crop risk due to cold.")

# Simple yield prediction (mock logic)
def estimate_yield(temp, humidity, moisture, rain):
    if 20 <= temp <= 35 and 50 <= humidity <= 80 and 30 <= moisture <= 70 and 50 <= rain <= 150:
        return "High Yield Expected"
    elif 15 <= temp <= 40 and 40 <= humidity <= 90:
        return "Moderate Yield Expected"
    else:
        return "Low Yield Expected"

st.markdown(f"### 🌱 Predicted Yield for {crop}: **{estimate_yield(temperature, humidity, soil_moisture, rainfall)}**")

# Visualization
st.subheader("📈 Environmental Data Trends")
sensor_data = {
    "Temperature (°C)": [temperature-2, temperature, temperature+1],
    "Humidity (%)": [humidity-5, humidity, humidity+3],
    "Soil Moisture (%)": [soil_moisture-4, soil_moisture, soil_moisture+5],
    "Rainfall (mm)": [rainfall-10, rainfall, rainfall+5],
}
st.line_chart(sensor_data)

# Bar chart
st.subheader("📊 Crop Growth Factors (Simulated)")
st.bar_chart({
    "Growth Factor": [temperature, humidity, soil_moisture, rainfall, ph_level*10]
})

st.markdown("---")
st.caption("🔒 Powered by Streamlit | AI-Driven Farming Dashboard | © 2025")


