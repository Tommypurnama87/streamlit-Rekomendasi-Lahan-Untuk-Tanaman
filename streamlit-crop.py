import pickle
import streamlit as st

# membaca model
crop_model  = pickle.load(open('crop_model.sav', 'rb'))

#judul web
st.title('Data Mining Rekomendasi Tanaman Untuk Ditanam Disebuah Lahan Pertanian')

# Membagi kolom
col1, col2, = st.columns(2)

with col1 :
    N = st.text_input ('Masukan Level Nitrogen')

with col2 :
    P = st.text_input ('Masukan Level Phosphorus')

with col1 :
    K = st.text_input ('Masukan Level Potassium')

with col2 :
    temperature = st.text_input ('Masukan Tingkat Temperature')

with col1 :
    humidity = st.text_input ('Masukan Tingkat Local Humidity')

with col2 :
    ph = st.text_input ('Masukan Tingkat Keasaman Tahah')

with col1 :
    rainfall = st.text_input ('Masukan Tingkat Curah Hujan Per Musim')

# code untuk prediksi
crop_recomend = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    crop_prediction = crop_model.predict([[N, P, K, temperature, humidity, ph, rainfall]])

    if(crop_prediction[0] == 0):
       crop_recomend = 'Cocok Untuk Padi'
    elif(crop_prediction[0] == 1):
       crop_recomend = 'Cocok Untuk Coffee'
    else :
        crop_recomend = 'Cocok Untuk Jagung'
    st.success(crop_recomend)

