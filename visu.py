import streamlit as st
import plotly.express as px
import main
import met_script as met_s

# cd "C:\Users\Leonel Espinoza\Desktop\archivos_de_py\dashboard_serio_muestra_1"
# stremlit run "visu.py"


st.set_page_config(layout="wide")

st.subheader("Dashboard Amper")


#Metricas ↓


met_data = main.f_ex__met_data()

c1, c2, c3 = st.columns(3)

with (c1):
    met_s.f_ex__kpi_script_data(
        data={
            "Total Vendido" : {
                "v" : met_data["met_1"],
                "c" : "#9CE0FF",
                "f" : "$"
            }
        }
    )
with (c2):
    met_s.f_ex__kpi_script_data(
        data={
            "Cantidad Total Vendida" : {
                "v" : met_data["met_2"],
                "c" : "#9CFF9F"
            }
        }
    )
with (c3):
    met_s.f_ex__kpi_script_data(
        data={
            "Mejor Producto" : {
                "v" : met_data["met_3"],
                "c" : "#000000"
            }
        }
    )



#columnas grf_1, grf_2

c1, c2 = st.columns(2)

#grf_1

grf_1_data = main.f_ex__grf_1_data()

grf_1 = px.bar(
    grf_1_data,
    x="Producto",
    y="Ventas ($)",
    color_discrete_sequence=["#000000"]
)

grf_1.update_layout(
    height=400
)

with(c1):
    st.plotly_chart(grf_1)


#grf_2 ↓

grf_2_data = main.f_ex__grf_2_data()

grf_2 = px.pie(
    grf_2_data,
    names="Dia de la Semana",
    values="Ventas ($)"
)

grf_2.update_traces(
    textinfo="label + value",
    texttemplate="%{label}<br>$%{value:,.2f}",
    textfont=dict(color="#000000")
)

with (c2):
    st.plotly_chart(grf_2)