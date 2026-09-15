from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Weather API"

@app.route("/weather")
def weather():
    city = request.args.get("city")
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    
    geocoding_params = {
        "name": city,
        "count": 1
    }
    
    geocoding_response = requests.get(
        geocoding_url,
        params=geocoding_params
    )
    
    geocoding_data = geocoding_response.json()
    
    if "results" not in geocoding_data:
        return {
            "error": "都市が見つかりませんでした"
        }, 404
    
    latitude = geocoding_data["results"][0]["latitude"]
    longitude = geocoding_data["results"][0]["longitude"]
    
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    temperature = data["current"]["temperature_2m"]
    
    return {
        "temperature": temperature
    }

if __name__ == "__main__":
    app.run(debug=True)