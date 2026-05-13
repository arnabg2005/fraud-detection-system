# System Architecture

## Overview

The Fraud Detection App is a Streamlit-based web application that uses machine learning to predict fraudulent transactions in real-time.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│                    (Streamlit Web App)                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   Input Processing Layer                     │
│         • Data Validation                                  │
│         • Feature Engineering                              │
│         • Data Transformation                              │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   Machine Learning Model                     │
│         • Pre-trained Pipeline                             │
│         • Real-time Prediction                             │
│         • Probability Scoring                              │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   Output Processing Layer                  │
│         • Result Formatting                                │
│         • Risk Assessment                                  │
│         • Visual Feedback                                  │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. User Interface Layer
- **Technology**: Streamlit
- **Purpose**: Provide an interactive web interface
- **Features**:
  - Form inputs for transaction details
  - Real-time prediction display
  - Visual feedback (color-coded results)

### 2. Input Processing Layer
- **Modules**:
  - `utils.py`: Data validation and preprocessing
  - Feature engineering functions
- **Responsibilities**:
  - Validate input data
  - Transform raw inputs to model-ready format
  - Handle missing or invalid data

### 3. Machine Learning Model
- **Model Type**: Pre-trained scikit-learn pipeline
- **File**: `fraud_detection_pipeline.pkl`
- **Features**:
  - Transaction type
  - Transaction amount
  - Account balances (sender and receiver)
- **Output**: Binary classification (0 = Legitimate, 1 = Fraud)

### 4. Output Processing Layer
- **Functions**:
  - Format prediction results
  - Assign risk levels
  - Generate user-friendly messages

## Data Flow

1. **Input Phase**
   ```
   User Input → Streamlit Interface → Data Validation
   ```

2. **Processing Phase**
   ```
   Validated Data → Feature Engineering → Model Prediction
   ```

3. **Output Phase**
   ```
   Prediction Result → Formatting → Display to User
   ```

## Security Considerations

- No sensitive data is stored or logged
- All processing happens in real-time
- No external API calls
- Model is loaded locally

## Scalability

Current architecture supports:
- Single-user deployment (Streamlit default)
- Can be containerized with Docker for multi-user deployment
- Model can be updated independently of the application

## Future Enhancements

1. **API Layer**: Add REST API for programmatic access
2. **Database**: Store prediction history
3. **Monitoring**: Add logging and monitoring
4. **A/B Testing**: Support multiple model versions
5. **Batch Processing**: Support bulk predictions
