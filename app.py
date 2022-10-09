import streamlit as st
import utilss as utl
from views import home,about,detect_D2,configuration
import detect_yolo 


st.set_page_config(layout="wide", page_title='Détection d\'objets routiers')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = utl.get_current_route()
    if route == "Page d\'accueil":
        home.load_view()
    elif route == "A propos":
        about.load_view()
    elif route == "Detection avec Detectron2":
        detect_D2.load_view_D2()
    elif route == "Detection avec Yolo v5":
        detect_yolo.load_view_yolo()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()

