import streamlit as st
st.set_option('browser.gatherUsageStats', False)

st.set_option('deprecation.showfileUploaderEncoding', False)
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


# Function to establish a MySQL database connection and fetch patient information
def load_patient_info(volunteer_id):
    global conn 
    try:
        conn = establish_mysql_connection()
        
        if conn is not None:
            cursor = conn.cursor()
            # Define the SQL query to retrieve patient information based on volunteer ID
            query = f"""
                SELECT vp.ID, vp.first_name, vp.last_name, vp.gender, vp.age, vp.location, vp.contact_number, vp.mail_id, vp.conditions, vp.vaccine_type, vp.created_at,
                    vf.Oxygen, vf.PulseRate, vf.Temperature, vf.Diabities, vf.bp_systolic, vf.bp_diastolic
                FROM volunteer_personal_data vp
                JOIN volunteer_fitness_data vf ON vp.ID = vf.ID
                WHERE vp.ID = '{volunteer_id}';
                """
            # Execute the query
            cursor.execute(query)

            # Fetch the patient information
            patient_info = cursor.fetchone()

            return patient_info
        

    except mysql.connector.Error as err:
        print("MySQL Connection Error:", err)
        return None

    
def validate_unique_id(unique_id):
    conn = establish_mysql_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT volunteer_id FROM patients WHERE unique_id = %s", (unique_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            return result[0]
        
    else:
        return None

# Function to generate prescription suggestions using the random forest model
def generate_prescription(volunteer_id):
    
    
    patient_info = load_patient_info(volunteer_id)

    # Extract the required values from the patient_info tuple
    # Extract the required values from the patient_info tuple
    ID = patient_info[0]
    first_name = patient_info[1]
    last_name = patient_info[2]
    gender = patient_info[3]
    age = patient_info[4]
    location = patient_info[5]
    contact_number = patient_info[6]
    mail_id = patient_info[7]
    conditions = patient_info[8]
    vaccine_type = patient_info[9]
    created_at = patient_info[10]
    oxygen = patient_info[11]
    pulse_rate = patient_info[12]
    temperature = patient_info[13]
    diabetes = patient_info[14]
    bp_systolic = patient_info[15]
    bp_diastolic = patient_info[16]
    
    
    # Create the volunteer_info_df DataFrame
    volunteer_feature_names2 = ['Oxygen', 'PulseRate', 'Temperature', 'Age', 'bp_systolic', 'bp_diastolic', 'Diabetes']
    volunteer_info_df = pd.DataFrame({
        'Oxygen': [oxygen],
        'PulseRate': [pulse_rate],
        'Temperature': [temperature],
        'Age': [age],
        'bp_systolic': [bp_systolic],
        'bp_diastolic': [bp_diastolic],
        'Diabetes': [diabetes]
    }, columns=volunteer_feature_names2)

    # Use the prescription model to predict the prescription
    prescription_prediction = prescription_model.predict(volunteer_info_df[volunteer_feature_names2])
     # Return the prescription suggestions
    return prescription_prediction


    
def load_data():
    # Replace with your data loading logic
    data = [
        { "rating": "guru"},
    ]
    return pd.DataFrame(data)
