import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel("parimonio x receita.xlsx", sheet_name="Planilha1")

df = df.groupby(['id'])[["Patrimonio Liq ($Bn)", "receita"]].sum().reset_index()
df = df.sort_values(by="receita", ascending=False)

df["Patrimonio Liq ($Bn)"] = df["Patrimonio Liq ($Bn)"] * 1000
df = df[df["Patrimonio Liq ($Bn)"] != 0]
df = df[df["receita"] != 0]

scatter = alt.Chart(df).mark_circle(size=100).encode(
    x=alt.X("Patrimonio Liq ($Bn):Q", title="Patrimônio Líquido ($Bn)"),
    y=alt.Y("receita:Q", title="Receita"),
    tooltip=[
        alt.Tooltip("id:N", title="ID"),
        alt.Tooltip("Patrimonio Liq ($Bn):Q", title="Patrimônio Líq", format=",.2f"),
        alt.Tooltip("receita:Q", title="Receita", format=",.2f")
    ]
)

labels = alt.Chart(df).mark_text(
    align="center",
    baseline="bottom",
    dy=-5,  
    size=12
).encode(
    x="Patrimonio Liq ($Bn):Q",
    y="receita:Q",
    text="id:N"
)

final_chart = (scatter + labels).properties(
    title="Gráfico de Receita vs Patrimônio Líquido"
).interactive()


st.subheader("Gráfico Dispersão com Rótulos")
st.altair_chart(final_chart, use_container_width=True)

df["Patrimonio Liq ($Bn)"] = df["Patrimonio Liq ($Bn)"].map("{:,.2f}".format)
df["receita"] = df["receita"].map("{:,.2f}".format)
st.write(df)
