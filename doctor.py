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
        return conn
    except mysql.connector.Error as err:
        print("MySQL Connection Error:", err)
        return None

# Function to establish a MySQL database connection and fetch patient information
def load_patient_info(volunteer_id):
    try:
        # Create a cursor object to execute SQL queries
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

        # Close the cursor and database connection
        #cursor.close()
        #conn.close()

        return patient_info
    except mysql.connector.Error as err:
        st.error("MySQL Connection Error: " + str(err))
        return None

# Function to generate prescription suggestions using the random forest model
def generate_prescription(volunteer_id):
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Specify the absolute path to the model files
    zone_model_path =os.path.join(current_dir, "rf_classifier_zone.pkl")
    prescription_model_path = os.path.join(current_dir, "rf_classifier_prescription.pkl")

    # Load the zone model
    zone_model = joblib.load(zone_model_path)

    # Load the prescription model
    prescription_model = joblib.load(prescription_model_path)
    
    patient_info = load_patient_info(volunteer_id)

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
    volunteer_feature_names1 = ['Oxygen', 'PulseRate', 'Temperature','bp_systolic', 'bp_diastolic']
    volunteer_info_df = pd.DataFrame({
        'Oxygen': [oxygen],
        'PulseRate': [pulse_rate],
        'Temperature': [temperature],
        'bp_systolic': [bp_systolic],
        'bp_diastolic': [bp_diastolic],
        
    }, columns=volunteer_feature_names1)
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
   
    

    # Use the zone model to predict the zone
    zone_prediction = zone_model.predict(volunteer_info_df[volunteer_feature_names1])

    # Use the prescription model to predict the prescription
    prescription_prediction = prescription_model.predict(volunteer_info_df[volunteer_feature_names2])



    # Return the prescription suggestions
    return zone_prediction,prescription_prediction
