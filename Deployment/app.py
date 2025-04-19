# Importing libraries
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from tensorflow.keras.models import model_from_json

# Load environment variables
load_dotenv()

# Flask app
app = Flask(__name__)

# Load coordinates CSV
coordinates_df = pd.read_csv("image_coordinates.csv")

# Load model
try:
    with open("model.json", "r") as json_file:
        model_json = json_file.read()
    model = model_from_json(model_json)
    print("Model structure loaded.")
except Exception as e:
    print(f"Error loading model structure: {e}")
    model = None

if model:
    try:
        model.load_weights("weights.keras")
        model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
        print("Model weights loaded and compiled.")
    except Exception as e:
        print(f"Error loading weights: {e}")
        model = None

# Class labels
class_names = ["Annual Crop", "Forest", "Herbaceous Vegetation", "Highway", "Industrial",
               "Pasture", "Permanent Crop", "Residential", "River", "SeaLake"]

# Image preprocessing
def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((64, 64))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

# Scraper agent to get related links
def search_land_info(query):
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        return []

    params = {
        "q": f"{query} land use",
        "api_key": api_key,
        "num": 3,
        "engine": "google"
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()
        links = []
        if "organic_results" in data:
            for result in data["organic_results"]:
                link = result.get("link")
                if link:
                    links.append(link)
                if len(links) >= 3:
                    break
        return links

    except Exception as e:
        print(f"Error fetching search results: {e}")
        return []

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500

        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        filename = file.filename
        image = Image.open(file)
        processed = preprocess_image(image)

        predictions = model.predict(processed)
        class_index = np.argmax(predictions)
        confidence = float(np.max(predictions))
        predicted_class = class_names[class_index]

        # Fetching links
        try:
            links = search_land_info(predicted_class)
        except Exception as e:
            print(f"Link error: {e}")
            links = []

        # Fetching coordinates
        try:
            coords = coordinates_df[coordinates_df["Image"] == filename]
            if not coords.empty:
                latitude = float(coords.iloc[0]["Latitude"])
                longitude = float(coords.iloc[0]["Longitude"])
            else:
                latitude = None
                longitude = None
        except Exception as e:
            print(f"Coordinates error: {e}")
            latitude = None
            longitude = None

        return jsonify({
            "prediction": predicted_class,
            "confidence": confidence,
            "related_links": links,
            "latitude": latitude,
            "longitude": longitude
        }), 200

    except Exception as e:
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

# Run server
if __name__ == "__main__":
    app.run(debug=True)