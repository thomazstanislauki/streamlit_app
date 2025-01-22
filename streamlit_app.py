import plotly.express as px
import streamlit as st
import pandas as pd

st.image('/Users/thomazhenrique/Downloads/pether_thiel.png', width=620)

st.markdown("Li o [último relatório econômico-financeiro da ANS](https://www.gov.br/ans/pt-br/assuntos/noticias/numeros-do-setor/ans-divulga-dados-economico-financeiros-relativos-ao-3o-trimestre-de-2024) sobre seguradoras de saúde para você não precisar ler.")
st.text(" Antecipando: se você já é do mercado, não espere nenhuma análise genial sobre o mercado.")
st.markdown("Meu objetivo é trazer luz para dados que vão além de headlines de PR e trazer ao mundo a reflexão que os dados me geraram sobre o poder da coragem e [delusional self belief](https://blog.samaltman.com/how-to-be-successful) para mover o mundo para frente.")


st.divider()

st.title("Capítulo 1: It's always day 0.1")

st.subheader("Alice")
st.text("Fundada em 2020, Alice alcançou a marca de 10k membros em 1Q23 ainda no modelo B2C.") 
st.markdown("Em 2Q23, [**compra carteira da QSaúde**](https://alice.com.br/blog/imprensa/alice-compra-carteira-clientes-qsaude/), pivota para B2B e mais que dobra 'na marra' o número de membros: ~10k para ~27k. Um ano e meio depois, a empresa cresceu ~50% e finalizou 2024, segundo Gui Azevedo (founder) com [40k membros.](https://www.linkedin.com/posts/guilherme-gui-azevedo-14807730_retrospectiva-2024-spotify-na-alice-activity-7282775874171531264-q6ox?utm_source=share&utm_medium=member_desktop)") 
st.write("Vale destacar que esse dado foi divulgado pela própria empresa. O último dado publicado pela ANS no dia de produção desse artigo é de 3Q24: 34.7k.")

st.subheader("Sami")
st.text("Sami inicia operação em 2021 e vive 2 anos de crescimento acelerado. 2021 sai de 0 para ~6k beneficiários. Em 2022 mais que dobra e finaliza o ano com 15k beneficiários.")
st.text("O ritmo desacelerou significativamente em 2023 e 2024. Em 2023, a empresa cresceu 30%, terminando o ano com 21k beneficiários. 2024 tem sido ainda mais difícil — encolheu em ~300 segurados se comparado ao início do ano.") 
st.text("Na data de produção deste artigo ainda não foram divulgados dados de 4Q24.") 

# Create DataFrame for beneficiaries growth
beneficiaries_data = pd.DataFrame({
    'Trimestre': ['1Q21', '2Q21', '3Q21', '4Q21', '1Q22', '2Q22', '3Q22', '4Q22', 
                '1Q23', '2Q23', '3Q23', '4Q23', '1Q24', '2Q24', '3Q24', '4Q24'],
    'Alice': [1.3, 2.4, 3.8, 6.5, 8.2, 9.4, 10.0, 10.0, 9.8, 26.6, 26.2, 26.1, 27.2, 31.0, 34.7, 40],
    'Sami': [0.8, 2.0, 3.6, 5.7, 7.7, 10.4, 12.8, 15.0, 16.7, 18.8, 19.9, 21.0, 21.3, 21.6, 20.7, 0]
})

# Create color map
color_map = {'Alice': '#bd037e', 'Sami': '#ff5852'}

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
             title='Número de Segurados no final do período')

st.plotly_chart(fig)

st.subheader("Still scratching the surface")
st.text("Alice e Sami juntas somam 0.1% da Saúde Suplementar brasileira.")

df = pd.DataFrame( 
    [
        {"Nome Coluna": "Sami", "Beneficiários": "20.781", "Receita 2024": "R$ 84.794.661"},
        {"Nome Coluna": "Alice", "Beneficiários": "34.741", "Receita 2024": "R$ 257.107.166"},
        {"Nome Coluna": "Mercado Total", "Beneficiários": "50.691.591", "Receita 2024": "R$ 261.340.143.528"},
        {"Nome Coluna": "Alice + Sami vs Total", "Beneficiários": "0.10%", "Receita 2024": "0.13%"}
    ]
)

st.dataframe(df)

