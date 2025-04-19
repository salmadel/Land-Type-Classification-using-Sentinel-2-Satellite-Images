# 🌍 GeoLens : Land-Type Classification Using Sentinel-2 Satellite Images
## Project Overview
**GeoLens** is an AI-driven web platform that utilizes **Convolutional Neural Networks (CNNs)** to classify land cover types from high-resolution Sentinel-2 satellite images. The system accurately identifies one of ten predefined land types—such as forest, water bodies, residential zones, and crop fields—based on RGB imagery.

In addition to land classification, GeoLens enhances user experience by integrating a **search agent (via SerpAPI)** that fetches real-time resources and reports related to the predicted land type. Furthermore, if geographic coordinates are available, the platform displays an **interactive map** showing the location of the uploaded image.

By combining deep learning with intelligent search and geospatial visualization, GeoLens provides a powerful and accessible tool for applications in **environmental monitoring**, **urban planning**, **agriculture**, and **disaster management**.

## Project Objectives
• **Environmental Monitoring:** Detect land cover changes, deforestation, and ecosystem shifts.

• **Urban Planning:** Monitor urban expansion and support infrastructure optimization.

• **Agriculture Management:** Identify crop types and assess farmland conditions.

• **Disaster Response:** Evaluate affected areas to enhance recovery planning.

• **Automation:** Deliver fast, scalable, and accurate land classification through deep learning.

## Team Members
**1. Dr/** [Mohamed Elsayed Nassar](https://github.com/Mohamed-Nassar88)

**2. Dr/** [Amal Adel Sheta](https://github.com/DrAmalSheta)

**3. Eng/** [Ahmed Hamdy Kandil](https://github.com/AhmedKandil2014)

**4. Eng/** Yara Saeed Abdelfadil

**5. Eng/** [Salma Adel Saleh](https://github.com/salmadel)

## Dataset
• [Dataset Link](https://zenodo.org/records/7711810#.ZAm3k-zMKEA)

• **Source:** Sentinel-2 RGB satellite images

• **Total Images:** 27,000

• **Image Resolution:** 64x64 pixels (RGB)

• **Classes (10):** Forest, Residential, Herbaceous Vegetation, Sea Lake, Annual Crop, Industrial, River, Highway, Permanent Crop, Pasture

• **Balanced Distribution:** No corrupt or duplicated images

• **Image Samples:**
![download (5)](https://github.com/user-attachments/assets/76a77590-77a7-4f5d-8124-35e1ae293458)


## Project Workflow
**1. Data Collection & Exploration**

• Collected and analyzed 27,000 Sentinel-2 RGB satellite images.

• Used EDA to visualize patterns and dataset characteristics.

**2. Data Preprocessing**

• Normalized image pixel values.

• Split dataset into training (70%), testing (20%), and validation (10%).

**3. Model Development & Training**

• Built and evaluated multiple **CNN** architectures using **TensorFlow/Keras**.

• Trained using the **Adam optimizer** with **categorical cross-entropy loss** and **early stopping**.

• Selected the best-performing model based on accuracy and F1-score.

**4. Model Deployment**

• Deployed the trained model in a **Flask-based** platform.

• Designed an interactive UI with **HTML**, **CSS**, and **JavaScript**.

• Displayed predicted land type with a confidence percentage.

**5. Search Agent Integration**

• Integrated **SerpAPI** to fetch 2–3 relevant online resources based on the predicted class.

• Helps users explore more about the detected land type.

**6. Map Visualization**

• Integrated **Leaflet.js** for dynamic map rendering.

• Displayed image location on the map using geographic coordinates, if available.

## Used Technologies
• **Python:** ML & backend logic

• **OpenCV:** Image handling

• **Flask:** Web app backend

• **TensorFlow/Keras:** CNN training

• **HTML/CSS/JS:** Frontend interface

• **SerpAPI:** Google search agent integration

• **Leaflet.js:** Map rendering from coordinates

• **NumPy, Pandas, Matplotlib, Seaborn:** Data analysis & visualization

## Results
After extensive training and evaluation, the best-performing model achieved:

• **Test Accuracy:** 97.09%

• **Loss:** 0.03

• **Precision, Recall, F1-Score:** ~97% across all metrics

![best normalize cm](https://github.com/user-attachments/assets/104b7945-5c49-4957-a51c-f40d96bd71c2)
![best curves](https://github.com/user-attachments/assets/78bc3a9e-d126-4399-8738-17848d72f699)


## User Interface Test




https://github.com/user-attachments/assets/dff2cba5-9217-48bc-957f-6778ad7a2ad5



## License
• **Dataset License**

The Sentinel-2 satellite imagery used in this project is freely available under EU law [(Copernicus Sentinel Data Terms and Conditions)](https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice). Please ensure compliance with these terms when using the data.


 • **Code License**
 
 The code used to process and classify the Sentinel-2 data is licensed under the MIT License, which allows you to freely use, modify, and distribute the code, as long as you include the copyright notice.



