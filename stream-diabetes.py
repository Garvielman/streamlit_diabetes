import pickle
import streamlit as st

# Memuat model diabetes
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul aplikasi
st.title('Data Mining Prediction Diabetes')

# Membuat kolom untuk input field
col1, col2 = st.columns(2)

with col1:
    Age = st.number_input('Input Age', min_value=0, max_value=120, step=1)

with col2:
    Gender = st.selectbox('Input Gender', [0, 1])  # Mengasumsikan 0 untuk perempuan dan 1 untuk laki-laki

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

# Placeholder untuk hasil diagnosis
diab_diagnosis = ''

# Ketika tombol diklik, buat prediksi dan tampilkan hasil
if st.button('Test Prediction Diabetes'):
    # Konversi semua input ke nilai numerik
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
    Musclestiffness = int(Musclestiffness)
    Alopecia = int(Alopecia)
    Obesity = int(Obesity)

    # Membuat prediksi dengan array 2D
    diab_prediction = diabetes_model.predict([[Age, Gender, Polyuria, Polydipsia, Suddenweightloss, Weakness, Polyphagia, Genitalthrush, Visualblurring, Itching, Irritability, Delayedhealing, Partialparesis, Musclestiffness, Alopecia, Obesity]])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

    st.success(diab_diagnosis)
