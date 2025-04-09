import streamlit as st

# Title
st.title("Sustainable Farming Assistant")

# Sidebar - Input data
st.sidebar.header("Input Parameters")

soil_type = st.sidebar.selectbox("Soil Type", ["Sandy", "Clay", "Loam"])
temp = st.sidebar.slider("Temperature (°C)", 10, 45, 25)
humidity = st.sidebar.slider("Humidity (%)", 10, 100, 50)
rainfall = st.sidebar.slider("Rainfall (mm)", 0, 300, 100)
growth_stage = st.sidebar.selectbox("Crop Growth Stage", ["Seeding", "Vegetative", "Flowering", "Harvest"])

# Agents' logic (simplified for demo)

def recommend_crop(soil, temp, humidity, rainfall):
    if soil == "Loam" and 20 <= temp <= 30 and rainfall > 50:
        return "Rice or Maize"
    elif soil == "Sandy" and temp > 30:
        return "Millets or Groundnut"
    else:
        return "Wheat or Barley"

def fertilizer_plan(stage):
    plans = {
        "Seeding": "Use Nitrogen-rich fertilizer",
        "Vegetative": "Apply balanced NPK",
        "Flowering": "Phosphorus and Potassium focused",
        "Harvest": "Minimal input, prepare for soil recovery"
    }
    return plans.get(stage, "No recommendation")

def market_prediction():
    return "Maize prices expected to rise next month"

def farmer_advice(crop, fert, market):
    return f"\n✅ Recommended Crop: {crop}\n\n✅ Fertilizer Advice: {fert}\n\n📈 Market Insight: {market}\n"

# Outputs
crop = recommend_crop(soil_type, temp, humidity, rainfall)
fert = fertilizer_plan(growth_stage)
market = market_prediction()
advice = farmer_advice(crop, fert, market)

st.subheader("Farming Advisor Output")
st.text(advice)

# Telegram Bot note
st.markdown("---")
st.markdown("👨‍🌾 Want this on your phone? Integrate this with a Telegram bot for real-time advice to farmers!")
