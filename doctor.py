import streamlit as st
import mysql.connector

# Global variable for the database connection
conn = None

def establish_mysql_connection():
    global conn

    try:
        # Establish MySQL connection
        conn = mysql.connector.connect(
            host='silverapp.mysql.database.azure.com',
            user='rushi2701',
            password='User@2701',
            database='silverapp'
        )

        # Display success message
        st.title("Database Connection Established")

        return conn
    except mysql.connector.Error as err:
        # Display error message
        st.error(f"MySQL Connection Error: {err}")
        return None

# In patient.py
def doctor_app():
    # Your implementation here
    st.title("Hello world")
    conn =mysql.connector.connect(user="rushi2701", password="User@2701", host="silverapp.mysql.database.azure.com", port=3306, database="silverapp", ssl_ca="{ca-cert filename}", ssl_disabled=False)

        # Display success message
    st.title("Database Connection Established")

# Call the connection function only when needed
if __name__ == "__main__":
    establish_mysql_connection()
    doctor_app()
