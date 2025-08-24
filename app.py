#### AI ####
from tensorflow.keras.models import load_model
import tensorflow as tf
from PIL import Image
import numpy as np
#### streamlit ####
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import os

#### reset ####
if "model" not in st.session_state:
    model_list = os.listdir("models")
    if model_list == []:
        st.session_state.model = None
        st.session_state.model_name = None
    else:
        st.session_state.model_name = model_list[0]
        st.session_state.model = load_model(f"models/{model_list[0]}")

if "pdt" not in st.session_state:
    st.session_state.pdt = (0,1.0000)


#### Image Preprocessing ####
def predict_digit(model, image_path):
    img = Image.open(image_path).convert('L')
    img = img.resize((28, 28))
    img_array = np.array(img)

    img_array = 255 - img_array  

    img_array = img_array / 255.0  

    img_array = np.expand_dims(img_array, axis=-1)  
    img_array = np.expand_dims(img_array, axis=0)   

    predictions = model.predict(img_array)
    predicted_label = np.argmax(predictions)
    predicted_prob = float(np.max(predictions))
    return predicted_label, predicted_prob

#### UI ####
st.title("AI 이미지 분류 모델 사용하기")
stroke_width = st.slider("펜 굵기", 30, 50, 30)

canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",
    stroke_width=stroke_width,
    stroke_color="#000000",
    background_color="#FFFFFF",
    update_streamlit=True,
    height=500,
    width=500,
    drawing_mode="freedraw",
    key="canvas",
)
name = st.text_area("이미지 이름")

if st.button("INPUT에 저장하기",use_container_width=True):
    if name == "":
        st.error("이미지 이름을 입력해주세요.")
    elif canvas_result.image_data is not None:    
        img = Image.fromarray((canvas_result.image_data).astype(np.uint8))
        save_dir = "input"
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, name+".png")
        img.save(save_path)
        st.success(f"이미지가 저장되었습니다: {save_path}")
    else:
        st.error("이미지가 없습니다. 그림을 그려주세요.")

model_option = st.selectbox("분류 모델 선택",os.listdir("models"))

if st.button("모델 가져오기",use_container_width=True):
    st.session_state.model_name = model_option
    st.session_state.model = load_model(f"models/{model_option}")
    st.success(f"모델을 가져왔습니다: {model_option}")
else:
    if st.session_state.model is not None:
        st.success(f"현재 선택된 모델: {st.session_state.model_name}")
    else:
        st.error("모델이 없습니다. 모델을 가져와주세요.")

img_option = st.selectbox("이미지 선택",os.listdir("input"))
keywords = {'Mnist데이타셋': [0,1,2,3,4,5,6,7,8,9], 'Fashion-MNIST데이타셋':  ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]}
keyword_option = st.selectbox("사용하시는 데이터셋 선택",keywords.keys())

if st.button("이미지 분류하기",use_container_width=True):
    st.session_state.pdt = predict_digit(st.session_state.model, f"input/{img_option}")
    st.session_state.pdt = (keywords[keyword_option][st.session_state.pdt[0]], st.session_state.pdt[1])
    st.success(f"이미지 분류 성공")
st.metric("이미지 분류 결과", st.session_state.pdt[0], str(st.session_state.pdt[1]*100)+"%", border=True)