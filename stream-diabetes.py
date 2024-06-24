import pickle
import streamlit as st

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.tittle('Data Mining Prediction Diabetes')

col1, col2 = st.columns(2)

with col1 :
	Age = st.text_input ('input umur')

with col2 :
	Gender = st.text_input ('input Gender')

with col1 :
	Polyuria = st.text_input ('YES/NO')

with col2 :
	Polydipsia = st.text_input ('YES/NO')

with col1 :
	sudden weight loss = st.text_input ('YES/NO')

with col2 :
	weakness = st.text_input ('YES/NO')

with col1 :
	Polyphagia = st.text_input ('YES/NO')

with col2 :
	Genital thrush = st.text_input ('YES/NO')

with col1 :
	visual blurring = st.text_input ('YES/NO')

with col2 :
	Itching = st.text_input ('YES/NO')

with col1 :
	Irritability = st.text_input ('YES/NO')

with col2 :
	delayed healing = st.text_input ('YES/NO')

with col1 :
	partial paresis = st.text_input ('YES/NO')

with col2 :
	muscle stiffness = st.text_input ('YES/NO')

with col1 :
	Alopecia,Obesity = st.text_input ('YES/NO')

diab_diagnosis = ''

if st.button('Test Prediction Diabetes'):
	diab_prediction = diabetes_model.prediction([[Age,Gender,Polyuria,Polydipsia,sudden weight loss,weakness,Polyphagia,Genital thrush,visual blurring,Itching,Irritability,delayed healing,partial paresis,muscle stiffness,Alopecia,Obesity]])

	if(diab_prediction[0] == 1):
		diab_diagnosis = 'Pasien terkena Diabetes'
	else :
		diab_diagnosis = 'Pasien tidak terkena Diabetes'

	st.success(diab_diagnosis)