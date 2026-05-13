"""
Utility functions for the fraud detection application.
"""

import pandas as pd
import numpy as np

def validate_transaction_data(data):
    """
    Validate transaction data before prediction.
    
    Args:
        data (dict): Transaction data dictionary
        
    Returns:
        bool: True if data is valid, False otherwise
    """
    required_fields = ['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
    
    for field in required_fields:
        if field not in data:
            return False
    
    # Additional validation logic can be added here
    return True

def preprocess_transaction_data(data):
    """
    Preprocess transaction data for model prediction.
    
    Args:
        data (dict): Raw transaction data
        
    Returns:
        pd.DataFrame: Preprocessed data ready for prediction
    """
    # Convert to DataFrame
    df = pd.DataFrame([data])
    
    # Add any preprocessing steps here
    # For example, feature engineering, scaling, etc.
    
    return df

def format_prediction_result(prediction, probability=None):
    """
    Format prediction result for display.
    
    Args:
        prediction (int): Binary prediction (0 or 1)
        probability (float, optional): Prediction probability
        
    Returns:
        dict: Formatted result
    """
    result = {
        'is_fraud': bool(prediction),
        'message': "This transaction appears to be fraudulent" if prediction == 1 else "This transaction appears legitimate",
        'risk_level': "High" if prediction == 1 else "Low"
    }
    
    if probability is not None:
        result['confidence'] = f"{probability:.2%}"
    
    return result
