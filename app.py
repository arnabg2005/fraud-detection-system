#!/usr/bin/env python3
"""
Fraud Detection App - Main Entry Point
This is the main entry point for the fraud detection application.
"""

import streamlit as st
from src.fraud_detection import run_app

if __name__ == "__main__":
    run_app()
