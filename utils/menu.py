import streamlit as st


def menu():
    st.sidebar.title("菜單")
    st.sidebar.page_link(page="main.py", label="首頁", icon="🏠")
    st.sidebar.markdown("---")
    st.sidebar.title("課程")
    st.sidebar.page_link(page="pages/class16.py", label="class16", icon="📚")
    st.sidebar.page_link(page="pages/class17.py", label="class17", icon="📚")
    st.sidebar.page_link(page="pages/class17-2.py", label="class17-2", icon="📚")
    st.sidebar.page_link(page="pages/class19.py", label="class19", icon="📚")
    st.sidebar.page_link(page="pages/class19-2.py", label="class19-2", icon="📚")
    st.sidebar.page_link(page="pages/class20.py", label="class20", icon="📚")

    st.sidebar.markdown("---")
