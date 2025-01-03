import streamlit as st

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
