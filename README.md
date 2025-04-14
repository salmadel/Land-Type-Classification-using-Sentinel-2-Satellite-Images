# Land-Type-Classification-using-Sentinel-2-Satellite-Images (GeoLens Platform)
## Project Overview
**GeoLens** is an end-to-end AI platform designed to classify land types using Sentinel-2 satellite imagery and assist users through an AI-powered chatbot. The system combines **Convolutional Neural Networks (CNNs)** for image classification and **Natural Language Processing (NLP)** for real-time user interaction and support.

By analyzing high-resolution RGB satellite images, GeoLens can distinguish between 10 distinct land cover categories such as forests, urban zones, water bodies, and crop types.

GeoLens supports applications in environmental monitoring, urban planning, agriculture, and disaster response, making land analysis fast, interactive, and accessible.

## Project Objectives
• **Environmental Monitoring:** Detect land cover changes and deforestation.

• **Urban Planning:** Track urban expansion and optimize infrastructure.

• **Agriculture Management:** Identify crops and monitor farmland.

• **Disaster Response:** Assess damaged areas for better recovery planning.

• **AI Chatbot Assistance:** Provide interactive support and insights.

• **Automation:** Enable fast and scalable land classification.

## Team Members
**1. Dr/** [Mohamed Elsayed Nassar](https://github.com/Mohamed-Nassar88)

**2. Dr/** [Amal Adel Sheta](https://github.com/DrAmalSheta)

**3. Eng/** [Ahmed Hamdy Kandil](https://github.com/AhmedKandil2014)

**4. Eng/** Yara Saeed Abdelfadil

**5. Eng/** [Salma Adel Saleh](https://github.com/salmadel)

## Dataset
• **Source:** Sentinel-2 RGB satellite images

• **Total Images:** 27,000

• **Image Resolution:** 64x64 pixels (RGB)

• **Classes (10):** Forest, Residential, Herbaceous Vegetation, Sea Lake, Annual Crop, Industrial, River, Highway, Permanent Crop, Pasture

• **Balanced Distribution:** No corrupt or duplicated images

• [Dataset Link](https://zenodo.org/records/7711810#.ZAm3k-zMKEA)

• **Image Samples:**
![download (5)](https://github.com/user-attachments/assets/76a77590-77a7-4f5d-8124-35e1ae293458)


## Project Workflow
**1. Data Collection & Exploration**

• Collected Sentinel-2 satellite images and analyzed class distribution.

• Used EDA to visualize patterns and dataset characteristics.

**2. Data Preprocessing**

• Split data (Train 70%, Test 20%, Validation 10%).

• Normalized pixel values and applied data augmentation.

**3. Model Development & Training**

• Built and evaluated multiple **CNN** architectures using **TensorFlow/Keras**.

• Trained using the **Adam optimizer** with **categorical cross-entropy loss** and **early stopping**.

• Selected the best-performing model based on accuracy and F1-score.

**4. Model Deployment**

• Integrated the trained model into a **Flask-based** web app.

• Designed an interactive UI with **HTML**, **CSS**, and **JavaScript**.

• Enabled users to upload satellite images and receive instant land-type predictions along with a confidence score (%) for better interpretability.

**5. Chatbot Integration**

• Added a smart assistant using **LLaMA 3.2–3B-Instruct** for real-time user support.

• Helps users navigate the platform, understand results, and ask about land types and use cases.

## Used Technologies
• **Python:** Core logic and ML modeling

• **Flask:** Web server and integration

• **TensorFlow/Keras:** CNN training

• **OpenCV:** Image processing

• **HTML/CSS/JS:** Frontend

• **Hugging Face Transformers:** Chatbot NLP

• **NumPy, Pandas, Matplotlib, Seaborn:** Data analysis & visualization

## Results
After extensive training and evaluation, the best-performing model achieved:

• **Test Accuracy:** 97.09%

• **Loss:** 0.03

• **Precision, Recall, F1-Score:** ~97% across all metrics

![best normalize cm](https://github.com/user-attachments/assets/104b7945-5c49-4957-a51c-f40d96bd71c2)
![best curves](https://github.com/user-attachments/assets/78bc3a9e-d126-4399-8738-17848d72f699)


## User Interface Test



https://github.com/user-attachments/assets/81acb2e6-75dd-496b-8ac1-bd4ba7635da9

## License
• **Dataset License**

The Sentinel-2 satellite imagery used in this project is freely available under EU law [(Copernicus Sentinel Data Terms and Conditions)](https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice). Please ensure compliance with these terms when using the data.


 • **Code License**
 
 The code used to process and classify the Sentinel-2 data is licensed under the MIT License, which allows you to freely use, modify, and distribute the code, as long as you include the copyright notice.



