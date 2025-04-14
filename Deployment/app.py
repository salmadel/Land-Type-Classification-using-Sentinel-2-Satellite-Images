# Importing libraries
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import requests
from dotenv import load_dotenv
from tensorflow.keras.models import model_from_json

# Load environment variables
load_dotenv()

# Creating flask app
app = Flask(__name__)

# Hugging Face model connection
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct"

if not HUGGINGFACE_API_KEY:
    raise ValueError("ERROR: Hugging Face API key is missing. Check your .env file.")

# Loading model structure
try:
    with open("model.json", "r") as json_file:
        model_json = json_file.read()
    model = model_from_json(model_json)
    print("Model structure loaded successfully.")
except Exception as e:
    print(f"Error loading model structure: {e}")
    model = None

# Loading model weights
if model:
    try:
        model.load_weights("weights.keras")
        model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
        print("Weights loaded and model compiled successfully.")
    except Exception as e:
        print(f"Error loading weights: {e}")
        model = None

# Class labels
class_names = ["Annual Crop", "Forest", "Herbaceous Vegetation", "Highway", "Industrial",
               "Pasture", "Permanent Crop", "Residential", "River", "SeaLake"]

# Image preprocessing function
def preprocess_image(image):
    image = image.convert('RGB')  
    image = image.resize((64, 64))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded properly'}), 500

        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        image = Image.open(file)

        processed_image = preprocess_image(image)

        predictions = model.predict(processed_image)
        class_index = np.argmax(predictions)
        confidence = float(np.max(predictions))

        predicted_class = class_names[class_index]

        return jsonify({'prediction': predicted_class, 'confidence': confidence}), 200

    except Exception as e:
        return jsonify({'error': f'Error in prediction: {str(e)}'}), 500

# Chatbot API route
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Geospatial knowledge base context
        context = """
Forest: Areas covered with dense trees and vegetation.
Residential: Areas with houses and living communities.
Industrial: Zones used for factories and production.
River: Natural flowing water bodies.
Herbaceous Vegetation: Lands covered with small plants and shrubs.
Highway: Main roads used for transportation.
Sea/Lake: Large water bodies, either salt or fresh water.
Permanent Crop: Lands used for long-term crops like fruit trees.
Annual Crop: Fields used for seasonal crops like wheat.
Pasture: Grasslands used for grazing animals.
"""

        # Construct the prompt
        prompt = f"""You are a helpful assistant specialized in geospatial analysis and land classification. 
Answer briefly and clearly. Use the following information only if relevant:

{context}

Q: {user_message}
A:"""

        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 300,
                "temperature": 0.5,  
                "top_p": 0.8
            }
        }

        print("Sending request to Hugging Face API...")

        try:
            response = requests.post(
                f"https://api-inference.huggingface.co/models/{MODEL_NAME}",
                headers=headers,
                json=payload
            )
        except Exception as e:
            print(f"Error sending request to Hugging Face: {str(e)}")
            return jsonify({"error": f"Request failed: {str(e)}"}), 500

        print("Response received!")
        print("Raw Hugging Face response text:", response.text)

        if response.status_code != 200:
            return jsonify({"error": "API request failed", "details": response.text}), 500

        response_data = response.json()

        # Extract the generated answer
        if isinstance(response_data, list) and "generated_text" in response_data[0]:
            full_response = response_data[0]["generated_text"]
        elif isinstance(response_data, dict) and "generated_text" in response_data:
            full_response = response_data["generated_text"]
        else:
            full_response = "Sorry, I couldn't generate a response."

        # Clean the answer after "A:"
        bot_response = full_response.split("A:")[-1].strip()

        return jsonify({"response": bot_response}), 200

    except Exception as e:
        print(f"Chatbot error: {str(e)}")
        return jsonify({"error": f"Chatbot error: {str(e)}"}), 500

# Running flask app
if __name__ == '__main__':
    app.run(debug=True)
