import streamlit as st
from patient import patient_app
from doctor import doctor_app

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

# Define the different app pages
app_pages = {
    'Home': None,
    'Patient': patient_app,
    'Doctor': doctor_app
}

# Create a SessionState object to store the current page
if 'page' not in st.session_state:
    st.session_state.page = 'Home'


# Get the index of the current page
current_page_index = list(app_pages.keys()).index(st.session_state.page)

# Render the dropdown for page selection
new_page = st.sidebar.selectbox(
    '',
    list(app_pages.keys()),
    index=current_page_index,
)

# Update the current page based on the selected page in the sidebar
if new_page != st.session_state.page:
    st.session_state.page = new_page

# Render the app page based on the selected page name
page = app_pages[st.session_state.page]
if page is not None:
    page()
# Add introduction to the Home page
if st.session_state.page == 'Home':
    st.markdown(
                """
                <div style="border: 1px solid #CCCCCC; padding: 10px; margin-bottom: 10px;">
                    <h4>Welcome to the Home Page </h4>
                    
                </div>
                """,
                unsafe_allow_html=True
        )
   