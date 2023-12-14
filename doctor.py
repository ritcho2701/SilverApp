import streamlit as st
import pandas as pd
import mysql.connector
import joblib
import os
import random
import numpy as np
from datetime import datetime
# Global variable for the database connection
conn = None


st.title("Hello world")

def establish_mysql_connection():
    global conn  # Add this line to indicate you're using the global variable

    try:
        # Establish MySQL connection
        conn = mysql.connector.connect(
            conn = mysql.connector.connect(
            host='silverapp.mysql.database.azure.com',
            user='rushi2701',
            password='User@2701',
            database='silverapp'
        )
        )
        st.write("Database Connection Information:", conn)

        return conn
    except mysql.connector.Error as err:
        print("MySQL Connection Error:", err)
        return None
    
# In patient.py
def doctor_app():
    # Your implementation here
    st.title("Hello world")
    pass
if __name__ == "__main__":
    establish_mysql_connection()