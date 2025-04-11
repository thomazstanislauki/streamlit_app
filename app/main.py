# main.py
import plotly.express as px
import streamlit as st
import pandas as pd
import app.utils.texts as text
import app.data.data as data
import app.utils.utils as utils

# st.image('/Users/thomazhenrique/Downloads/pether_thiel.png', width=620)

utils.urls_style()
utils.sidebar()

text.intro()

st.divider()

text.chapter_1(section=1)

fig = px.bar(
    data.get_beneficiaries(),
    x="Trimestre",
    y="Beneficiários (k)",
    color="Operadora",
    color_discrete_map={"Alice": "#bd037e", "Sami": "#ff5852"},
    barmode="group",
    title="Número de Segurados no final do período",
)

st.plotly_chart(fig)

text.chapter_1(section=2)

st.dataframe(data.get_revenue())

text.chapter_1(section=3)

st.divider()

text.chapter_2(section=1)

chart_data = data.get_market_trends()

fig = px.bar(
    chart_data,
    x="Ano",
    y="Receita em R$ bilhões",
    color="Operadora",
    title="Receita acumulada até último período de cada ano",
    barmode="stack",
    color_discrete_map={
        "Outras operadoras": "#6f2da8",
        "Bradesco (5711)": "#cc092f",
        "SUL AMERICA (6246)": "#d15321",
        "AMIL (326305)": "#461bff",
        "Hapvida (368253)": "#0063af",
        "Notre Dame (359017)": "#eb6032",
    },
)

yearly_totals = data.get_yearly_totals(chart_data)

for year in yearly_totals.index:
    fig.add_annotation(
        x=year,
        y=yearly_totals[year],
        text=f"{yearly_totals[year]:.1f}",
        showarrow=False,
        yshift=10,
    )

st.plotly_chart(fig)

text.chapter_2(section=2)

fig_startup_revenue = px.bar(
    data.get_startup_revenue(),
    x="Ano",
    y="Receita em R$ milhões",
    color="Operadora",
    title="Receita das Startups por Ano",
    barmode="group",
    color_discrete_map={"Alice": "#bd037e", "Sami": "#ff5852"},
)

st.plotly_chart(fig_startup_revenue)

text.chapter_2(section=3)

fig_bar = px.bar(
    data.get_premium_by_beneficiary(),
    x="Período",
    y="Prêmio por beneficiário (k)",
    color="Operadora",
    title="Média de prêmio por beneficiário",
    color_discrete_map={"Sami": "#ff5852", "Alice": "#bd037e"},
    barmode="group",
    text_auto=True,
)
fig_bar.update_layout(uniformtext_minsize=8, uniformtext_mode="hide")
fig_bar.update_traces(textposition="outside")

st.plotly_chart(fig_bar)

fig_bar = px.bar(
    data.get_premium_comparison(),
    x="Período",
    y="Prêmio por beneficiário (k)",
    color="Empresa",
    title="Média de prêmio por beneficiário",
    color_discrete_map={
        "Alice (421928)": "#bd037e",
        "OMINT (359661)": "#1b3069",
        "CARE PLUS (379956)": "#0179cf",
        "SUL AMERICA (6246)": "#d15321",
    },
    barmode="group",
    text_auto=True,
)
fig_bar.update_layout(uniformtext_minsize=8, uniformtext_mode="hide")
fig_bar.update_traces(textposition="outside")

text.chapter_2(section=4)

st.plotly_chart(fig_bar)

text.chapter_2(section=5)

st.divider()

text.chapter_3()

fig_line = px.line(
    data.get_claims(),
    x="Ano",
    y="Sinistralidade (%)",
    color="Operadora",
    title="Sinistralidade acumulada até último período de cada ano",
    markers=True,
)

st.plotly_chart(fig_line)

st.divider()

text.chapter_4()
# Comparar despesas de time vs outras operadoras. Isso dá pra puxar via DRE (slide 8 ou 9, se não me engano da ANS)
# Insight aqui é que enquanto outras operadoras são "financeiras" com rede credenciada, a Alice e Sami se comportam como empresas de tech que operam no setor de saúde
# Dúvida: até quando esses investimentos em time/produto vão ser necessários? Alguma hora a chave vira?

st.divider()

text.chapter_5()
# Despesas de comercialização (corretagem, incentivos tbem dá pra puxar via DRE) significativamente maiores que outras operadoras

st.divider()

text.final_chapter()

# Final revenue comparison
revenue_comparison = data.get_revenue_comparison()

fig_bar = px.bar(
    revenue_comparison,
    x="Ano",
    y="Receita em R$ milhões",
    color="Operadora",
    title="Receita acumulada até último período de cada ano",
    barmode="group",
)

for i in range(len(revenue_comparison)):
    fig_bar.add_annotation(
        x=revenue_comparison["Ano"][i],
        y=revenue_comparison["Receita em R$ milhões"][i],
        text=f"{revenue_comparison['Receita em R$ milhões'][i]}",
        showarrow=False,
        yshift=10,
    )

st.plotly_chart(fig_bar, config={"responsive": True})
