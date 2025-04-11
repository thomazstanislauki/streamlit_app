import streamlit as st

def sidebar():
    with st.sidebar:
        st.markdown("[Capítulo 1](#df1e4b24)")
        st.markdown("[Capítulo 2](#6e7c1246)")
        st.markdown("[Capítulo 3](#9bf8ed1)")	
        st.markdown("[Capítulo 4](#bd8f6fd8)")
        st.markdown("[Capítulo 5](#6fcf2441)")
        st.markdown("[Capítulo Final](#96137013)")

def urls_style():
    st.markdown(
    """
    <style>
        a {
            color: inherit !important;
            text-decoration: none;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
