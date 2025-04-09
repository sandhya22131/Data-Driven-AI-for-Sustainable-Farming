import streamlit as st
import random
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Sustainable Farming Assistant", layout="wide")

# Custom CSS for improved aesthetics
st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1519682337058-a94d519337bc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80");
        background-size: cover;
    }
   [data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Introduction
st.title("🌾 Sustainable Farming Assistant")
st.markdown("<p class='big-font'>Empowering Farmers with AI and IoT for a Sustainable Future</p>", unsafe_allow_html=True)
st.markdown("Harnessing the power of AI and IoT to revolutionize farming practices, ensuring sustainability and increased yields.")

st.markdown("---")

# 1. Soil & Weather Monitoring Agent
st.header("1️⃣ Soil & Weather Monitoring Agent")

col1, col2 = st.columns(2)

with col1:
    soil_type = st.selectbox("Select Soil Type", ["Sandy", "Loamy", "Clay", "Silty"])
with col2:
    weather = st.selectbox("Current Weather", ["Sunny", "Rainy", "Cloudy", "Windy"])

if st.button("Recommend Crops Based on Soil & Weather"):
    crops = {
        "Sandy": ["Peanuts", "Watermelon", "Okra"],
        "Loamy": ["Wheat", "Sugarcane", "Corn"],
        "Clay": ["Rice", "Jute", "Soybeans"],
        "Silty": ["Soybean", "Cabbage", "Broccoli"]
    }
    recommended_crops = crops.get(soil_type, ['No data'])
    st.success(f"🌱 Recommended Crops: {', '.join(recommended_crops)}")

st.markdown("---")

# 2. Fertilizer & Water Optimization Agent
st.header("2️⃣ Fertilizer & Water Optimization Agent")

growth_stage = st.selectbox("Select Crop Growth Stage", ["Seedling", "Vegetative", "Flowering", "Harvest"])

if st.button("Optimize Inputs for Current Growth Stage"):
    water_usage = random.randint(5, 10)
    fertilizer_options = ['NPK 20-20-20', 'Urea', 'Compost', 'Organic Mix']
    fertilizer = random.choice(fertilizer_options)
    st.info(f"💧 Recommended Water Usage: {water_usage} liters/day\n\n🌱 Recommended Fertilizer: {fertilizer}")

st.markdown("---")

# 3. Market Prediction Agent
st.header("3️⃣ Market Prediction Agent")

# Sample market data (replace with real data)
market_data = {
    'Crop': ["Wheat", "Rice", "Corn", "Soybean", "Sugarcane"],
    'Price': [250, 180, 150, 300, 120],
    'Demand': [80, 90, 75, 85, 70]
}
market_df = pd.DataFrame(market_data)

# Normalize demand and price to create a combined score
market_df['Score'] = (market_df['Demand'] / 100) + (market_df['Price'] / market_df['Price'].max())
trending_crop = market_df.sort_values(by='Score', ascending=False).iloc[0]['Crop']

if st.button("Get Real-Time Market Insights"):
    st.success(f"📈 Highly Profitable Crop to Grow Now: **{trending_crop}**")

    # Interactive Market Trends Visualization
    fig = px.bar(market_df, x='Crop', y='Price', color='Demand',
                 title='Crop Prices and Demand',
                 labels={'Price': 'Price per Ton', 'Demand': 'Demand (Scale of 100)'})
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# 4. Farmer Advisory Agent
st.header("4️⃣ Farmer Advisory Agent")

language = st.selectbox("Select Preferred Language", ["English", "Hindi", "Tamil", "Telugu"])
question = st.text_input("Ask a farming-related question")

if st.button("Get Personalized Advice"):
    advice = f"Ensure regular irrigation and use organic compost during the vegetative stage for {trending_crop}."
    st.markdown(f"🗣️ In **{language}**: '{advice}'")

st.markdown("---")

# 5. IoT Sensor Integration (Simulated)
st.header("5️⃣ Simulated IoT Sensor Data")
st.markdown("Visualizing real-time data from IoT sensors for informed decision-making.")

# Sample IoT data (replace with actual sensor data)
sensor_data = {
    'Timestamp': pd.date_range(start='2025-07-22', periods=10, freq='H'),
    'Temperature': [28, 29, 30, 31, 30, 29, 28, 27, 26, 25],
    'Humidity': [60, 62, 63, 65, 64, 62, 61, 60, 59, 58],
    'Soil Moisture': [45, 46, 47, 48, 47, 46, 45, 44, 43, 42]
}
sensor_df = pd.DataFrame(sensor_data)
sensor_df = sensor_df.set_index('Timestamp')

# Display sensor data as a line chart
st.line_chart(sensor_df)

st.markdown("---")

# Sidebar for Contact and Additional Information
st.sidebar.header("📱 Contact via WhatsApp/Telegram")
st.sidebar.markdown("For real-time advice, connect with our AI agent:")
st.sidebar.markdown("[Join WhatsApp Bot](https://wa.me/1234567890)")
st.sidebar.markdown("[Join Telegram Bot](https://t.me/farm_assist_bot)")

st.sidebar.header("Additional Resources")
st.sidebar.markdown("[Learn More About Sustainable Farming](https://www.fao.org/sustainability/en/)")
st.sidebar.markdown("[Explore IoT in Agriculture](https://www.iotforall.com/iot-in-agriculture)")

# Footer
st.markdown("---")
st.caption("© 2025 Sustainable Farming Hackathon Project")

