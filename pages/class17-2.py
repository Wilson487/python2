from utils import init_page

init_page()
import streamlit as st
import os


image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

# st.title("圖片")
# st.image("image/0.png", width=300)
image_width = st.number_input("請輸入圖片寬度", value=300, step=10)
a = st.selectbox("請選擇圖片", ["0.png", "1.jpg", "fighter.jpg"])

st.write(f"你選擇的圖片是:{a}")

if a == "0.png":
    st.image("image/0.png", width=image_width)
elif a == "1.jpg":
    st.image("image/1.jpg", width=image_width)
else:
    st.image("image/fighter.jpg", width=image_width)
