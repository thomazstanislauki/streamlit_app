import streamlit as st
import pandas as pd
import plotly.express as px

st.image('/Users/thomazhenrique/Downloads/pether_thiel.png', width=620)

st.title("O maior desafio de Davi não é Golias, é o próprio Davi. ")
st.markdown("Li o [último relatório econômico-financeiro da ANS](https://www.gov.br/ans/pt-br/assuntos/noticias/numeros-do-setor/ans-divulga-dados-economico-financeiros-relativos-ao-3o-trimestre-de-2024) sobre seguradoras de saúde para você não precisar ler.")
st.text(" Antecipando: se você já é do mercado, não espere nenhuma análise genial sobre o mercado.")
st.text("Meu objetivo é trazer luz para dados que vão além das headlines bonitas de rodadas de investimento e levar ao mundo a reflexão pessoal que os dados me geraram sobre o poder da coragem e self belief para mover o mundo e a saúde para frente.")


st.divider()

st.subheader("Capítulo 1: Jeff Bezos is wrong. Not day 1. It's day 0.1")

st.text("Fundada em 2020, Alice atingiu seus primeiros 10k beneficiários em 1Q23.") 
st.markdown("Em 2Q23, [Alice adquire QSaúde](https://alice.com.br/blog/imprensa/alice-compra-carteira-clientes-qsaude/) e faz o grande salto de sua história em número de beneficiários saindo de ~10k para ~27k. Desde então, Alice adicionou 8.1k vidas (+30%) e finalizou 3Q24 com 34.7k beneficiários.")

st.text("Já Sami inicia suas operações em 2021 e 1Q23 atinge ~17k beneficiários, 70% a mais que Alice no mesmo trimestre. Vale destacar que até esse momento Alice operava B2C.")

# Create DataFrame for beneficiaries growth
beneficiaries_data = pd.DataFrame({
    'Trimestre': ['1Q21', '2Q21', '3Q21', '4Q21', '1Q22', '2Q22', '3Q22', '4Q22', 
                '1Q23', '2Q23', '3Q23', '4Q23', '1Q24', '2Q24', '3Q24'],
    'Alice': [1.3, 2.4, 3.8, 6.5, 8.2, 9.4, 10.0, 10.0, 9.8, 26.6, 26.2, 26.1, 27.2, 31.0, 34.7],
    'Sami': [0.8, 2.0, 3.6, 5.7, 7.7, 10.4, 12.8, 15.0, 16.7, 18.8, 19.9, 21.0, 21.3, 21.6, 20.7]
})

# Create color map
color_map = {'Alice': '#FF1493', 'Sami': '#FFB6C1'}

# Melt the DataFrame for Plotly
beneficiaries_melted = pd.melt(beneficiaries_data, 
                              id_vars=['Trimestre'], 
                              value_vars=['Alice', 'Sami'],
                              var_name='Operadora', 
                              value_name='Beneficiários (k)')

# Create grouped bar chart
fig = px.bar(beneficiaries_melted, 
             x='Trimestre', 
             y='Beneficiários (k)', 
             color='Operadora',
             color_discrete_map=color_map,
             barmode='group',
             title='Crescimento em número de beneficiários')

st.plotly_chart(fig)


st.text("Em receita e beneficiários, Alice e Sami hoje somam 0.1% da Saúde Suplementar brasileira.")

df = pd.DataFrame(
    [
        {"Nome Coluna": "Sami", "Beneficiários": "20.781", "Receita Total (acumulado até 3Q24)": "R$ 84.794.661"},
        {"Nome Coluna": "Alice", "Beneficiários": "34.741", "Receita Total (acumulado até 3Q24)": "R$ 257.107.166"},
        {"Nome Coluna": "Mercado Total", "Beneficiários": "50.691.591", "Receita Total (acumulado até 3Q24)": "R$ 261.340.143.528"},
        {"Nome Coluna": "Alice + Sami vs Total", "Beneficiários": "0.10%", "Receita Total (acumulado até 3Q24)": "0.13%"}
    ]
)

st.dataframe(df)




st.text("Pista infinita pela frente. Então, quão rápido Sami e Alice estão correndo nessa pista? ")

st.divider()

st.subheader("Capítulo 2: Outgrow Goliath and peers")

st.text ("TL;DR:")
st.text("- setor cresceu 12% em receita 3Q23 vs 3Q24.")
st.text("- CAGR entre 3Q19 e 3Q24: 8.04%.")
st.text ("- top 3 seguradoras em núm. segurados, Hapvida lidera em crescimento de receita: 13% entre 23 e 24.")