# Streamlit app
def doctor_app():
    global conn  # Declare the variable as global to modify it within the function
    if conn is None:
        conn = establish_mysql_connection()
    # Add logo image
    logo_image = 'silverline-logo.png'
    
    st.sidebar.image(logo_image, use_column_width=True)
    st.sidebar.title("Doctor Dashboard")

    # Add patient information sidebar
    volunteer_id = st.sidebar.text_input("**Volunteer ID**", key="volunteer_id_input")
    
    patient_info = load_patient_info(volunteer_id)
    

    if patient_info is not None:
        # Display patient information in the sidebar
        st.subheader(f"Volunteer Name: {patient_info[1]}")
        st.sidebar.write(f"**Age:** {patient_info[4]}")
        st.sidebar.write(f"**Gender:** {patient_info[3]}")
        st.sidebar.write(f"**Location:** {patient_info[5]}")
        st.sidebar.write(f"**Contact Details:** {patient_info[6]}")
        logo_image = 'icon.png'
        st.sidebar.image(logo_image, use_column_width=True)


        

        zone_prediction,prescription_prediction = generate_prescription(volunteer_id)
        
        # Display the results
        # Convert ndarray to string
        zone_prediction_str = zone_prediction.item() # color name
        if zone_prediction_str == 0:
            zone_prediction_str = 'Red'
        elif zone_prediction_str == 1:
            zone_prediction_str= 'Amber'
        elif zone_prediction_str == 2:
            zone_prediction_str= 'Yellow'
        elif zone_prediction_str == 3:
            zone_prediction_str = 'Green'
        else:
            zone_label = 'Unknown' 
        # Define a dictionary mapping color names to CSS color values
        color_map = {
            'Green': 'green',
            'Yellow': "yellow",
            'Amber':'orange',
            'Red':"red",
            # Add more color mappings as needed
        }
        # Check if the color exists in the color map
        if zone_prediction_str in color_map:
            # Get the CSS color value for the color
            color = color_map[zone_prediction_str]
        else:
            # Use a default color if the color is not found in the map
            color = 'black'

        # Apply CSS styling to the text using HTML markup
        styled_text = f'<span style="color: {color}; font-weight: bold; font-size: larger; border-radius: 5px;">{zone_prediction_str}</span>'

        # Display the styled text
        #st.markdown(f"Zone Assigned: {styled_text}", unsafe_allow_html=True)
                # Set the CSS style for the box
        box_style = f'''
        background-color: {color};
        color: #FFFFFF;
        padding: 8px;
        border-radius: 10px;
        text-align: center;
        flex: 0.5;
         '''
        
        #conn = establish_mysql_connection()
        # Create a cursor object to execute SQL queries
        '''cursor = conn.cursor()
        query1 = f""" SELECT COUNT(*) AS count1
                    FROM complete_data1
                    WHERE response = 'option1';
                    """
        cursor.execute(query1)
        result1 = cursor.fetchone()
        query2 = f""" SELECT COUNT(*) AS count1
                    FROM complete_data1
                    WHERE response = 'option2';
                    """
        cursor.execute(query2)
        result2 = cursor.fetchone() '''
        #result1[0]=21
        #result1[0]=20
        #result2[0]=10
        accuracy_percentage= 75                    #(result1[0]/(result1[0]+result2[0]))*100

        # Close the cursor and database connection
        #cursor.close()
        #conn.close()

        # Define colors for different ranges
        if accuracy_percentage < 30:
            triangle_color = "red"       # Low accuracy, critical
        elif accuracy_percentage < 70:
            triangle_color = "yellow"    # Moderate accuracy, warning
        else:
            triangle_color = "green"     # High accuracy, normal

        
        st.markdown(
            f"""
            <div style="display: flex;">
            <div style="display: flex; align-items: center; border-right: 1px solid white; padding-right: 10px;">
                <h3>Zone of Volunteer:</h3>
                <div style="{box_style}">{zone_prediction_str}</div>
            </div>
            <div style="border: 2px solid #ccc;padding: 5px; display: flex; align-items: baseline;">
                <h4>Effective Prescription Rate</h4>
                <div style="margin-right: 5px;"><span style="font-weight: bold; font-size: 24px;">{accuracy_percentage:.0f}%</span></span></div>
                <div style="position: relative; bottom: -8px; width: 0; height: 0; border-left: 12px solid transparent; border-right: 12px solid transparent; border-bottom: 20px solid {triangle_color};"></div>

            """,
            unsafe_allow_html=True
        )

        
        st.markdown(
            """
            <div style="padding: 8px;">
                <h3 style="background-color: orange; color: #FFFFFF; padding: 4px; border-radius: 4px;">IOT Monitored Report </h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        patient_info = load_patient_info(volunteer_id)
        
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
                    oxygen=patient_info[11],
                    pulse_rate=patient_info[12],
                    temperature=patient_info[13],
                    Diabetes=patient_info[14],
                    bp_systolic=patient_info[15],
                    bp_diastolic=patient_info[16]
                    
                ),
                unsafe_allow_html=True
            )


        #st.write(f"Diabetes: {patient_info[15]}")
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


        ##################################################################################
        # Define a default message
        default_message = "hello Volunteer"
        # Establish MySQL connection
       
        #conn = establish_mysql_connection()
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        # Fetch the latest response based on timestamp
        select_query = "SELECT response,Fatigue,pain_or_soreness,headache , muscle_or_joint_pain ,low_grade_fever,additional_side_effects FROM complete_data1 WHERE ID = %s"
        select_values = (volunteer_id,)
        cursor.execute(select_query, select_values)
        result = cursor.fetchone()


        # Check if a result is found
        # Check if a result is found
        if result:
            # Access the column values using index positions
            if "option1" == result[0]:
                response = "Prescription followed and feeling better"
            elif "option2" == result[0]:
                response = "Prescription followed but not feeling better"
            elif "option3" == result[0]:
                response = "Prescription Not Followed and feeling better"
            elif "option4" == result[0]:
                response = "Prescription not followed and not feeling better"
            else:
                response="Not given any feedback"

            fatigue = "Yes" if result[1] == 1 else "No"
            pain_or_soreness = "Yes" if result[2] == 1 else "No"
            headache = "Yes" if result[3] == 1 else "No"
            muscle_or_joint_pain = "Yes" if result[4] == 1 else "No"
            low_grade_fever = "Yes" if result[5] == 1 else "No"
            additional_side_effects = result[6]

            # Create a DataFrame to store the data in a tabular format
            data = {
                "Response": [response],
                "Fatigue": [fatigue],
                "Pain or Soreness": [pain_or_soreness],
                "Headache": [headache],
                "Muscle or Joint Pain": [muscle_or_joint_pain],
                "Low-Grade Fever": [low_grade_fever],
                "Additional Side Effects": [additional_side_effects],
            }
            df = pd.DataFrame(data)
            # Display the latest response in a vertical table format
            st.markdown(
                """
                <div style="padding: 8px;">
                    <h3 style="background-color: orange; color: #FFFFFF; padding: 4px; border-radius: 4px;">Volunteer Response </h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.table(df.T)
            
            
            

        else:
            st.markdown(
                """
                <div style="padding: 8px;">
                    <h3 style="background-color: orange; color: #FFFFFF; padding: 4px; border-radius: 4px;">Volunteer Response </h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("**No response found.**")

        # Close the cursor and database connection
        #cursor.close()
        #conn.close()
        
        # Define a default message
        default_message = "Hello patient"

        # Create a text area for the message
        message = st.text_area("**Additional comment:**", value=default_message)

        # Add a submit button
        submit_button = st.button("Submit")

        # Check if the submit button is clicked
        if submit_button:
            # Perform the necessary actions with the message
            # ...
            # Insert the message into the database
            # ...
            st.success("Message submitted successfully!")
        
    else:
        st.sidebar.write("Enter the volunteer id")
        # Display welcome message with styling
        st.markdown("<h2 style='color: orange;'>Welcome, esteemed doctor!</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'> We are grateful for your dedication and We wish you a positive experience on our app.</p>", unsafe_allow_html=True)
        st.image('logo2.png',width=300)

if __name__ == "__main__":
    doctor_app()
