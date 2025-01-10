import streamlit as st
from utils import init_page

init_page()
st.title("這是標題")
demo_messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好，我是課程助手"},
    {"role": "user", "content": "看起來不錯喔"},
    {"role": "assistant", "content": "沒錯，就是這樣!"},
]

for message in demo_messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if message := st.chat_input("請輸入你的問題"):
    with st.chat_message("user"):
        st.write(message)
    with st.chat_message("assistant"):
        st.write(f"這是示範回覆，我收到訊息[{message}]")
