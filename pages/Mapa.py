import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(page_title="PlayTennis - THM", page_icon="🎾")


df = pd.read_csv('./data/unidades_playtennis.csv')

mapa = folium.Map(
    location=[-23.5505, -46.6333],
    zoom_start=11
)

# Mapa Outros
folium.TileLayer(
    tiles='https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',
    attr='&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    name='Stadia Alidade Smooth Dark',
    control=True
).add_to(mapa)

icon_img = "./assets/img/PlayTennis.png"


for index, row in df.iterrows():

    # HTML do IFrame
    html_iframe = f"""
        <div style="font-family: Arial, sans-serif; padding: 10px; width: 100%; box-sizing: border-box; flex-direction: column; display: flex; align-items: center; justify-content: center; height: 100%; gap: 8px;">
            <h2 style="margin: 0 0 8px 0; font-size: 1.2em; color: #2d3a4a; text-align: center; width: 100%; text-transform: uppercase;">{row['nome_unidade']}</h2>
            <p style="margin: 0 0 10px 0; color: #444; font-size: 1.2em;">{row['sobre']}</p>
            
            <p style="margin: 0 0 10px 0; color: #444; font-size: 0.9em; text-align: center;">A unidade possui: {row['oferecimento_unidade']}</p>
            
            <div style="width: 100%; border-top: 1px solid #e0e0e0; margin: 8px 0 0 0; padding-top: 8px;">
                <div style="margin-bottom: 4px; text-align: center;"><b>Telefone:</b> <span style="color:#1976d2;">{row['telefone']}</span></div>
                <div style="text-align: center;"><b>Endereço:</b> <span style="color:#1976d2;">{row['endereco']}</span></div>
            </div>
        </div>
    """

    # Criação do popup
    iframe_html = folium.IFrame(html=html_iframe, width=500, height=400)
    popup = folium.Popup(iframe_html)

    # Ícone 
    icon = folium.CustomIcon(
        icon_image=icon_img,
        icon_size=(30, 30),
    )

    # Marker
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=popup,
        icon=icon
    ).add_to(mapa)


st.title("🗺️ Mapa de Unidades PlayTennis")

st.divider()

st_mapa = st_folium(mapa, use_container_width=True, height=800)
