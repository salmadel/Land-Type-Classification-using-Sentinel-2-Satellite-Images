# Land-Type-Classification-using-Sentinel-2-Satellite-Images
## Project Overview
This project aims to classify different land types using **Sentinel-2 satellite images** and **deep 
learning techniques**. By analyzing RGB satellite imagery, we can accurately identify various 
land cover types, such as forests, water bodies, urban areas, and agricultural land. This 
classification can help in environmental monitoring, urban planning, and sustainable resource 
management. Our model will be trained using **Convolutional Neural Networks (CNNs)** and 
pretrained architectures to achieve high accuracy and robustness.

## Project Objectives
• **Environmental Monitoring:** Tracks land cover changes over time, aiding in deforestation detection, climate change analysis, and natural disaster assessment.

• **Urban Planning:** Helps city planners analyze urban expansion and optimize land use for sustainable infrastructure development.

• **Agriculture Management:** Supports crop monitoring, identifies arable land, and enhances resource allocation to improve agricultural yield.

• **Disaster Response:** Provides critical insights for disaster management teams to assess affected areas and plan efficient recovery strategies.

• **Automation and Efficiency:** Reduces manual effort and enhances accuracy in land classification, enabling large-scale and cost-effective analysis.

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

• Split data (Train 70%, Validation 10%, Test 20%).

• Normalized pixel values and applied data augmentation.

• Resized images to 64×64 pixels.

**3. Model Development & Training**

• Built and trained multiple CNN models with regularization.

• Trained using the Adam optimizer with categorical cross-entropy loss and early stopping.

• Selected the best-performing model based on accuracy and F1-score.

**4. Model Deployment**

• Integrated the trained model into a Flask-based web app.

• Designed an interactive UI with HTML, CSS, and JavaScript.

## Used Technologies
**1. Programming Languages & Frameworks**

• **Python:** Used for data preprocessing, model training, and backend development.

• **Flask:** Lightweight web framework for deploying the CNN model.

• **JavaScript, HTML, CSS:** Used for frontend development and UI design.

**2. Libraries & Tools**

• **TensorFlow/Keras:** Deep learning framework for model development.

• **OpenCV:** Image processing and manipulation.

• **NumPy & Pandas:** Data handling and analysis.

• **Seaborn & Matplotlib:** Data visualization and exploratory analysis.

## Results
After extensive training and evaluation, the best-performing model achieved:

• **Test Accuracy:** 97.09%

• **Loss:** 0.03

• **Precision, Recall, F1-Score:** ~97% across all metrics

![best normalize cm](https://github.com/user-attachments/assets/104b7945-5c49-4957-a51c-f40d96bd71c2)
![best curves](https://github.com/user-attachments/assets/78bc3a9e-d126-4399-8738-17848d72f699)

## License

The dataset is licensed under the MIT license. In general, Sentinel data is free and open to the public under EU law. Please consider the [Copernicus Sentinel Data Terms and Conditions](https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice) when using Copernicus Sentinel data.

## User Interface Test



https://github.com/user-attachments/assets/2cfc7df1-12de-46ab-bdf3-519155fccc36



