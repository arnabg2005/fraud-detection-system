"""
Configuration settings for the Fraud Detection application.
"""

import os

# Application Settings
APP_NAME = "Fraud Detection Prediction App"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "A Streamlit-based web application for predicting fraudulent transactions using machine learning."

# Model Settings
MODEL_PATH = "fraud_detection_pipeline.pkl"
MODEL_NAME = "Fraud Detection Pipeline"

# Transaction Types
TRANSACTION_TYPES = ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT']

# Default Values for Input Fields
DEFAULT_VALUES = {
    'amount': 1000.0,
    'oldbalanceOrg': 10000.0,
    'newbalanceOrig': 9000.0,
    'oldbalanceDest': 0.0,
    'newbalanceDest': 0.0
}

# UI Text
UI_TEXT = {
    'title': "Fraud Detection Prediction App",
    'description': "Please enter the transaction details and use the predict button",
    'transaction_type_label': "Transaction Type",
    'amount_label': "Amount",
    'oldbalanceOrg_label': "Old Balance (Sender)",
    'newbalanceOrig_label': "New Balance (Sender)",
    'oldbalanceDest_label': "Old Balance (Receiver)",
    'newbalanceDest_label': "New Balance (Receiver)",
    'predict_button': "Predict",
    'prediction_label': "Prediction",
    'fraud_message': "This transaction can be fraud",
    'legitimate_message': "This transaction look like its not a fraud"
}

# File Paths
DATA_DIR = "data"
NOTEBOOKS_DIR = "notebooks"
IMAGES_DIR = "images"

# Check if model file exists
def check_model_exists():
    """Check if the model file exists."""
    return os.path.exists(MODEL_PATH)

# Create necessary directories if they don't exist
def create_directories():
    """Create necessary directories if they don't exist."""
    directories = [DATA_DIR, NOTEBOOKS_DIR, IMAGES_DIR]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