# Streamlit app
def patient_app():
    
    global conn  # Declare the variable as global to modify it within the function
    
    logo_image = 'silverline-logo.png'
    st.sidebar.image(logo_image, use_column_width=True)
    st.sidebar.title("Volunteer Dashboard")
    volunteer_id=''
    unique_id = st.sidebar.text_input("**Volunteer UniqueID**", key="volunteer_id_input")
    if st.sidebar.markdown('<div class="floating-text">Submit</div>', unsafe_allow_html=True):
        volunteer_id = validate_unique_id(unique_id)
        
    patient_info = load_patient_info(volunteer_id)
    if patient_info is not None:
        prescription_prediction = generate_prescription(volunteer_id)       
        # Display the results
        prescription_prediction_str=prescription_prediction.tolist()
        custom_color="#FF5733"
        # Display the colored box with red text
        st.markdown(
            f"""
            <div style="border: 3px solid #ccc;padding-left: 100px;padding-right:10px;display: flex;">
                <div style="display: flex; align-items: center; border-right: 1px solid white; padding-right: 10px;">
                    <h3 style='color:#FF8C00;'>Hello {patient_info[1]}!</h3>
                </div>
                <div style=" display: flex; align-items: baseline;">
                    <div> <h1> </h1></div>
                    <div> <h1> </h1></div>
                    <div> <h1> </h1></div>
                    <div> <h1><span style='color:{custom_color};'>Ebot</span></h1>
                        <div><strong>Health & Safety our mission</strong></div>
                        <div style="color: #008080;">Please feel free to contact 24*7</div>
                        <div><strong>Email:</strong>ebot@xyz.com</div>
                    </div>
                </div>
                
        
            </div>
                
           </div>

            """,
            unsafe_allow_html=True
        )
        st.markdown(
                """
                <div style="padding: 8px;">
                    <h3 style="background-color: orange; color: #FFFFFF; padding: 4px; border-radius: 4px;">IOT Monitored Report</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown(
                    """
                    <div style="border: 2px solid #CCCCCC; padding: 10px; margin-bottom: 10px;">
                        <p><strong>Oxygen:</strong> {oxygen} %</p>
                        <p><strong>Pulse Rate:</strong> {pulse_rate} bpm</p>
                        <p><strong>Temperature:</strong> {temperature} °F </p>
                        <p><strong>Blood Pressure (Systolic):</strong> {bp_systolic} mmHg</p>
                        <p><strong>Blood Pressure (Diastolic):</strong> {bp_diastolic} mmHg</p>
                        <p><strong>Diabetes:</strong> {Diabetes} mg/dL</p>
                    </div>
                    """.format(
                        oxygen=int(patient_info[11]),
                        pulse_rate=int(patient_info[12]),
                        temperature=patient_info[13],
                        Diabetes=patient_info[14],
                        bp_systolic=patient_info[15],
                        bp_diastolic=patient_info[16]

                    ),
                    unsafe_allow_html=True
                )
        # Add main window for prescription suggestions
    
        st.markdown(
            """
            <div style="padding: 8px;">
                <h3 style="background-color: orange; color: #FFFFFF; padding: 4px; border-radius: 4px;">Prescription Suggestions </h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        prescription_prediction_str = str(prescription_prediction.tolist())
        # Access the identified conditions
        identified_conditions_str = prescription_prediction_str[0][0]
        # Convert the string representation of the list back to a list
        prescription_prediction_list = eval(prescription_prediction_str)
        st.markdown(
                """
                <div style="border: 1px solid #CCCCCC; padding: 10px; margin-bottom: 10px;">
                    <h4>Predictive Health Conditions </h4>
                    <p>{condition}</p>
                </div>
                """.format(condition=prescription_prediction_list[0][0]),
                unsafe_allow_html=True
        )


        # Access the prescription steps
        prescription_steps_str = prescription_prediction_list[0][1]
        
        prescription_bullets = prescription_steps_str.split(".")
        formatted_prescription = "\n".join(["\n• " + bullet.strip() for bullet in prescription_bullets if bullet.strip() != ""])
        
        st.markdown(
            """
            <div style="border: 1px solid #CCCCCC; padding: 10px; margin-bottom: 10px;">
                <h4>Prescription Steps </h4>
                <p>{prescription}</p>
            </div>
            """.format(prescription=formatted_prescription),
            unsafe_allow_html=True
        )
        
                

        # feedback form
        
        id = 1  # Replace with your own logic to generate a unique ID
        # Display the options
        st.info("Your prescription has been generated! Please share your feedback after 2 hours. Your insights help us for better care and enhance our services. Thank you for choosing us!")

        current_time = datetime.now()
        #st.subheader("Select any additional effects experienced:")
        st.markdown(
                """
                <div style="padding: 8px;">
                    <h3 style="background-color: orange; color: #FFFFFF; padding: 4px; border-radius: 4px;">Select any additional effects experienced</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
        option5 = st.checkbox("Fatigue")
        option6 = st.checkbox("Pain or Soreness at the Injection Site")
        option7 = st.checkbox("Headache")
        option8 = st.checkbox("Muscle or Joint Pain")
        option9 = st.checkbox("Low-Grade Fever")
        additional_side_effects = st.text_area("Additional effects (if any):")
        # Initialize the response variable
        # Display the options
        st.write("Please select an option:")
        option1 = st.button("Prescription followed and feeling better")
        option2 = st.button("Prescription followed but not feeling better")
        option3 = st.button("Prescription Not Followed and feeling better")
        option4 = st.button("Prescription not followed and not feeling better")
        response = ""
        # Check the selected option and display the corresponding message
        if option1:
            st.success("Good to see that prescription working for you!")
            response = "Prescription followed and feeling better"
        elif option2:
            st.info("Kindly contact doctor! contact No:+91********67")
            response = "Prescription followed but not feeling better" 
        elif option3:
            st.warning("That's the good progress but we request you to follow the prescription")
            response = "Prescription Not Followed and feeling better"
            
        elif option4:
            st.info("We request you to follow prescription and let us know how you are feeling.")
            response = "Prescription not followed and not feeling better"
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        feedback = {
            "response": response,
            "fatigue": option5,
            "pain_or_soreness": option6,
            "headache": option7,
            "muscle_or_joint_pain": option8,
            "low_grade_fever": option9,
            "additional_side_effects": additional_side_effects
        }
        cursor = conn.cursor()
        st.write("**************************************************")
        if st.button("Submit Feedback"):
            

            st.success("Feedback submitted successfully.")
            
            #cursor.close()
            #conn.close()
        # Close the cursor and database connection
        #cursor.close()
        #conn.close()   

        

        
        
    else:
        # Display welcome message with styling
        st.markdown("<h2 style='color: orange;'>Welcome, volunteer!</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>We wish you good health and a positive experience on our app.</p>", unsafe_allow_html=True)
        st.image('logo2.png',width=300)

if __name__ == '__main__':
    patient_app()
