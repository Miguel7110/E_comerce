import pandas as pd
import streamlit as st
import graficos as graf

st.set_page_config(layout= 'wide')

# CSS css
#def load_css(file):
    #with open(file) as f:
        #st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#load_css('style.css')


st.title('Análisis de Ventas y Rendimiento 📈')


st.sidebar.image('src/Python_PNG.png')


# habrir df y darle formato a la columna de tiempo
df_final = pd.read_csv('src/df_final.csv', sep=',')
df_final['fecha_compra'] = pd.to_datetime(df_final['fecha_compra'], errors='coerce')
df_final['año_compra'] = df_final['año_compra'].astype(str)



# filtro para las CIUDADES
estados = sorted(list(df_final['ciudad_nombre'].unique()))
estado = st.sidebar.multiselect("Estates", estados)

if estado: 
    df_final = df_final[df_final['ciudad_nombre'].isin(estado)]

# filtro para el tipo de PRODUCTO
productos = sorted(list(df_final['tipo_producto'].unique()))
productos.insert(0,'All Products')
producto = st.sidebar.selectbox('Select Produc', productos)

if producto != 'All Products':
    df_final = df_final[df_final['tipo_producto'] == producto]


# filtro para los AÑOS
años = sorted(list(df_final['año_compra'].unique()))
año = st.sidebar.multiselect('Years', años)

if año:
    df_final = df_final[df_final['año_compra'].isin(año)]
    

# LLAMAR LOS GRAFICOS
grafico_linea = graf.pregunta_2(df_final)
grafico_barra = graf.pregunta_3(df_final)
grafico_mapa = graf.pregunta_4(df_final)
grafico_pizza = graf.pregunta_1(df_final)
grafico_d = graf.grafico_d(df_final)


# CREANDO 2 COLUMNAS y mastral grafici dentro de las columnas 
col1, col2 = st.columns([2, 1])
with col1:
    #st.plotly_chart(grafico_d, use_container_width=True)
    st.plotly_chart(grafico_mapa, use_container_width=True)
with col2:
    st.plotly_chart(grafico_pizza, use_container_width=True)
    

#MOSTRAL LOS GRAFICOS inferiores que no estan dentro de las columnas.
st.plotly_chart(grafico_linea, use_container_width=True)
st.plotly_chart(grafico_barra, use_container_width=True)
