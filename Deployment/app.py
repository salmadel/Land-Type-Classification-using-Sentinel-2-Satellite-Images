#Importing libraries
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io
from tensorflow.keras.models import model_from_json

#Creating flask app
app = Flask(__name__)

#Loading model structure
try:
    with open("model.json", "r") as json_file:
        model_json = json_file.read()
    model = model_from_json(model_json)
    print("Model structure loaded successfully.")
except Exception as e:
    print(f"Error loading model structure: {e}")
    model = None

#Loading model weights
if model:
    try:
        model.load_weights("weights.keras")
        model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
        print("Weights loaded and model compiled successfully.")
    except Exception as e:
        print(f"Error loading weights: {e}")
        model = None

#Class labels
class_names = ["Annual Crop", "Forest", "Herbaceous Vegetation", "Highway", "Industrial",
               "Pasture", "Permanent Crop", "Residential", "River", "SeaLake"]

#Image preprocessing function
def preprocess_image(image):
    image = image.convert('RGB')  
    image = image.resize((64, 64))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

#Homepage route
@app.route('/')
def home():
    return render_template('index.html')

#Prediction endpoint
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

#Running flask app
if __name__ == '__main__':
    app.run(debug=True)