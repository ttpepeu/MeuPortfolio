import streamlit as st

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
        col1, col2 = st.columns(2)
        
        with col1:
            """st.title('ChatBot')
            st.image('img/chatbot.jpg')
            st.info(
                'Este chatbot está sendo desenvolvido para o laceb(Laboratório) do Mackenzie, com finalidade de fazer análise de dados das cidades da Região Metropolitana de Campinas.'
                )
            sub_col1, sub_col2 = st.columns(2)
            with sub_col1:
                button('Veja o código','#')
            with sub_col2: 
                button('Veja o bot','#')"""
            st.title('Sistema de Banco')
            st.image('img/atm.jpg')
            st.info(
                'Este repositório contém o desafio do curso de linguagem python da Digital Innovation One solucionado, objetivo era desenvolver um sistema de banco de maneira simples com as seguintes operações(Depósito, saque, extrato)'
                )
            button('Veja o código','https://github.com/ttpepeu/Sistema-de-Banco')

            st.title('Análise Telecom')
            st.image('img/telecom01.jpg')
            st.info(
                'Nessa análise com python você verá o desempenho dos serviços da    empresa de telecom.'
                )
            button('Veja o código','https://github.com/ttpepeu/Python-Telecom/tree/main')
        
        with col2: 
            st.title('Power BI')
            st.image('img/pwoerbi.png')
            st.info(
                'Aqui você encontrará todos meus projetos feitos no Power BI.'
                )
            button('Veja os dashboards','https://app.powerbi.com/view?r=eyJrIjoiOTcxMmEwNjItN2U4MC00YmI0LTk4NmItNjBjNjMyODhiMzVhIiwidCI6ImZiMmIxMjBiLTdlMDMtNDQxZi1hNTJkLWVkODVkMzJiY2M3ZSJ9&pageName=ReportSection9479078add58ddd218d9')

            st.title('Análise Covid-19')
            st.image('img/covid.png')
            st.info(
                'Nessa análise com python você verá a evolução da covid-19 no Brasil.'
                )
            button('Veja o código','https://github.com/ttpepeu/PY-COVID19')

    
    def pag3(): # Pagina de contatos
        st.write('LinkedIn: [https://www.linkedin.com/in/ttpepeu/](https://www.linkedin.com/in/ttpepeu/)')
        st.write('GitHub: [https://github.com/ttpepeu](https://github.com/ttpepeu)')
        st.write('Número do contato e Whatsapp: [+55 (19) 99804-7527](https://api.whatsapp.com/send?phone=5519998047527)')
        st.write('E-mail: [10920013485@mackenzista.com.br](mailto:10920013485@mackenzista.com.br)')
        