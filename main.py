import pandas as pd
import streamlit as st



@st.cache_data
def f_ex__met_data():
    df = pd.read_csv("data_raw.csv")

    total_vendido = df["total"].sum()

    cantidad_vendida = df["cantidad"].sum()

    mejor_producto = df.groupby(df["producto"])["total"].sum().idxmax()


    data = {
        "met_1" : total_vendido,
        "met_2" : cantidad_vendida,
        "met_3" : mejor_producto
    }

    return(data)



@st.cache_data
def f_ex__grf_1_data():
    df = pd.read_csv("data_raw.csv")

    productos_ventas = df.groupby(df["producto"])["total"].sum().sort_values(ascending=False).to_dict()


    data = pd.DataFrame({
        "Producto" : list(productos_ventas.keys()),
        "Ventas ($)" : list(productos_ventas.values())
    }) 

    return (data)



@st.cache_data
def f_ex__grf_2_data():
    df = pd.read_csv("data_raw.csv")

    dia_semana_ventas = df.groupby(df["dia_semana"])["total"].sum().to_dict()


    data = pd.DataFrame({
        "Dia de la Semana" : list(dia_semana_ventas.keys()),
        "Ventas ($)" : list(dia_semana_ventas.values())
    })

    return (data)
