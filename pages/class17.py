import streamlit as st
import os

st.title("這是標題")
st.write(
    "這是一個用'st.write'顯示的文字，可以處理種格式，例如:數字，文字，Markdown，數據框等"
)
st.text("這是一個用'st.text'顯示的純文字字串，只能顯示純文字，不支持其他格式")
st.markdown(
    """
這是一個用"st.markdown"顯示的字串，
可以處理Markdown語法，
例如:**粗體文字**，
*斜體文字*，
[連結](https://www.google.com)，
代碼塊:
```python print("Hello World")
"""
)


#   streamlit run main.py


with st.expander("點擊展開/收起"):
    st.markdown(
        """
        這是展開元件內部
        """
    )

number = st.number_input("請輸入文字", step=1)
st.markdown(f"你輸入的文字是:{number}")

text = st.text_input("請輸入文字")
st.markdown(f"你輸入的文字是:{text}")


if st.button("sb加1"):
    st.balloons()


col1, col2 = st.columns(2)
col1.button("功德加1", key="btn1")
col2.button("成績加2", key="btn2")

col1, col2 = st.columns([1, 2])
col1.button("功德加1", key="btn3")
col2.button("成績加2", key="btn4")

col1, col2, col3 = st.columns([1, 2, 3])

col1.button("功德加1", key="btn5")
col2.button("成績加2", key="btn6")
col3.button("顏質加3", key="btn7")


col1, col2 = st.columns([1, 2])
with col1:
    if st.button("功德加1", key="btn8"):
        st.balloons()
    st.write("這是col1")
with col2:
    if st.button("成績加2", key="btn9"):
        st.balloons()
    st.write("這是col2")

    col_num = st.number_input("")
    cols = st.columns(4)
    for i in range(len(cols)):
        with cols[i]:
            st.button(f"功德加{i+1}", key=f"btn{i+10}")


col1, col2 = st.columns(2)
with col1:
    st.button("功德加1", key="1")
    st.button("功德加2", key="2")
    st.button("功德加3", key="3")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.markdown("---")
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"功德加{i+1}", key=f"{i+4}")
    with col2:
        st.write(f"這是col2_{i+1}")


ans = 1
if st.button("功德加1", key="ans1"):
    ans = ans + 1
st.write(f"ans={ans}")


if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("功德加1", key="ans2"):
    st.session_state.ans = st.session_state.ans + 1
    st.balloons()
st.write(f"ans={st.session_state.ans}")


image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

st.title("圖片")
st.image("image/0.png", width=300)


fruit = st.selectbox("請選擇圖片", ["仕奇", "多拉B夢"])
st.write(f"你選擇的圖片是:{fruit}")
