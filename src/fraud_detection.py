import streamlit as st
import pandas as pd
import joblib
import os

def run_app():
    """Run the fraud detection Streamlit app."""
    
    # Load the model
    model_path = "fraud_detection_pipeline.pkl"
    if not os.path.exists(model_path):
        st.error(f"Model file '{model_path}' not found. Please ensure it exists in the project root.")
        return
    
    try:
        model = joblib.load(model_path)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return

    st.title("Fraud Detection Prediction App")
    st.markdown("Please enter the transaction details and use the predict button")
    st.divider()

    # Transaction type selection
    transction_type = st.selectbox("Transction Type ", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT'])

    # Input fields
    amount = st.number_input("Amount ", min_value=0.0, value=1000.0)
    oldbalanceOrg = st.number_input("Old Balance (Sender) ", min_value=1000.0, value=10000.0)
    newbalanceOrig = st.number_input("New Balance (Sender) ", min_value=1000.0, value=9000.0)
    oldbalanceDest = st.number_input("Old Balance (Receiver) ", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("New Balance (Receiver) ", min_value=0.0, value=0.0)

    if st.button("Predict"):
        input_data = pd.DataFrame([{
            "type": transction_type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest
        }])

        try:
            prediction = model.predict(input_data)[0]
            st.subheader(f"Prediction: {int(prediction)}")

            if prediction == 1:
                st.error("This transction can be fraud")
            else:
                st.success("This transction look like its not a fraud")
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")

if __name__ == "__main__":
    run_app()
