import streamlit as st
import pytrends
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
