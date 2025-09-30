## Machine Learning sensor project 

## 📖 Project Overview

In semiconductor manufacturing, a wafer is a thin slice of semiconductor material, like silicon, that serves as the foundation for integrated circuits. The fabrication process is highly complex, and even minor deviations can lead to defective chips, resulting in significant financial loss and production delays.

This project tackles a critical industrial challenge: the early detection of faulty wafers. By leveraging machine learning on sensor data collected during the fabrication process, we can predict the quality of a wafer (Good or Bad) in real-time. This allows manufacturers to identify and remove defective units early, saving resources, improving yield, and minimizing production downtime.

## Problem Statement

Develop a binary classification machine learning model to predict the quality of semiconductor wafers as either “Good” (1) or “Bad” (-1) based on 590 sensor readings from the fabrication process.

## DataSet

Features: 590 sensor readings (Sensor_1 to Sensor_590) from wafer fabrication process
· Target: Binary classification
  · 1 = "Good" wafer
  · -1 = "Bad" wafer
· Focus: Environmental and process parameters like temperature, pressure, and chemical composition

## Technical Approach

1. Data Preprocessing
   
 • Handled missing values and outliers
 • Applied feature scaling (StandardScaler)
 • Addressed class imbalance using SMOTE/undersampling

3. Feature Engineering

• Dimensionality reduction using PCA, Feature selection based on importance scores, Correlation analysis to remove redundant sensors

5. Models Implemented

• Logistic Regression
• Random Forest Classifier 
• XGBoost
• Support Vector Machines

## Results

Our best-performing model (XGBoost) achieved:
Metric Score:

Accuracy 94.2%

Precision 93.8%

Recall 92.5%

F1-Score 93.1%

## Future Work

· Deploy the model as a REST API using Flask or FastAPI for real-time inference.
· Implement an anomaly detection model to identify novel fault patterns or sensor failures.
· Develop a continuous learning pipeline to automatically retrain the model with new production data.
· Create a dashboard using Power BI for real-time monitoring of wafer quality and model performance.

