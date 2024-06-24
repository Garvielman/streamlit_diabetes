import pickle
import streamlit as st

# Load the diabetes model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Title of the app
st.title('Data Mining Prediction Diabetes')

# Creating columns for input fields
col1, col2 = st.columns(2)

with col1:
    Age = st.number_input('Input Age', min_value=0, max_value=120, step=1)

with col2:
    Gender = st.selectbox('Input Gender', [0, 1])  # Assuming 0 for female and 1 for male

with col1:
    Polyuria = st.number_input('Input Polyuria', min_value=0, max_value=1, step=1)

with col2:
    Polydipsia = st.number_input('Input Polydipsia', min_value=0, max_value=1, step=1)

with col1:
    Suddenweightloss = st.number_input('Input Sudden Weight Loss', min_value=0, max_value=1, step=1)

with col2:
    Weakness = st.number_input('Input Weakness', min_value=0, max_value=1, step=1)

with col1:
    Polyphagia = st.number_input('Input Polyphagia', min_value=0, max_value=1, step=1)

with col2:
    Genitalthrush = st.number_input('Input Genital Thrush', min_value=0, max_value=1, step=1)

with col1:
    Visualblurring = st.number_input('Input Visual Blurring', min_value=0, max_value=1, step=1)

with col2:
    Itching = st.number_input('Input Itching', min_value=0, max_value=1, step=1)

with col1:
    Irritability = st.number_input('Input Irritability', min_value=0, max_value=1, step=1)

with col2:
    Delayedhealing = st.number_input('Input Delayed Healing', min_value=0, max_value=1, step=1)

with col1:
    Partialparesis = st.number_input('Input Partial Paresis', min_value=0, max_value=1, step=1)

with col2:
    Musclestiffness = st.number_input('Input Muscle Stiffness', min_value=0, max_value=1, step=1)

with col1:
    Alopecia = st.number_input('Input Alopecia', min_value=0, max_value=1, step=1)

with col2:
    Obesity = st.number_input('Input Obesity', min_value=0, max_value=1, step=1)

# Placeholder for the diagnosis result
diab_diagnosis = ''

# When the button is clicked, make the prediction and display the result
if st.button('Test Prediction Diabetes'):
    # Convert all inputs to numeric values
    Age = int(Age)
    Gender = int(Gender)
    Polyuria = int(Polyuria)
    Polydipsia = int(Polydipsia)
    Suddenweightloss = int(Suddenweightloss)
    Weakness = int(Weakness)
    Polyphagia = int(Polyphagia)
    Genitalthrush = int(Genitalthrush)
    Visualblurring = int(Visualblurring)
    Itching = int(Itching)
    Irritability = int(Irritability)
    Delayedhealing = int(Delayedhealing)
    Partialparesis = int(Partialparesis)
    Muscle_stiffness = int(Musclestiffness)
    Alopecia = int(Alopecia)
    Obesity = int(Obesity)

    diab_prediction = diabetes_model.predict([[Age, Gender, Polyuria, Polydipsia, Suddenweightloss, Weakness, Polyphagia, Genitalthrush, Visualblurring, Itching, Irritability, Delayedhealing, Partialparesis, Musclestiffness, Alopecia, Obesity]])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

    st.success(diab_diagnosis)