st.subheader("Otimismo ou ceticismo?")
st.text("Por um lado, o mercado prova-se grande o suficiente para acomodar billion dollar-businesses.")
st.text("Por outro, são 4 anos de estrada, +230 milhões de dólares captados e nem a superfície parece ter sido atingida.") 
st.text("A ambição de ambas startups parece ser de gerar mudanças sistêmicas na saúde brasileira.")
st.text("Ao colocar a penetração em perspectiva, me questiono o quão longe estamos de mudanças tectônicas. É preciso mais 5/10 anos ou 20/30 anos? Mais $50 milhões ou $500 milhões? Alta dependência dos órgãos reguladores para acelerar a evolução do sistema?")
st.text("A clareza de quão longe estamos de mudanças substanciais em termos de tempo, regulação e investimento é essencial para tirar qualquer conclusão sobre qual será a magnitude do impacto dessas startups.") 
st.text("Elas serão os heróis que iniciam o movimento e morrem antes de vê-lo tomando proporções sem precedentes ou conseguirão 'endure for long enough' para criar e surfar a própria tailwind?")
st.divider()

st.title("Capítulo 2: Go big or go home")

st.text ("Independente de opinião, fato é que Sami e Alice tem 'mercado infinito' pela frente. Então, quão rápido elas estão capturando demanda?")
st.text("Spoiler: é muito mais rápido que o mercado e pares. Mesmo assim, é rapido suficiente?")
st.text("É isso que esse capítulo quer responder.")

st.subheader ("Setting the baseline...")
st.text("- Zoom out: entre 2020 e 2023 o mercado de saúde suplementar cresceu 30%.")
st.text("- Zoom in: 2023 foi o melhor ano desde pandemia — 17% de crescimento. Se mantivermos a sazonalidade do último ano nesse 4Q, números indicam crescimento superior a 10%, segunda melhor porformance desde 2020.")
st.text ("- Titãs: desde 2020, um terço do mercado está nas mãos das top 5 seguradoras. A Hapvida é a operadora que mais cresceu nesse intervalo: +95%. Destaque de 2024 é a Amil que nos três primeiros trimestres já atingiu ~93% da receita de 2023 vs ~80% das outras quatro. Se seguir nesse velocidade, a Amil deve crescer +20% nesse ano.")
st.caption("*Apesar da fusão entre Notre Dame e Hapvida, relatório ANS ainda reporta como operadoras distintas.*")

#tentativa
chart_data = pd.DataFrame({
    'Operadora': ['Outras operadoras', 'Bradesco (5711)', 'SUL AMERICA (6246)', 'AMIL (326305)', 'Hapvida (368253)', 'Notre Dame (359017)'] * 5,
    'Ano': [2020] * 6 + [2021] * 6 + [2022] * 6 + [2023] * 6 + [2024] * 6,
    'Receita em R$ bilhões': [
        # 2020
        163.8, 26.4, 19.1, 19.7, 6.2, 9.4,
        # 2021
        181.6, 29.8, 20.3, 20.0, 7.8, 10.5,
        # 2022
        177.0, 31.0, 23.0, 18.6, 10.5, 11.6,
        # 2023
        209.0, 35.3, 27.3, 21.3, 12.2, 14.0,
        # 2024
        168.6, 28.7, 23.2, 19.9, 10.3, 10.6 
    ]
})

# Calculate yearly totals
yearly_totals = chart_data.groupby('Ano')['Receita em R$ bilhões'].sum().round(1)

fig = px.bar(chart_data, x='Ano', y='Receita em R$ bilhões', color='Operadora', 
             title='Receita acumulada até último período de cada ano',
             barmode='stack',
             color_discrete_map={'Outras operadoras': '#6f2da8', 'Bradesco (5711)': '#cc092f', 'SUL AMERICA (6246)': '#d15321', 'AMIL (326305)': '#461bff', 'Hapvida (368253)': '#0063af', 'Notre Dame (359017)': '#eb6032'})

# Add total annotations above each bar stack
for year in yearly_totals.index:
    fig.add_annotation(
        x=year,
        y=yearly_totals[year],
        text=f'{yearly_totals[year]:.1f}',
        showarrow=False,
        yshift=10
    )

st.plotly_chart(fig)

st.subheader("Maçã com maçã")
st.write("Apesar do baseline transmitir o 'general growth rate' da indústria, Alice e Sami são uma 'espécie rara' de operadora. Tech-native, VC-backed, jovens. Então, os ângulos de comparação devem ser outros.")

st.subheader("Ângulo 1: startup vs startup", divider='gray')
st.subheader("Alice: software growth rate")

st.write("Mesmo em um setor cauteloso com mudanças e com uma camada intensa de serviços in-house [(segundo Gui Azevedo, ~1/3 do time são de profissionais de saúde)](https://drive.google.com/file/d/1pZLquHpzZulnnejWN4uV7n8T35A_ISHy/view?usp=sharing), Alice atingiu a ['taxa mágica de crescimento'](https://www.battery.com/blog/helping-entrepreneurs-triple-triple-double-double-double-to-a-billion-dollar-company/) de empresas pure software nos últimos 3 anos. A empresa vem de +1400%, +230%, +195% desde 2021 respectivamente.")
st.write("[Em um podcast publicado em Junho de 2024](https://drive.google.com/file/d/1pZLquHpzZulnnejWN4uV7n8T35A_ISHy/view?usp=sharing), Gui Azevedo projetava 500 milhões de receita para esse ano. Segundo dado [publicado no LinkedIn](https://www.linkedin.com/posts/guilherme-gui-azevedo-14807730_retrospectiva-2024-spotify-na-alice-activity-7282775874171531264-q6ox?utm_source=share&utm_medium=member_desktop), a empresa atingiu R$450 milhões de receita anualizada, +50% de crescimento YoY.")
st.write("Reforçando que esse é um dado publicado pela empresa e não pela ANS. O último report da ANS na produção desse artigoda foi de 3Q24: R$257 milhões.")

