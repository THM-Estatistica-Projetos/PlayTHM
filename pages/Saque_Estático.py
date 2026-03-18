import streamlit as st

# Alterar para a página
title = "Análise Postural"
page_icon = ":material/sports_tennis:"

default_text_color = "rgb(15, 13, 66)"
default_secondary_text_color = "#e67c3e"

st.set_page_config(page_title=title, page_icon=page_icon)

st.markdown(f"""
            
            <style>
                .main_title {{
                    font-size: 65px !important;   
                    color: {default_text_color} !important;
                }}
                .center {{
                    display: flex;
                    justify-content: center;
                    padding-left: 15px;
                    width: fit-content;
                    border-bottom: 5px solid {default_text_color};
                }}
            </style>
           
            <div class="center">
                <h1 class="main_title">{title}</h1>
            </div>
            
            """, unsafe_allow_html=True)

st.write("")

motion_video = open("assets/video/Motion_capture.mp4", "rb")
motion_bytes = motion_video.read()
    
st.video(motion_bytes, autoplay=True, loop=True, muted=True)