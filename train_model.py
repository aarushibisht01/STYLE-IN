import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

data_path = "data/synthetic_weather_data.csv"

if not os.path.exists(data_path):
    print("❌ Dataset not found. Please ensure 'synthetic_weather_data.csv' exists in the 'data/' folder.")
    exit()

df = pd.read_csv(data_path)

X = df[["temperature", "humidity", "wind_speed"]]
y = df["weather_label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

model_path = "model/weather_model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model trained and saved to {model_path}")
