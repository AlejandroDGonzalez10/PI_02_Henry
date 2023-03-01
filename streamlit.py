import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import pickle
from pathlib import Path
import altair as alt
import plotly.graph_objects as og
import plotly.graph_objs as go
from datetime import date, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA



spx500 = pd.read_csv('spx_yf.csv')
spx = pd.read_csv('spx.csv')
spx500stock = pd.read_csv('stockspy.csv')
spx500date = pd.read_csv('spx_date.csv')


st.title('Analisis de mercado del SPX500')
st.header('Análisis del mercado bursátil de los últimos 23 años')
st.write('Este dashboard presenta un análisis de la situación del mercado bursátil en los últimos 23 años para las empresas pertenecientes al índice SP500 (Standard & Poor\'s 500 Index). Se han analizado diferentes focos, incluyendo la variación de precios en el tiempo, la comparación entre distintas acciones y el cálculo de estadísticas bursátiles, entre otros.')


menu = ['Análisis del SPX500', 'Recomendaciones de inversión']
selection = st.sidebar.selectbox("Seleccione una opción", menu)

if selection == 'Análisis del SPX500':
    st.title('Análisis del SPX500')
    
    
    # Crear gráfico de precios
    fig = px.line(spx500, x='Date', y="Close", title="Precio de cierre del SPX500")
    st.plotly_chart(fig)

    
    # Correlación entre símbolos
    
    
    # Histograma de retornos diarios
    spx500 = pd.read_csv('spx_yf.csv', parse_dates=['Date'])
    spx500['Return'] = spx500['Adj Close'].pct_change()

    plt.hist(spx500['Return'], bins=50)
    plt.xlabel('Retorno diario')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de los retornos diarios del S&P 500')
    
    

    

    # Gráfico de barras para el volumen
    fig = px.bar(spx500, x='Date', y='Volume', title='Volumen del SPX500 en los últimos 23 años')

 
    # Cambiar el nombre de los ejes
    fig.update_xaxes(title_text='Año')
    fig.update_yaxes(title_text='Volumen en mil millones')
    st.plotly_chart(fig)


    data = {'Salud': 110.658028, 'XLU': 87.195233, 'Bienes de consumo básicos': 77.123092,
        'Energía': 65.037446, 'Servicios financieros': 117.162117, 'Industriales': 117.753514,
        'Materiales': 114.970844, 'Inmobiliario': 62.605929, 'Tecnología': 263.845669,
        'Consumo discrecional': 104.365176}
    sector_gains = pd.Series(data)

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(sector_gains.index, sector_gains.values)
    ax.set_xticklabels(sector_gains.index, rotation=90, ha='right')
    ax.set_ylabel('Ganancias (%)')
    ax.set_title('Ganancias de los sectores del SPX500')
    plt.tight_layout()
    plt.show()

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)

   
    
    # Calcular el rendimiento diario de cada empresa
    daily_returns = pd.read_csv('spx_yf.csv')
    for ticker in data.columns:
        daily_returns[ticker] = data[ticker].pct_change()
    # Gráfico de la variación de precios de todas las empresas a lo largo del tiempo
    st.write('Variación de precios de todas las empresas a lo largo del tiempo')
    st.line_chart(data)
    # Gráfico del rendimiento diario de cada empresa a lo largo del tiempo
    st.write('Rendimiento diario de todas las empresas a lo largo del tiempo')
    st.line_chart(daily_returns)



# # cargar datos previamente descargados o almacenados en la nube
# df_sp500 = pd.read_csv('sp500_data.csv')
# # filtrar empresas con criterios de inversión específicos
# filtro = (df_sp500["Market Cap"] > 1000000000) & (df_sp500["Price/Earnings"] < 20)
# empresas_filtradas = df_sp500[filtro]
# # calcular el retorno de inversión esperado y el riesgo
# empresas_filtradas["ROI Esperado"] = empresas_filtradas["Price Target"] / empresas_filtradas["Last Price"] - 1
# empresas_filtradas["Riesgo"] = empresas_filtradas["Beta"] * empresas_filtradas["Volatility"]
# # ordenar empresas por ROI esperado
# empresas_ordenadas_roi = empresas_filtradas.sort_values(by=["ROI Esperado"], ascending=False).reset_index(drop=True)
# # ordenar empresas por riesgo
# empresas_ordenadas_riesgo = empresas_filtradas.sort_values(by=["Riesgo"]).reset_index(drop=True)
# # mostrar mejores recomendaciones basadas en ROI esperado
# st.write("Mejores recomendaciones basadas en ROI esperado:")
# st.dataframe(empresas_ordenadas_roi[["Company", "ROI Esperado"]].head(10))
# # mostrar mejores recomendaciones basadas en riesgo
# st.write("Mejores recomendaciones basadas en riesgo:")
# st.dataframe(empresas_ordenadas_riesgo[["Company", "Riesgo"]].head(10))


# if selection == 'Recomendaciones de inversión':

#     st.title('Recomendaciones de inversión')
  
#     # Cargar los datos de precios de cierre ajustados de las empresas de SPX desde 2000 hasta la fecha actual
#     spx500stock = pd.read_csv('stockspy2.csv')
    
   
#     # Seleccionar las empresas con los mayores retornos anualizados
#     n_recommendations = 10
#     top_returns = spx500stock.nlargest(n_recommendations, columns='Adj Close')

#     # Crear un data frame con la información de las empresas seleccionadas
#     recommendations = top_returns[['Symbol', 'Sector', 'Industria', 'Adj Close']].reset_index()
#     recommendations.columns = ['Symbol', 'Empresa', 'Sector', 'Industria', 'Retorno anualizado']

#     # Mostrar el data frame en una aplicación de Streamlit
#     st.write(recommendations)
    
    
#     st.title('Recomendaciones de periodo de tiempo de 5 años')
  
#     # Cargar los datos de precios de cierre ajustados de las empresas de SPX desde 2000 hasta la fecha actual
#     sp500stock = pd.read_csv('stockspy3.csv')
    
   
#     # Seleccionar las empresas con los mayores retornos anualizados
#     n_recommendations = 10
#     top_returns = sp500stock.nlargest(n_recommendations, columns='Adj Close')

#     # Crear un data frame con la información de las empresas seleccionadas
#     recommendations = top_returns[['Symbol', 'Sector', 'Industria', 'Adj Close']].reset_index()
#     recommendations.columns = ['Symbol', 'Empresa', 'Sector', 'Industria', 'Retorno anualizado']

#     # Mostrar el data frame en una aplicación de Streamlit
#     st.write(recommendations)