#tentativa
chart_data = pd.DataFrame({
    'Operadora': ['Bradesco (5711)', 'Notre Dame (359017)', 'Hapvida (368253)', 'Outras operadoras'] * 6,
    'Ano': [2019] * 4 + [2020] * 4 + [2021] * 4 + [2022] * 4 + [2023] * 4 + [2024] * 4,
    'Receita em R$ bilhões': [
        # 2019
        19.0, 5.1, 4.0, 149.3,
        # 2020
        19.7, 6.9, 4.5, 149.3,
        # 2021
        22.0, 7.7, 5.3, 159.9,
        # 2022
        23.0, 8.5, 7.7, 163.7,
        # 2023
        26.1, 10.6, 9.1, 187.5,
        # 2024
        28.7, 10.5, 10.3, 211.6
    ]
})

# Calculate yearly totals
yearly_totals = chart_data.groupby('Ano')['Receita em R$ bilhões'].sum().round(1)

fig = px.bar(chart_data, x='Ano', y='Receita em R$ bilhões', color='Operadora', 
             title='Receita acumulada até 3Q',
             barmode='stack')

# Add total annotations above each bar stack
for year in yearly_totals.index:
    fig.add_annotation(
        x=year,
        y=yearly_totals[year],
        text=f'{yearly_totals[year]}',
        showarrow=False,
        yshift=10
    )

st.plotly_chart(fig)

st.subheader("Maçã com Maça")
st.write("Para uma comparação mais justa, olharemos para operadoras de Médio Porte (20 - 100 mil beneficiários) e modalidade Medicina de Grupo (vendem para PF e/ou PJ com rede própria ou terceirizada). Alice e Sami pertencem a esse recorte.")

st.write("TL;DR:")

st.write("- 3Q23 vs 3Q24, pares registraram queda de 1% em receita. R$8.6bi vs R$8.8bi no ano anterior")

st.write("- Alice e Sami registraram crescimento de 77% e 45%, respectivamente")

st.write("- Interessante notar como em 2022 ambas estavam coladas em receita. Mas, em 2023 e 2024 Alice dispara")

chart_data = pd.DataFrame({
    'Operadora': ['Alice (421928)', 'Sami (422398)'] * 6,
    'Ano': [2019] * 2 + [2020] * 2 + [2021] * 2 + [2022] * 2 + [2023] * 2 + [2024] * 2,
    'Receita em R$ milhões': [
        # 2019
        0.0, 0.0,
        # 2020
        0.49, 0.0,
        # 2021
        12.5, 5.4,
        # 2022
        57.0, 56.2,
        # 2023
        144.6, 58.7,
        # 2024
        257.1, 84.7
    ]
})

fig = px.bar(chart_data, x='Ano', y='Receita em R$ milhões', color='Operadora',
             title='Receita acumulada até 3Q',
             barmode='group')

# Calculate yearly totals
# Get data for each operadora by year
alice_data = chart_data[chart_data['Operadora'] == 'Alice (421928)'].set_index('Ano')['Receita em R$ milhões']
sami_data = chart_data[chart_data['Operadora'] == 'Sami (422398)'].set_index('Ano')['Receita em R$ milhões']

# Add annotations for each bar
# Update color scheme for Alice and Sami
fig.update_traces(marker_color='#FF1493', selector=dict(name='Alice (421928)'))
fig.update_traces(marker_color='red', selector=dict(name='Sami (422398)'))

for year in alice_data.index:
    # Alice annotation
    fig.add_annotation(
        x=year,
        y=alice_data[year],
        text=f'{alice_data[year]:.1f}',
        showarrow=False,
        yshift=10,
        xshift=-15  # Shift left for Alice bar
    )
    # Sami annotation  
    fig.add_annotation(
        x=year,
        y=sami_data[year],
        text=f'{sami_data[year]:.1f}',
        showarrow=False,
        yshift=10,
        xshift=15  # Shift right for Sami bar
    )

st.plotly_chart(fig)

st.divider()

st.subheader("Capítulo 3: Se correr o bicho pega, se crescer o bicho come?")
st.write("Vetor 1: Sinistralidade")

#line chart data

line_data = pd.DataFrame({
    'Operadora': ['Alice', 'Sami', 'Operadoras Pares', 'Mercado'] * 6,
    'Ano': [2019] * 4 + [2020] * 4 + [2021] * 4 + [2022] * 4 + [2023] * 4 + [2024] * 4,
    'Sinistralidade (%)': [
        # 2019
        0, 0, 78.3, 82.0,
        # 2020 
        63.5, 80.0, 71.7, 85.0,
        # 2021
        107.8, 82.0, 80.2, 87.0,
        # 2022
        118.8, 85.0, 80.7, 89.0,
        # 2023
        84.5, 95.8, 77.3, 85.4,
        # 2024
        85.3, 92.1, 79.5, 83.1
    ]
})

fig_line = px.line(line_data, x='Ano', y='Sinistralidade (%)', color='Operadora',
                   title='Sinistralidade acumulada até último período de cada ano',
                   markers=True)

st.plotly_chart(fig_line)


st.divider()

st.subheader("Capítulo 4: Built different. ")

st.divider()

st.subheader("Capítulo 5: Quem quer rir tem que fazer rir…")
st.write("check out this [link](%s)" % url)

st.divider()

