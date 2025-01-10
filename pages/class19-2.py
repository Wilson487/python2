import streamlit as st
from utils import init_page

init_page()
st.title("這是標題")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
if message := st.chat_input("請輸入你的問題"):
    with st.chat_message("user"):
        st.write(message)
    st.session_state.messages.append({"role": "user", "content": message})
    assistant_response = f"你剛剛說了：{message}"
    with st.chat_message("assistant"):
        st.write(assistant_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response}
    )
