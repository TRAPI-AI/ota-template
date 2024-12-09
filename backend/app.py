from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

DUFFEL_API_KEY = os.getenv('DUFFEL_API_KEY')

@app.route('/duffel-flights-list-offers', methods=['POST'])
def duffel_flights_list_offers():
    url = 'https://api.duffel.com/air/offer_requests'
    headers = {
        "Accept-Encoding": "gzip",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Duffel-Version": "v2",
        "Authorization": f"Bearer {DUFFEL_API_KEY}"
    }
    data = request.get_json()
    response = requests.post(url, headers=headers, json=data)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(port=5000)