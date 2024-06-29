
import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd
import importlib















train = pd.read_csv('train.csv')

# web application

st.set_page_config(
	page_title="Flights Prices Prediction",
	page_icon="✈️",
	layout="wide"
)

#title page
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        font-size: 2.5em;
        color: #FFFFFF;
        padding: 2px 0;
        margin-bottom: 4px;
    }
    .centered-subheader {
        text-align: center;
        font-size: 1.8em;
        color: #FFFFFF;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh; /* Full viewport height to center vertically */
    }
    </style>
            
    <div class="container">
        <div class="centered-title">WELCOME TO FLIGHT PRICE PREDICTOR</div>
        <div class="centered-subheader"><span style="color: red;">AWS SAGEMAKER</span></div>
        <div class="centered-subheader">&</div>
        <div class="centered-subheader"><span style="color: red;">STREAMLIT</span></div>
    </div>
    """, unsafe_allow_html=True)


#sidebar



st.sidebar.header("Main Menu")

with st.sidebar:
    selected = option_menu("", ['Home','Predict', 'Airline','Source','Destination','Duration','Journey date'], 
    icons=[ 'house', 'search','airplane','house','globe','clock','calendar'], menu_icon="cast", default_index=0)
    

# def run_script(script_path):
#     with open(script_path) as script:
#         exec(script.read())

# if selected == 'Predict':
#     run_script('app-predict.py')





