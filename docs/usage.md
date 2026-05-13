# Usage Guide

## Getting Started

### Running the Application

1. **Using Streamlit directly:**
   ```bash
   streamlit run fraud_detection.py
   ```

2. **Using the main app entry point:**
   ```bash
   python app.py
   ```

3. **With virtual environment activated:**
   ```bash
   .venv\Scripts\activate
   streamlit run fraud_detection.py
   ```

### Accessing the App

Once running, open your web browser and navigate to:
- Local URL: http://localhost:8501

## Using the Application

### Step 1: Select Transaction Type
Choose from the dropdown:
- PAYMENT
- TRANSFER
- CASH_OUT
- DEPOSIT

### Step 2: Enter Transaction Details
Fill in the following fields:
- **Amount**: Transaction amount (minimum 0.0)
- **Old Balance (Sender)**: Sender's balance before transaction
- **New Balance (Sender)**: Sender's balance after transaction
- **Old Balance (Receiver)**: Receiver's balance before transaction
- **New Balance (Receiver)**: Receiver's balance after transaction

### Step 3: Get Prediction
Click the **"Predict"** button to get the fraud prediction result.

### Understanding Results

- **Prediction: 1** (Red alert): The transaction is likely fraudulent
- **Prediction: 0** (Green): The transaction appears legitimate

## Example Transactions

### Example 1: Legitimate Transfer
- Type: TRANSFER
- Amount: 5000.0
- Old Balance (Sender): 15000.0
- New Balance (Sender): 10000.0
- Old Balance (Receiver): 2000.0
- New Balance (Receiver): 7000.0

### Example 2: Suspicious Transaction
- Type: CASH_OUT
- Amount: 200000.0
- Old Balance (Sender): 50000.0
- New Balance (Sender): 0.0
- Old Balance (Receiver): 0.0
- New Balance (Receiver): 200000.0

## Troubleshooting

### Common Issues

1. **Model file not found**
   - Ensure `fraud_detection_pipeline.pkl` is in the project root directory

2. **Import errors**
   - Install required packages: `pip install -r requirements.txt`

3. **Streamlit not found**
   - Install streamlit: `pip install streamlit`

### Support

For additional help, please:
1. Check the README.md file
2. Open an issue on GitHub
3. Contact the maintainers
