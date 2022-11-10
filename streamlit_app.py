import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Mando", page_icon="⚙️")

#TITULO
st.title('Novus Mando ⚙️ - GrupoIberoPistacho 🌰')

#SUBTITULO
st.write('---')
st.write("""
**Tecnología Novus Solutions**
- ⚙️: `Monitores de Operación por Horas, de Eficiencia Energética y de Productos` con `Alarmas de Baja Producción e Ineficiencias Energéticas` y `Recomendaciones para más Ventas y Reducción de Gastos Energéticos`
""")
st.write('---')

st.markdown('Versión Ejemplo Borrador')

option = st.selectbox(
    'Elige la PLANTA DE PROCESADO de análisis',
    ('Toledo', 'Talavera', 'Madrid', 'Albacete', 'Vigo'))
if option:
    st.write('Datos históricos disponibles para la PLANTA de ', option, 'desde el día/mes/año hasta el día/mes/año')





st.markdown("Otros Monitores 📺 Personalizables para Grupo IberoPistacho: INVERSIONES + EXPLOTACIÓN + CONSULTORÍAS BÁSICAS-PLUS-PREMIUM + LEGALIZACIÓN DE POZOS + REAGRUPACIÓN PARCELARIA + TRATAMIENTOS")



#MONITOR 1: HORARIOS
st.header("Monitor 📺 de Operación por Horarios ⏰")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Hora Top 1 en Producción", value = '1am', delta='362%')
col2.metric("Hora Top 2 en Producción", "0am", "317%")
col3.metric("Hora Top 3 en Producción", "2am", "289%")


hora_seleccionada = st.slider(
    "Selecciona una hora de análisis", 0, 23)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])

st.write("Desagregación geográfica de PROVEEDORES MÁS ECONÓMICOS para la hora ", hora_seleccionada, "en la Comunidad de Madrid")

st.write(
    pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": 40.3875,
            "longitude": -3.7575416667,
            "zoom": 12,
            "pitch": 50},
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=150,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                ),
             pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                ),
        ],
        ))

st.markdown('CONCLUSIONES MONITOR HORAS:')
st.text('Las horas de mayor producción son en la madrugada (1h,0h,2h), seguido de la mañana (8am,9am,10am)')
st.text('Los proveedores más económicos requieren transporte de madrugada')


#MONITOR 2: PRODUCTOS
st.header("Monitor 📺 de Operación por Eficiencia Energética ⚡︎")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Ventas Agregadadas", value = '709.572€', delta='27Jun4Nov')
col2.metric("Toneladas Vendidas", "7Millones", "27Jun4Nov")
col3.metric("Hectáreas Cultivads", "13Millones", "27Jun4Nov")


x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Producción Julio', 'Producción Agosto', 'Producción Septiembre']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)

st.write('Top 3 de mejores productos y horas')
st.write(pd.DataFrame({
    'ID Productos más vendidos': [8, 32, 33],
    'Horas de mayores producciones': [1, 0, 2]}))



st.markdown('CONCLUSIONES MONITOR PRODUCTOS:')
st.text('3 productos (ID=8,32,33) generan más del 50% de la facturación de los últimos 130 días')

#ALARMAS
st.header("Alarmas de Baja Producción ⚠️")

alarma1, alarma2, alarma3 = st.columns(3)
alarma1.metric("Productos con mayores defectos", "1/2/18", "-85%prom")
alarma2.metric("Horarios de menor producción", "16h.13h.18h", "-73%prom")
alarma3.metric("Inventario de mayor rotación", "8-32-33", "485%prom")

chart_data = pd.DataFrame(np.random.randn(23, 3), columns=["Efectivo", "TarjetaCrédito", "TarjetaDébito"])
st.area_chart(chart_data)
    
st.write('ID TOP 1 Producto de menor facturación', 1)
st.write('ID TOP 2 Producto de menor facturación', 2)
st.write('ID TOP 3 Producto de menor facturación', 18)

st.markdown('CONCLUSIONES ALARMAS ⚠️:')
st.text('3 productos (ID=1,2,18) están concentrando la peor facturación de los últimos 130 días')
st.text('Las horas de menor facturación son en la tarde (16h,13h,18h)')



#RECOMENDACIONES
st.header("Recomendaciones para Aumentar Ventas 🧠")

rec1, rec2, rec3 = st.columns(3)
rec1.metric("Horario de mayor potencial de crecimiento", "4pm", "85%prom")
rec2.metric("Productos de mayor potencial de crecimiento", "ID_08", "73%prom")
rec3.metric("Productos sin tracción requerida para matenerse", "1-2-18", "-45%prom")

st.text('Potenciales zonas de mayor facturación')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])

st.map(df)

st.markdown('CONCLUSIONES RECOMENDACIONES 🧠:')
st.text('Se puede crecer 117% la facturación si se equlibran las ventas en los horarios de 4pm y 1pm')
st.text('Se puede aumentar la rentabilidad en 35% si se aumentan las ventas de los productos con ID_007 y ID_004')

st.caption('Todos los análisis son representativos únicamente entre el día/mes/años y el día/mes/año con sus días ☀️ y con sus noches 🌛')