st.subheader("Sami: altos e baixos")

st.write("Ritmo acelerado: de zero a +10 milhões de receita em um ano desde sua fundação. Em 2022, a empresa cresce 570% e chega a +70 milhões de receita anual em apenas 2 anos de existência.") 
st.write("Rough year: em 2023, a Sami cresceu apenas ~18%. Isso é menos que as bilionárias Sul América (19%) e Notre Dame (20%) e em linha com as outras titãs da indústria - Hapvida, Amil e Bradesco que cresceram cerca de 14 - 15%. Segundo [matéria do Startups](https://startups.com.br/negocios/rodada-de-investimento/sami-levanta-r-60m-em-rodada-para-bater-metas-em-2025/), o plano era concluir 2023 com R$120 milhões de receita vs ~84 milhões realizados.")
st.write("Em [divulgação da nova rodada em Dezembro de 2024](https://startups.com.br/negocios/rodada-de-investimento/sami-levanta-r-60m-em-rodada-para-bater-metas-em-2025/), Guilherme Berado, CEO da Sami, divulgou que planeja encerrar 2024 com R$110 milhões de receita. Ou seja, crescer 30% em um trimestre, feito realizado no mesmo trimestre do ano passado quando cresceu >40% em um tri. Let's watch and see.")

startup_revenue = pd.DataFrame({
    'Operadora' : ['Alice', 'Sami'] * 5,
    'Ano': [2020] * 2 + [2021] * 2 + [2022] * 2 + [2023] * 2 + [2024] * 2,
    'Receita em R$ milhões': [
        # 2020
        1.4, 0.0,
        # 2021
        22.0, 10.6,
        # 2022
        74.3, 71.0,
        # 2023
        219.3, 83.7,
        # 2024
        257.1, 84.8
    ]
})

fig_startup_revenue = px.bar(startup_revenue, x='Ano', y='Receita em R$ milhões', color='Operadora',
                              title='Receita das Startups por Ano',
                              barmode='group',
                              color_discrete_map={'Alice': '#bd037e', 'Sami': '#ff5852'})

st.plotly_chart(fig_startup_revenue)

st.subheader("Ângulo 2: posicionamento de mercado", divider='gray')
st.text("Apesar das similaridades, Alice e Sami tem posicionamento de pricing e target de cliente significativamente diferentes.")

# Bar chart data
st.subheader("Alice e high-end competitors")
st.write("Apesar de oferecer diferentes opções -- com/sem coparticipação, adesão livre/compulsória e possibilidades de cobertura de rede credenciada, a Alice tem posicionamento mais premium que a Sami.")
st.write("Rede credenciada com os hospitais, laboratórios, maternidades mais prestigiados de São Paulo, [plano com reembolso de consultas até 800 reais](https://www.linkedin.com/posts/guilherme-gui-azevedo-14807730_video-sobre-o-alice-ultra-o-melhor-plano-activity-7273027234527858688-F-lI?utm_source=share&utm_medium=member_desktop), planos de entrada mais caros.")
st.write("Apesar da cobertura nacional via [parceria com a Cassi](https://alice.com.br/blog/plano-de-saude/como-funciona-cobertura-nacional-alice/),  autogestão do BB, os próprios fundadores já declararam o foco em São Paulo. Por si só, essa decisão também traz uma estrutura de custos maior vs focar em regiões metropolitanas.")
st.write("Esse posicionamento se manifesta em uma média de prêmio por segurado pelo menos 40% maior que a Sami.")
st.caption("Método de cálculo: Prêmios Ganhos de Plano de Assistência à Saúde dividido pelo número de Beneficiários no período.")

bar_data = pd.DataFrame({
    'Período': ['4Q21', '4Q21', '4Q22', '4Q23', '3Q24', '4Q22', '4Q23', '3Q24'],
    'Operadora': ['Sami', 'Alice', 'Sami', 'Sami', 'Sami', 'Alice', 'Alice', 'Alice'],
    'Prêmio por beneficiário (k)': [round(1393/1000,1), round(2838/1000,1), round(4257/1000, 1), round(3613/1000, 1), round(3832/1000, 1), round(6220/1000, 1), round(8045/1000, 1), round(6053/1000, 1)]
})
# Add labels on top of each bar
bar_data['Label'] = bar_data['Prêmio por beneficiário (k)'].apply(lambda x: f'{x:.1f}')

