import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

from pytrends.request import TrendReq


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Solutions", page_icon="⚙️")

st.title('Novus Solutions ⚙️')
st.header("Detección de Cosecha En Tiempo Real💹")




picture = st.camera_input("Fotografía la planta de Pistacho a evaluar")

if picture:
    st.image(picture)
    


def render_basic_radar():
    option = {
        "title": {"text": "Diagnóstico Personalizado de Brecha de Conocimiento"},
        "legend": {"data": ["Estado Actual de Alumno", "Meta de Aprendizaje"]},
        "radar": {
            "indicator": [
                {"name": "Conceptos", "max": 6500},
                {"name": "Teorías", "max": 16000},
                {"name": "Modelos", "max": 30000},
                {"name": "Casos de Estudio", "max": 38000},
                {"name": "Ejercicios", "max": 52000},
                {"name": "Examen VideoLlamada", "max": 25000},
            ]
        },
        "series": [
            {
                "name": "Aprendizaje Actual Vs Proyectado",
                "type": "radar",
                "data": [
                    {
                        "value": [2000, 3000, 2000, 3500, 15000, 11800],
                        "name": "Estado Actual de Alumno",
                    },
                    {
                        "value": [6500, 16000, 30000, 38000, 52000, 25000],
                        "name": "Meta de Aprendizaje",
                    },
                ],
            }
        ],
    }
    st_echarts(option, height="500px")
