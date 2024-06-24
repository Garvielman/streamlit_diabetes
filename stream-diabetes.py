import pickle
import streamlit as st

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Data Mining Prediction Diabetes')

col1, col2 = st.columns(2)

with col1 :
	Age = st.text_input ('input umur')

with col2 :
	Gender = st.text_input ('input Gender')

with col1 :
	Polyuria = st.text_input ('input Polyuria')

with col2 :
	Polydipsia = st.text_input ('input Polydipsia')

with col1 :
	suddenweightloss = st.text_input ('input sudden weight loss')

with col2 :
	weakness = st.text_input ('input weaknes')

with col1 :
	Polyphagia = st.text_input ('input Polyphagia')

with col2 :
	Genitalthrush = st.text_input ('input Genital thrush')

with col1 :
	visualblurring = st.text_input ('input visual blurring')

with col2 :
	Itching = st.text_input ('input Itching')

with col1 :
	Irritability = st.text_input ('input Irritability')

with col2 :
	delayedhealing = st.text_input ('input delay healing')

with col1 :
	partialparesis = st.text_input ('input partial paresis')

with col2 :
	musclestiffness = st.text_input ('input muscle stiffness')

with col1 :
	Alopecia = st.text_input ('input Alopecia')
	
with col2 :
	Obesity = st.text_input ('input Obesity')

diab_diagnosis = ''

if st.button('Test Prediction Diabetes'):
	diab_prediction = diabetes_model.predict([[Age, Gender, Polyuria, Polydipsia, suddenweightloss, weakness, Polyphagia, Genitalthrush, visualblurring, Itching, Irritability, delayedhealing, partialparesis, musclestiffness, Alopecia, Obesity]])

	if(diab_prediction[0] == 1):
		diab_diagnosis = 'Pasien terkena Diabetes'
	else :
		diab_diagnosis = 'Pasien tidak terkena Diabetes'

	st.success(diab_diagnosis)
