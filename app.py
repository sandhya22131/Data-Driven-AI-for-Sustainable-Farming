
import streamlit as st
import pandas as pd
import sqlite3
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ---------- Load Datasets ----------
farmer_df = pd.read_csv("farmer_advisor_dataset.csv")
market_df = pd.read_csv("market_researcher_dataset.csv")

# ---------- SQLite Setup ----------
conn = sqlite3.connect('sustainfarm.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    soil TEXT, temp REAL, humidity REAL, rainfall REAL,
    stage TEXT, region TEXT, budget REAL, crop TEXT,
    sustainability_score REAL, price_prediction REAL
)
''')
conn.commit()

# ---------- Farmer Advisor Agent ----------
def farmer_agent(soil, temp, humidity, rainfall, budget):
    X = farmer_df[['soil_type', 'temperature', 'humidity', 'rainfall', 'budget']]
    y = farmer_df['recommended_crop']
    X_encoded = pd.get_dummies(X)
    model = RandomForestClassifier()
    model.fit(X_encoded, y)
    
    input_df = pd.DataFrame([{
        'soil_type': soil,
        'temperature': temp,
        'humidity': humidity,
        'rainfall': rainfall,
        'budget': budget
    }])
    input_encoded = pd.get_dummies(input_df).reindex(columns=X_encoded.columns, fill_value=0)
    predicted_crop = model.predict(input_encoded)[0]
    return predicted_crop

# ---------- Market Researcher Agent ----------
def market_agent(crop, region="default", season="Rabi"):
    X = market_df[['crop', 'region', 'season']]
    y = market_df['price']
    X_encoded = pd.get_dummies(X)
    model = LinearRegression()
    model.fit(X_encoded, y)

    input_df = pd.DataFrame([{'crop': crop, 'region': region, 'season': season}])
    input_encoded = pd.get_dummies(input_df).reindex(columns=X_encoded.columns, fill_value=0)
    predicted_price = model.predict(input_encoded)[0]
    return predicted_price

# ---------- Sustainability Score ----------
def calculate_sustainability(crop, rainfall, water_needed_avg=100):
    # Lower water crops and suitable rainfall = better score
    water_penalty = abs(water_needed_avg - rainfall) / water_needed_avg
    soil_score = 1 if crop in ["Millets", "Sorghum", "Pulses"] else 0.5
    return max(0.1, round((1 - water_penalty) * soil_score, 2))

# ---------- Fertilizer Plan ----------
def fertilizer_plan(stage):
    plans = {
        "Seeding": "Use Nitrogen-rich fertilizer",
        "Vegetative": "Apply balanced NPK",
        "Flowering": "Phosphorus and Potassium focused",
        "Harvest": "Minimal input, prepare for soil recovery"
    }
    return plans.get(stage, "No recommendation")

# ---------- Streamlit Interface ----------
st.title("🌾 Data-Driven AI for Sustainable Farming")
st.markdown("Developed using a Multi-Agent Framework with SQLite Memory")

st.sidebar.header("Farmer Input")
soil_type = st.sidebar.selectbox("Soil Type", sorted(farmer_df['soil_type'].unique()))
temp = st.sidebar.slider("Temperature (°C)", 10, 45, 25)
humidity = st.sidebar.slider("Humidity (%)", 10, 100, 50)
rainfall = st.sidebar.slider("Rainfall (mm)", 0, 300, 100)
growth_stage = st.sidebar.selectbox("Crop Growth Stage", ["Seeding", "Vegetative", "Flowering", "Harvest"])
region = st.sidebar.selectbox("Region", sorted(market_df['region'].unique()))
budget = st.sidebar.slider("Budget (₹)", 1000, 50000, 15000)

# ---------- Agents Execution ----------
predicted_crop = farmer_agent(soil_type, temp, humidity, rainfall, budget)
predicted_price = market_agent(predicted_crop, region)
sustainability_score = calculate_sustainability(predicted_crop, rainfall)
fertilizer_advice = fertilizer_plan(growth_stage)

# ---------- Store to SQLite ----------
cursor.execute('''
    INSERT INTO logs (soil, temp, humidity, rainfall, stage, region, budget, crop, sustainability_score, price_prediction)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (soil_type, temp, humidity, rainfall, growth_stage, region, budget, predicted_crop, sustainability_score, predicted_price))
conn.commit()

# ---------- Output Display ----------
st.subheader("🧠 AI Multi-Agent Recommendations")
st.markdown(f"""
✅ *Recommended Crop:* {predicted_crop}  
💧 *Sustainability Score:* {sustainability_score} (Higher = More Eco-Friendly)  
🧪 *Fertilizer Plan:* {fertilizer_advice}  
📈 *Expected Market Price:* ₹{predicted_price:.2f}
""")

# ---------- History Viewer ----------
with st.expander("📜 View Past Recommendations"):
    logs = pd.read_sql_query("SELECT * FROM logs ORDER BY id DESC LIMIT 10", conn)
    st.dataframe(logs)

# ---------- Footer ----------
st.markdown("---")
st.markdown("🧑‍🌾 Integrate with Telegram for real-time farmer assistance. Use Ollama for LLM reasoning layer."

