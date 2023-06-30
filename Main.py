import streamlit as st
from pags import pags

tab1, tab2, tab3 = st.tabs(['MENU', 'PROJETOS', 'CONTATOS'])


with open('style.css') as s:
    st.markdown(f'<style>{s.read()}</style>', unsafe_allow_html=True)


with tab1:
    pags.pag1()

with tab2:
    pags.pag2()

with tab3:
    pags.pag3()






