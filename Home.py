import streamlit as st

st.set_page_config(page_title="PlayTennis - THM", page_icon="🎾", layout="wide")

with st.sidebar:
    
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                background-color: #293473;
            }
            [data-testid="stSidebar"] * {
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)

    
    with st.container():
        st.markdown("""
            <style>
                div.stImage{
                    background-image: linear-gradient(to top, rgba(255, 255, 255, 0.1), transparent);
                    border-radius: 5px;
                    border-bottom: 2px solid rgba(255, 255, 255, 0.3);
                    padding: 10px;
                    width: 100px;
                    height: 75px;
                }
            </style>
        """, unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1, 7, 7, 1])
    
        st.logo("./assets/img/Logos.png", size="large")
    
    home = st.Page("./Home.py", title="Home", icon=":material/home:")
    visao = st.Page("./pages/Visão_Computacional.py", title="Scout com Visão Computacional", icon=":material/eye_tracking:")
    saque = st.Page("./pages/Saque_Estático.py", title="Análise Postural - Saque", icon=":material/sports_tennis:")
    saque2 = st.Page("./pages/Análise_Dinâmica.py", title="Análise Dinâmica - Fundamentos", icon=":material/construction:")
    mapa = st.Page("./pages/Mapa.py", title="Estudo de Mercado", icon=":material/map:")
    softwares = st.Page("./pages/Softwares.py", title="Estudo de Tecnologias", icon=":material/camera:")
    
    pg = st.navigation({
        "Inteligência de Dados": [mapa, softwares],
        "Inteligência Artificial": [visao, saque, saque2],
    })

pg.run()