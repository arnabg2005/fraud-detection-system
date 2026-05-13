"""
Test module for fraud detection application.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import validate_transaction_data, format_prediction_result

class TestFraudDetection(unittest.TestCase):
    """Test cases for fraud detection functions."""
    
    def test_validate_transaction_data_valid(self):
        """Test validation with valid data."""
        data = {
            'type': 'PAYMENT',
            'amount': 1000.0,
            'oldbalanceOrg': 10000.0,
            'newbalanceOrig': 9000.0,
            'oldbalanceDest': 0.0,
            'newbalanceDest': 0.0
        }
        self.assertTrue(validate_transaction_data(data))
    
    def test_validate_transaction_data_invalid(self):
        """Test validation with missing fields."""
        data = {
            'type': 'PAYMENT',
            'amount': 1000.0
            # Missing other required fields
        }
        self.assertFalse(validate_transaction_data(data))
    
    def test_format_prediction_result_fraud(self):
        """Test formatting for fraud prediction."""
        result = format_prediction_result(1)
        self.assertTrue(result['is_fraud'])
        self.assertEqual(result['risk_level'], 'High')
    
    def test_format_prediction_result_legitimate(self):
        """Test formatting for legitimate prediction."""
        result = format_prediction_result(0)
        self.assertFalse(result['is_fraud'])
        self.assertEqual(result['risk_level'], 'Low')

if __name__ == '__main__':
    unittest.main()
