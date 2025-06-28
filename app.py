from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model/weather_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            temp = float(request.form["temperature"])
            humidity = float(request.form["humidity"])
            wind_speed = float(request.form["wind_speed"])

            input_features = np.array([[temp, humidity, wind_speed]])
            prediction = model.predict(input_features)[0]  # e.g., "Sunny"

            prediction_html = prediction.lower() + ".html"

            return render_template(prediction_html, 
                                   temperature=temp, 
                                   humidity=humidity, 
                                   wind_speed=wind_speed, 
                                   weather=prediction)
        except Exception as e:
            return f"⚠️ Error: {str(e)}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)