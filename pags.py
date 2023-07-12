import streamlit as st
import streamlit as st
from bs4 import BeautifulSoup
import requests


# Botão desenvolvido em CSS
def button(comment,link_url):
    button_style = """
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 8px 18px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    """
    st.markdown(
        f'<a href="{link_url}" target="_blank"><button style="{button_style}">{comment}</button></a>',
        unsafe_allow_html=True
    )

class pags:
        
    def pag1(): # Pagina principal
        col1, col2, col3=st.columns(3)
        with col1:
            st.header('Pedro Trindade')
            st.text('Bem-vindo ao meu portfólio,\naqui você encontra todos\nmeu projetos.')

        with col2:
            pass

        with col3:
            st.image('img/profile-pic 1.png')
        
        
    
    def pag2(): # Pagina de projetos
        # Projetos PowerBI
        st.title('Projetos feitos com Power BI')
        st.image('img/pwoerbi.png')
        st.info(
            'Aqui você encontrará todos meus projetos feitos no Power BI.'
            )
        button('Veja os dashboards','https://app.powerbi.com/view?r=eyJrIjoiOTcxMmEwNjItN2U4MC00YmI0LTk4NmItNjBjNjMyODhiMzVhIiwidCI6ImZiMmIxMjBiLTdlMDMtNDQxZi1hNTJkLWVkODVkMzJiY2M3ZSJ9&pageName=ReportSection9479078add58ddd218d9')
        
        # Projetos GitHub
        st.title('Projetos salvos no GitHub')
        url = f'https://github.com/ttpepeu?tab=repositories'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")


        links = soup.find_all('a',{'itemprop':'name codeRepository'})

        columnFirst = []
        columnSecond = []
        repositorys = []

        addRepositorys = [repositorys.append(f'[{i.text.strip()}](https://github.com/ttpepeu/{i.text.strip()})') for i in links]

        separator = [columnFirst.append(repositorys[i]) for i in range(len (repositorys)) if i%2 == 0]
        separator = [columnSecond.append(repositorys[i]) for i in range(len (repositorys)) if i%2 == 1]

        col1, col2 = st.columns(2)

        with col1:
            for i in columnFirst:
                st.write(i)

        with col2:
            for i in columnSecond:
                st.write(i)
    
    def pag3(): # Pagina de contatos
        st.write('LinkedIn: [https://www.linkedin.com/in/ttpepeu/](https://www.linkedin.com/in/ttpepeu/)')
        st.write('GitHub: [https://github.com/ttpepeu](https://github.com/ttpepeu)')
        st.write('Número do contato e Whatsapp: [+55 (19) 99804-7527](https://api.whatsapp.com/send?phone=5519998047527)')
        st.write('E-mail: [10920013485@mackenzista.com.br](mailto:10920013485@mackenzista.com.br)')
        