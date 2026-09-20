from flask import Flask, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Weather API"

@app.route("/weather")
def weather():
    city = request.args.get("city")
    
    url = "https://api.weatherapi.com/v1/current.json"
       
    params = {
        "key": WEATHER_API_KEY,
        "q": city
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    print(data, flush=True)
    
    temperature = data["current"]["temp_c"]
    
    return {
        "temperature": temperature
    }

if __name__ == "__main__":
    app.run(debug=True)