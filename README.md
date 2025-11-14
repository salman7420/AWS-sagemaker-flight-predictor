# End-to-End Flight Price Prediction with AWS SageMaker

This repository contains the source code for an end-to-end machine learning project that predicts flight prices using a real-world dataset of domestic Indian flights. The entire pipeline, from data preprocessing to model deployment, is orchestrated using **AWS SageMaker**, demonstrating a production-ready approach to cloud-based machine learning.

## 📑 Project Overview

The goal of this project is to predict flight prices based on various features such as departure/destination city, time of day, airline, and meal options. This project moves beyond a typical notebook-based analysis by implementing a full MLOps lifecycle within the AWS ecosystem.

## ✨ Key Features

*   **Comprehensive EDA:** In-depth exploratory data analysis to uncover insights and correlations within the flight data.
*   **Advanced Feature Engineering:** Creation of new, impactful features from raw data to improve model performance.
*   **Robust Model Training:** Implemented and compared multiple models, including a final **XGBoost Regressor**, with extensive hyperparameter tuning using SageMaker's built-in capabilities.
*   **Ensemble Learning:** Utilized ensemble techniques to combine model predictions, further boosting accuracy and robustness.
*   **End-to-End AWS SageMaker Pipeline:** The entire workflow is managed within SageMaker, including data processing jobs, EDA and training jobs, showcasing best practices used in industry.

## 🛠️ Technology Stack

*   **Cloud Platform:** Amazon Web Services (AWS)
*   **ML Service:** AWS SageMaker (for training, tuning, and deployment)
*   **Core Libraries:** Python, Scikit-learn, Pandas, NumPy, XGBoost
*   **Visualization:** Matplotlib, Seaborn
*   **Web Development:** Streamlit

## 🚀 Project Pipeline

1.  **Data Ingestion & EDA:** Data is loaded from S3, and a comprehensive EDA is performed in a SageMaker Notebook instance.
2.  **Feature Engineering:** A SageMaker Processing Job is used to run a Scikit-learn script that preprocesses the data and engineers new features.
3.  **Model Training & Tuning:** An XGBoost model is trained on the processed data. SageMaker's HyperparameterTuner is used to find the optimal model parameters.
4.  **Model Deployment:** Used Pickle to save and load the Model.

## 📫 Contact

Your Name - https://www.linkedin.com/in/salman-rasheed-ai/ - salmanrasheedsrk86@gmail.com

Project Link: https://github.com/salman7420/AWS-sagemaker-flight-predictor/tree/master
