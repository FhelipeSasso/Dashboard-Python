import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")

# faturamento por unidade
# tipo de produto mais vendido, contribuiçao por filial
# desempenho das formas de pagamento
# avaliaçao das filiais

df = pd.read_csv("d:/sasel/Documents/DashboardPy/supermarket_sales.csv", sep=";", decimal = ",")
# converter object para data
df["Date"] = pd.to_datetime(df["Date"])
# ordenaçao
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered

# colunas

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# faturamento por unidade/rendimento de filiais
fig_date = px.bar(df_filtered, x = "Date", y = "Total", color = "City", title="Faturamento diario")
col1.plotly_chart(fig_date, use_container_width=True)

# orientation =  "h" para horizontal 

fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# .sum() e groupby para fazer o agrupamento e soma

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(df_filtered, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

# gráfico em pizza

fig_maru = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_maru, use_container_width=True)

# rendimento por cidade

city_rating = df_filtered.groupby("City")[["Total"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)