# Create bar chart
fig_bar = px.bar(bar_data, x='Período', y='Prêmio por beneficiário (k)', color='Operadora',
                 title='Média de prêmio por beneficiário',
                 color_discrete_map={'Sami': '#ff5852', 'Alice': '#bd037e'},
                 barmode='group',
                 text_auto=True
                 )
fig_bar.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig_bar.update_traces(textposition='outside')

st.plotly_chart(fig_bar)


st.text("Então, uma comparação mais coerente deve ser com OMINT, Care Plus, Sul América. Planos com posicionamento premium, cobertura predominante em São Paulo, rede credenciada conceituada.")

bar_data = pd.DataFrame({
    'Período': ['4Q21', '4Q22', '4Q23', '3Q24', '4Q21', '4Q22', '4Q23', '3Q24', '4Q21', '4Q22', '4Q23', '3Q24', '4Q21', '4Q22', '4Q23', '3Q24'],
    'Empresa': ['Alice (421928)', 'Alice (421928)', 'Alice (421928)', 'Alice (421928)', 'OMINT (359661)', 'OMINT (359661)', 'OMINT (359661)', 'OMINT (359661)', 'CARE PLUS (379956)', 'CARE PLUS (379956)', 'CARE PLUS (379956)', 'CARE PLUS (379956)', 'SUL AMERICA (6246)', 'SUL AMERICA (6246)', 'SUL AMERICA (6246)', 'SUL AMERICA (6246)'],
    'Prêmio por beneficiário (k)': [round(2838/1000, 1), round(6220/1000, 1), round(8045/1000, 1), round(6053/1000, 1), round(12927/1000, 1), round(15897/1000, 1), round(14151/1000, 1), round(12927/1000, 1), round(9020/1000, 1), round(10188/1000, 1), round(9030/1000, 1), round(8534/1000, 1), round(5597/1000, 1), round(6444/1000, 1), round(5788/1000, 1), round(4977/1000, 1)]
})
# Add labels on top of each bar
bar_data['Label'] = bar_data['Prêmio por beneficiário (k)'].apply(lambda x: f'R${x}')

# Create bar chart
fig_bar = px.bar(bar_data, x='Período', y='Prêmio por beneficiário (k)', color='Empresa',
                 title='Média de prêmio por beneficiário',
                 color_discrete_map={'Alice (421928)': '#bd037e', 'OMINT (359661)': '#1b3069', 'CARE PLUS (379956)': '#0179cf', 'SUL AMERICA (6246)': '#d15321'},
                 barmode='group',
                 text_auto=True
                 )
fig_bar.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig_bar.update_traces(textposition='outside')

st.plotly_chart(fig_bar)



st.subheader("Ângulo 3: Porte e modalidade", divider='gray')
st.text("Alice e Sami pertencem ao recorte de operadoras de Médio Porte (20 - 100 mil beneficiários) e modalidade Medicina de Grupo (vendem para PF e/ou PJ com rede própria ou terceirizada).")

st.write("TL;DR:")

st.write("- 3Q23 vs 3Q24, pares registraram queda de 1% em receita. 8.6bi vs 8.8bi no ano anterior")

st.write("- Alice e Sami registraram crescimento de 77% e 45%, respectivamente")

st.write("- Interessante notar como em 2022 ambas estavam coladas em receita. Mas, em 2023 e 2024 Alice dispara")



st.divider()

st.title("Capítulo 3: Se correr o bicho pega, se crescer o bicho come?")
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

st.title("Capítulo 4: Built different. ")

st.divider()

st.title("Capítulo 5: Quem quer rir tem que fazer rir…")

st.divider()

st.title("Capítulo Final: Courage is in shorter supply than genius")


bar_data = pd.DataFrame({
    'Ano': [2020, 2020, 2021, 2021, 2024, 2022, 2023, 2024],
    'Operadora': ['Sami', 'Alice', 'Sami', 'Sami', 'Sami', 'Alice', 'Alice', 'Alice'],
    'Receita em R$ milhões': [1.4, 0.0, 22.0, 10.6, 257.1, 74.3, 219.3, 84.8]
})

fig_bar = px.bar(bar_data, x='Ano', y='Receita em R$ milhões', color='Operadora',
                 title='Receita acumulada até último período de cada ano', barmode='group')

for i in range(len(bar_data)):
    fig_bar.add_annotation(x=bar_data['Ano'][i], y=bar_data['Receita em R$ milhões'][i], text=f"{bar_data['Receita em R$ milhões'][i]}", showarrow=False, yshift=10)

st.plotly_chart(fig_bar, config={'responsive': True})
