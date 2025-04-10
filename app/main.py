# main.py
import plotly.express as px
import streamlit as st
import pandas as pd
import app.utils.texts as text

# st.image('/Users/thomazhenrique/Downloads/pether_thiel.png', width=620)

text.intro()

st.divider()

text.chapter_1(section=1)

# Create DataFrame for beneficiaries growth
beneficiaries_data = pd.DataFrame(
    {
        "Trimestre": [
            "1Q21",
            "2Q21",
            "3Q21",
            "4Q21",
            "1Q22",
            "2Q22",
            "3Q22",
            "4Q22",
            "1Q23",
            "2Q23",
            "3Q23",
            "4Q23",
            "1Q24",
            "2Q24",
            "3Q24",
            "4Q24",
        ],
        "Alice": [
            1.3,
            2.4,
            3.8,
            6.5,
            8.2,
            9.4,
            10.0,
            10.0,
            9.8,
            26.6,
            26.2,
            26.1,
            27.2,
            31.0,
            34.7,
            40,
        ],
        "Sami": [
            0.8,
            2.0,
            3.6,
            5.7,
            7.7,
            10.4,
            12.8,
            15.0,
            16.7,
            18.8,
            19.9,
            21.0,
            21.3,
            21.6,
            20.7,
            0,
        ],
    }
)

# Create color map
color_map = {"Alice": "#bd037e", "Sami": "#ff5852"}

# Melt the DataFrame for Plotly
beneficiaries_melted = pd.melt(
    beneficiaries_data,
    id_vars=["Trimestre"],
    value_vars=["Alice", "Sami"],
    var_name="Operadora",
    value_name="Beneficiários (k)",
)

# Create grouped bar chart
fig = px.bar(
    beneficiaries_melted,
    x="Trimestre",
    y="Beneficiários (k)",
    color="Operadora",
    color_discrete_map=color_map,
    barmode="group",
    title="Número de Segurados no final do período",
)

st.plotly_chart(fig)

text.chapter_1(section=2)

df = pd.DataFrame(
    [
        {
            "Nome Coluna": "Sami",
            "Beneficiários": "20.781",
            "Receita 2024": "R$ 84.794.661",
        },
        {
            "Nome Coluna": "Alice",
            "Beneficiários": "34.741",
            "Receita 2024": "R$ 257.107.166",
        },
        {
            "Nome Coluna": "Mercado Total",
            "Beneficiários": "50.691.591",
            "Receita 2024": "R$ 261.340.143.528",
        },
        {
            "Nome Coluna": "Alice + Sami vs Total",
            "Beneficiários": "0.10%",
            "Receita 2024": "0.13%",
        },
    ]
)

st.dataframe(df)

text.chapter_1(section=3)

st.divider()

text.chapter_2(section=1)

# Create chart data for market trends
chart_data = pd.DataFrame(
    {
        "Operadora": [
            "Outras operadoras",
            "Bradesco (5711)",
            "SUL AMERICA (6246)",
            "AMIL (326305)",
            "Hapvida (368253)",
            "Notre Dame (359017)",
        ]
        * 5,
        "Ano": [2020] * 6 + [2021] * 6 + [2022] * 6 + [2023] * 6 + [2024] * 6,
        "Receita em R$ bilhões": [
            # 2020
            163.8,
            26.4,
            19.1,
            19.7,
            6.2,
            9.4,
            # 2021
            181.6,
            29.8,
            20.3,
            20.0,
            7.8,
            10.5,
            # 2022
            177.0,
            31.0,
            23.0,
            18.6,
            10.5,
            11.6,
            # 2023
            209.0,
            35.3,
            27.3,
            21.3,
            12.2,
            14.0,
            # 2024
            168.6,
            28.7,
            23.2,
            19.9,
            10.3,
            10.6,
        ],
    }
)

# Calculate yearly totals
yearly_totals = chart_data.groupby("Ano")["Receita em R$ bilhões"].sum().round(1)

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

# Add total annotations above each bar stack
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

# Create startup revenue data
startup_revenue = pd.DataFrame(
    {
        "Operadora": ["Alice", "Sami"] * 5,
        "Ano": [2020] * 2 + [2021] * 2 + [2022] * 2 + [2023] * 2 + [2024] * 2,
        "Receita em R$ milhões": [
            # 2020
            1.4,
            0.0,
            # 2021
            22.0,
            10.6,
            # 2022
            74.3,
            71.0,
            # 2023
            219.3,
            83.7,
            # 2024
            257.1,
            84.8,
        ],
    }
)

fig_startup_revenue = px.bar(
    startup_revenue,
    x="Ano",
    y="Receita em R$ milhões",
    color="Operadora",
    title="Receita das Startups por Ano",
    barmode="group",
    color_discrete_map={"Alice": "#bd037e", "Sami": "#ff5852"},
)

st.plotly_chart(fig_startup_revenue)

