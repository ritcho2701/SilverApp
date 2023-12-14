import streamlit as st
import pandas as pd
import mysql.connector
import joblib
import os
import random
from datetime import datetime
import numpy as np
# Global variable for the database connection
conn = None

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Specify the absolute path to the model files
prescription_model_path = os.path.join(current_dir, "rf_classifier_prescription.pkl")
# Load the prescription model
prescription_model = joblib.load(prescription_model_path)

# Add CSS styles
st.markdown(
    """
    <style>
    .floating-text {
        display: inline-block;
        padding: 8px 40px;
        background-color: transparent;
        color: #000000;
        border: 2px solid #FFA500;
        border-radius: 50px;
        box-shadow: 0px 2px 5px rgba(0, 255, 0, 0.25);
        text-align: center;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    
    .floating-text:hover {
        background-color: #006400;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def establish_mysql_connection():
    global conn  # Add this line to indicate you're using the global variable

    try:
        # Establish MySQL connection
        conn = mysql.connector.connect(
            host='silverapp.mysql.database.azure.com',
            user='rushi2701',
            password='User@2701',
            database='silverapp'
        )
        st.write("Database Connection Information:", conn)

        return conn
    except mysql.connector.Error as err:
        print("MySQL Connection Error:", err)
        return None



if __name__ == '__main__':
    patient_app()
