from model import Model
import streamlit as st

st.title('Prediksi Kualitas Anggur Merah')

st.header('Isi 11 Parameter di bawah ini: ')

model = Model()
params = []


fa = st.slider('Keasaman Tetap', 4.6, 15.9, 4.6, 0.1)
params.append(fa)

va = st.slider('Keasaman Rentan Menguap', 0.12, 1.58, 0.12, 0.01)
params.append(va)

ca = st.slider('Asam Sitrat', 0.0, 1.0, 0.0, 0.01)
params.append(ca)

rs = st.slider('Kadar Residu Gula', 0.9, 15.5, 0.5, 0.1)
params.append(rs)

ch = st.slider('Kadar Klorat', 0.01, 0.61, 0.01, 0.01)
params.append(ch)

fs = st.slider('Sulfur Dioksida Bebas', 1, 72, 1, 1)
params.append(fs)

ts = st.slider('Total Sulfur Dioksida', 6, 289, 6, 1)
params.append(ts)

de = st.slider('Massa Jenis', 0.99, 1.00, 0.99, 0.001)
params.append(de)

ph = st.slider('Kadar Keasaman (pH)', 2.74, 4.01, 2.74, 0.01)
params.append(ph)

su = st.slider('Kadar Sulfat (SO2)', 0.33, 2.00, 0.33, 0.01)
params.append(su)

al = st.slider('Persentase Kadar Alkohol', 8.4, 14.9, 8.4, 0.1)
params.append(al)


st.header('Hasil dari prediksi')
params = model.make_param(params)
res = model.predict_model(params)[0]
st.markdown(f'Predisi menunjukkan bahwa kualitas anggur merah berada pada angka: {res}')


st.header('Preview skor untuk model:')
chart = model.model_evaluation()
st.bar_chart(chart)