text.chapter_2(section=3)

# Bar chart data for premium per beneficiary
bar_data = pd.DataFrame(
    {
        "Período": ["4Q21", "4Q21", "4Q22", "4Q23", "3Q24", "4Q22", "4Q23", "3Q24"],
        "Operadora": [
            "Sami",
            "Alice",
            "Sami",
            "Sami",
            "Sami",
            "Alice",
            "Alice",
            "Alice",
        ],
        "Prêmio por beneficiário (k)": [
            round(1393 / 1000, 1),
            round(2838 / 1000, 1),
            round(4257 / 1000, 1),
            round(3613 / 1000, 1),
            round(3832 / 1000, 1),
            round(6220 / 1000, 1),
            round(8045 / 1000, 1),
            round(6053 / 1000, 1),
        ],
    }
)
# Add labels on top of each bar
bar_data["Label"] = bar_data["Prêmio por beneficiário (k)"].apply(lambda x: f"{x:.1f}")

# Create bar chart
fig_bar = px.bar(
    bar_data,
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

# Premium comparison with high-end competitors
bar_data = pd.DataFrame(
    {
        "Período": [
            "4Q21",
            "4Q22",
            "4Q23",
            "3Q24",
            "4Q21",
            "4Q22",
            "4Q23",
            "3Q24",
            "4Q21",
            "4Q22",
            "4Q23",
            "3Q24",
            "4Q21",
            "4Q22",
            "4Q23",
            "3Q24",
        ],
        "Empresa": [
            "Alice (421928)",
            "Alice (421928)",
            "Alice (421928)",
            "Alice (421928)",
            "OMINT (359661)",
            "OMINT (359661)",
            "OMINT (359661)",
            "OMINT (359661)",
            "CARE PLUS (379956)",
            "CARE PLUS (379956)",
            "CARE PLUS (379956)",
            "CARE PLUS (379956)",
            "SUL AMERICA (6246)",
            "SUL AMERICA (6246)",
            "SUL AMERICA (6246)",
            "SUL AMERICA (6246)",
        ],
        "Prêmio por beneficiário (k)": [
            round(2838 / 1000, 1),
            round(6220 / 1000, 1),
            round(8045 / 1000, 1),
            round(6053 / 1000, 1),
            round(12927 / 1000, 1),
            round(15897 / 1000, 1),
            round(14151 / 1000, 1),
            round(12927 / 1000, 1),
            round(9020 / 1000, 1),
            round(10188 / 1000, 1),
            round(9030 / 1000, 1),
            round(8534 / 1000, 1),
            round(5597 / 1000, 1),
            round(6444 / 1000, 1),
            round(5788 / 1000, 1),
            round(4977 / 1000, 1),
        ],
    }
)
# Add labels on top of each bar
bar_data["Label"] = bar_data["Prêmio por beneficiário (k)"].apply(lambda x: f"R${x}")

# Create bar chart
fig_bar = px.bar(
    bar_data,
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

# Line chart data for sinistralidade
line_data = pd.DataFrame(
    {
        "Operadora": ["Alice", "Sami", "Operadoras Pares", "Mercado"] * 6,
        "Ano": [2019] * 4
        + [2020] * 4
        + [2021] * 4
        + [2022] * 4
        + [2023] * 4
        + [2024] * 4,
        "Sinistralidade (%)": [
            # 2019
            0,
            0,
            78.3,
            82.0,
            # 2020
            63.5,
            80.0,
            71.7,
            85.0,
            # 2021
            107.8,
            82.0,
            80.2,
            87.0,
            # 2022
            118.8,
            85.0,
            80.7,
            89.0,
            # 2023
            84.5,
            95.8,
            77.3,
            85.4,
            # 2024
            85.3,
            92.1,
            79.5,
            83.1,
        ],
    }
)

fig_line = px.line(
    line_data,
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
bar_data = pd.DataFrame(
    {
        "Ano": [2020, 2020, 2021, 2021, 2024, 2022, 2023, 2024],
        "Operadora": [
            "Sami",
            "Alice",
            "Sami",
            "Sami",
            "Sami",
            "Alice",
            "Alice",
            "Alice",
        ],
        "Receita em R$ milhões": [1.4, 0.0, 22.0, 10.6, 257.1, 74.3, 219.3, 84.8],
    }
)

fig_bar = px.bar(
    bar_data,
    x="Ano",
    y="Receita em R$ milhões",
    color="Operadora",
    title="Receita acumulada até último período de cada ano",
    barmode="group",
)

for i in range(len(bar_data)):
    fig_bar.add_annotation(
        x=bar_data["Ano"][i],
        y=bar_data["Receita em R$ milhões"][i],
        text=f"{bar_data['Receita em R$ milhões'][i]}",
        showarrow=False,
        yshift=10,
    )

st.plotly_chart(fig_bar, config={"responsive": True})
