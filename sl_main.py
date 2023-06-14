import streamlit as st
from ImageCoder import *
from request_SD_img2img import *
from prompt_editor import translate_prompt, add_lora, correct_neg_prompt, correct_prompt
from PIL import Image

st.write("# Генерация интерьера помещения по изображению")

prompt = st.text_input("Введите положительное описание изображения")
if prompt:
    st.write("Перевод подсказки на английском:", translate_prompt(prompt))

neg_prompt = st.text_input("Введите негативное описание изображения (что не нужно включать в изображение)")
if neg_prompt:
    st.write("Перевод негативной подсказки на английском:", translate_prompt(neg_prompt))

uploaded_file = st.file_uploader(
    "Выберите изображение", type=["jpg", "jpeg", "png"],
    help="Перетащите файл сюда")


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # Отображение изображения
    st.image(image.resize((300, 300)),
             caption="Загруженное изображение", width=300)
    if st.button('Начать генерацию'):
        if prompt is None:
            prompt = ""
        if neg_prompt is None:
            neg_prompt = ""

        image = Image.open(uploaded_file)
        img64 = pil_image_to_base64(image)
        js = ControlnetRequest(img64,
                               correct_prompt(add_lora(translate_prompt(prompt))),
                               correct_neg_prompt(neg_prompt), url="https://bf2cfeffaebceabd24.gradio.live")\
            .send_request()

        image_bytes = base64.b64decode(js['images'][0])
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Результат генерации")
