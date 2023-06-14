import streamlit as st

st.write("# Получение дизайна планировки по изображению")

uploaded_files = st.file_uploader("Загрузите изображение",
                                  accept_multiple_files=False)
