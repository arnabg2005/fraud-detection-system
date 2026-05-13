# Fraud Detection Prediction App

A Streamlit-based web application for predicting fraudulent transactions using machine learning.

## Features

- Interactive web interface for entering transaction details
- Real-time fraud prediction using a pre-trained machine learning model
- Support for different transaction types (PAYMENT, TRANSFER, CASH_OUT, DEPOSIT)
- Visual feedback with color-coded results (red for fraud, green for legitimate)

## Project Structure

```
.
├── fraud_detection.py          # Main Streamlit application
├── fraud_detection_pipeline.pkl  # Pre-trained ML model
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fraud-detection-app.git
cd fraud-detection-app
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run fraud_detection.py
```

2. Open your web browser and navigate to:
```
http://localhost:8501
```

3. Enter the transaction details:
   - Select transaction type
   - Enter amount
   - Enter old and new balances for sender and receiver

4. Click the "Predict" button to get the fraud prediction result.

## Model Information

The application uses a pre-trained machine learning model (`fraud_detection_pipeline.pkl`) to classify transactions as fraudulent or legitimate. The model was trained on historical transaction data and considers features such as:

- Transaction type
- Transaction amount
- Old and new balances (sender and receiver)

## Dependencies

- streamlit >= 1.28.0
- pandas >= 2.0.0
- joblib >= 1.3.0
- scikit-learn >= 1.3.0
- numpy >= 1.24.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Thanks to the Streamlit team for the amazing web app framework
- Thanks to the scikit-learn team for the machine learning tools
