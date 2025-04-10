# app/utils/texts.py
import streamlit as st


def intro():
    st.markdown(
        """
        Li o [último relatório econômico-financeiro da ANS](https://www.gov.br/ans/pt-br/assuntos/noticias/numeros-do-setor/ans-divulga-dados-economico-financeiros-relativos-ao-3o-trimestre-de-2024)
        sobre seguradoras de saúde para você não precisar ler. 
        <br><br> Antecipando: se você já é do mercado, não espere nenhuma análise genial sobre o mercado. 
        <br><br> Meu objetivo é trazer luz para dados que vão além de headlines de PR e trazer ao mundo a reflexão que os dados me geraram
        sobre o poder da coragem e [delusional self belief](https://blog.samaltman.com/how-to-be-successful) para mover o mundo para frente.
        """,
        unsafe_allow_html=True,
    )


def chapter_1(section):
    if section == 1:
        st.title("Capítulo 1: It's always day 0.1")
        st.subheader("Alice")
        st.markdown(
            """
            Fundada em 2020, Alice alcançou a marca de 10k membros em 1Q23 ainda no modelo B2C.
            <br><br> Em 2Q23, [**compra carteira da QSaúde**](https://alice.com.br/blog/imprensa/alice-compra-carteira-clientes-qsaude/),
            pivota para B2B e mais que dobra 'na marra' o número de membros: ~10k para ~27k. Um ano e meio depois, a empresa cresceu
            ~50% e finalizou 2024, segundo Gui Azevedo (founder) com [40k membros.](https://www.linkedin.com/posts/guilherme-gui-azevedo-14807730_retrospectiva-2024-spotify-na-alice-activity-7282775874171531264-q6ox?utm_source=share&utm_medium=member_desktop)
            <br><br>Vale destacar que esse dado foi divulgado pela própria empresa. O último dado publicado pela ANS no dia de produção desse artigo é de 3Q24: 34.7k.
            """,
            unsafe_allow_html=True,
        )
        st.subheader("Sami")
        st.markdown(
            """
            Sami inicia operação em 2021 e vive 2 anos de crescimento acelerado. 2021 sai de 0 para ~6k beneficiários. 
            Em 2022 mais que dobra e finaliza o ano com 15k beneficiários. O ritmo desacelerou significativamente em 
            2023 e 2024. Em 2023, a empresa cresceu 30%, terminando o ano com 21k beneficiários. 2024 tem sido ainda 
            mais difícil — encolheu em ~300 segurados se comparado ao início do ano.
            <br><br> Na data de produção deste artigo ainda não foram divulgados dados de 4Q24.
            """,
            unsafe_allow_html=True,
        )

    elif section == 2:
        st.subheader("Still scratching the surface")
        st.markdown("Alice e Sami juntas somam 0.1% da Saúde Suplementar brasileira.")

    elif section == 3:
        st.subheader("Otimismo ou ceticismo?")
        st.markdown(
            """
            Por um lado, o mercado prova-se grande o suficiente para acomodar billion dollar-businesses.
            <br><br> Por outro, são 4 anos de estrada, +230 milhões de dólares captados e nem a superfície parece ter sido atingida.
            A ambição de ambas startups parece ser de gerar mudanças sistêmicas na saúde brasileira. 
            <br><br> Ao colocar a penetração em perspectiva, me questiono o quão longe estamos de mudanças tectônicas. 
            É preciso mais 5/10 anos ou 20/30 anos? Mais \$50 milhões ou \$500 milhões? Alta dependência dos órgãos 
            reguladores para acelerar a evolução do sistema?
            <br><br> A clareza de quão longe estamos de mudanças substanciais em termos de tempo, regulação e investimento é 
            essencial para tirar qualquer conclusão sobre qual será a magnitude do impacto dessas startups.
            <br><br> Elas serão os heróis que iniciam o movimento e morrem antes de vê-lo tomando proporções sem precedentes ou 
            conseguirão 'endure for long enough' para criar e surfar a própria tailwind?
            """,
            unsafe_allow_html=True,
        )


def chapter_2(section):
    if section == 1:
        st.title("Capítulo 2: Go big or go home")
        st.markdown(
            """
            Independente de opinião, fato é que Sami e Alice tem 'mercado infinito' pela frente. Então, quão rápido elas estão
            capturando demanda? <br><br> Spoiler: é muito mais rápido que o mercado e pares. Mesmo assim, é rapido suficiente?
            <br><br> É isso que esse capítulo quer responder.
            """,
            unsafe_allow_html=True,
        )

        st.subheader("Setting the baseline...")
        st.markdown(
            """
            - Zoom out: entre 2020 e 2023 o mercado de saúde suplementar cresceu 30%. <br><br>
            - Zoom in: 2023 foi o melhor ano desde pandemia — 17% de crescimento. Se mantivermos a sazonalidade do 
            último ano nesse 4Q, números indicam crescimento superior a 10%, segunda melhor porformance desde 2020. <br><br>
            - Titãs: desde 2020, um terço do mercado está nas mãos das top 5 seguradoras. A Hapvida é a operadora que mais
            cresceu nesse intervalo: +95%. Destaque de 2024 é a Amil que nos três primeiros trimestres já atingiu ~93% da
            receita de 2023 vs ~80% das outras quatro. Se seguir nesse velocidade, a Amil deve crescer +20% nesse ano.
            """,
            unsafe_allow_html=True,
        )
        st.caption(
            "*Apesar da fusão entre Notre Dame e Hapvida, relatório ANS ainda reporta como operadoras distintas.*"
        )

    elif section == 2:
        st.subheader("Maçã com maçã")
        st.markdown(
            """
            Apesar do baseline transmitir o 'general growth rate' da indústria, Alice e Sami são uma 'espécie rara' de operadora. 
            Tech-native, VC-backed, jovens. Então, os ângulos de comparação devem ser outros.
            """
        )

        st.subheader("Ângulo 1: startup vs startup", divider="gray")
        st.subheader("Alice: software growth rate")

        st.markdown(
            """
            Mesmo em um setor cauteloso com mudanças e com uma camada intensa de serviços in-house 
            [(segundo Gui Azevedo, ~1/3 do time são de profissionais de saúde)](https://drive.google.com/file/d/1pZLquHpzZulnnejWN4uV7n8T35A_ISHy/view?usp=sharing), 
            Alice atingiu a ['taxa mágica de crescimento'](https://www.battery.com/blog/helping-entrepreneurs-triple-triple-double-double-double-to-a-billion-dollar-company/) 
            de empresas pure software nos últimos 3 anos. A empresa vem de +1400%, +230%, +195% desde 2021 respectivamente.
            
            [Em um podcast publicado em Junho de 2024](https://drive.google.com/file/d/1pZLquHpzZulnnejWN4uV7n8T35A_ISHy/view?usp=sharing), 
            Gui Azevedo projetava 500 milhões de receita para esse ano. Segundo dado 
            [publicado no LinkedIn](https://www.linkedin.com/posts/guilherme-gui-azevedo-14807730_retrospectiva-2024-spotify-na-alice-activity-7282775874171531264-q6ox?utm_source=share&utm_medium=member_desktop), 
            a empresa atingiu R\$450 milhões de receita anualizada, +50% de crescimento YoY.
            
            Reforçando que esse é um dado publicado pela empresa e não pela ANS. O último report da ANS na produção desse artigoda foi de 3Q24: R\$257 milhões.
            """
        )

        st.subheader("Sami: altos e baixos")

        st.markdown(
            """
            Ritmo acelerado: de zero a +10 milhões de receita em um ano desde sua fundação. Em 2022, a empresa cresce 570% e 
            chega a +70 milhões de receita anual em apenas 2 anos de existência.
            
            Rough year: em 2023, a Sami cresceu apenas ~18%. Isso é menos que as bilionárias Sul América (19%) e Notre Dame (20%) 
            e em linha com as outras titãs da indústria - Hapvida, Amil e Bradesco que cresceram cerca de 14 - 15%. Segundo 
            [matéria do Startups](https://startups.com.br/negocios/rodada-de-investimento/sami-levanta-r-60m-em-rodada-para-bater-metas-em-2025/), 
            o plano era concluir 2023 com R\$120 milhões de receita vs ~84 milhões realizados.
            
            Em [divulgação da nova rodada em Dezembro de 2024](https://startups.com.br/negocios/rodada-de-investimento/sami-levanta-r-60m-em-rodada-para-bater-metas-em-2025/), 
            Guilherme Berado, CEO da Sami, divulgou que planeja encerrar 2024 com R\$110 milhões de receita. Ou seja, crescer 30% em um 
            trimestre, feito realizado no mesmo trimestre do ano passado quando cresceu >40% em um tri. Let's watch and see.
            """
        )

    elif section == 3:
        st.subheader("Ângulo 2: posicionamento de mercado", divider="gray")
        st.markdown(
            """
            Apesar das similaridades, Alice e Sami tem posicionamento de pricing e target de cliente significativamente diferentes.
            """
        )

        # Bar chart data
        st.subheader("Alice e high-end competitors")
        st.markdown(
            """
            Apesar de oferecer diferentes opções -- com/sem coparticipação, adesão livre/compulsória e possibilidades de 
            cobertura de rede credenciada, a Alice tem posicionamento mais premium que a Sami.
            
            Rede credenciada com os hospitais, laboratórios, maternidades mais prestigiados de São Paulo, 
            [plano com reembolso de consultas até 800 reais](https://www.linkedin.com/posts/guilherme-gui-azevedo-14807730_video-sobre-o-alice-ultra-o-melhor-plano-activity-7273027234527858688-F-lI?utm_source=share&utm_medium=member_desktop), 
            planos de entrada mais caros.
            
            Apesar da cobertura nacional via [parceria com a Cassi](https://alice.com.br/blog/plano-de-saude/como-funciona-cobertura-nacional-alice/), 
            autogestão do BB, os próprios fundadores já declararam o foco em São Paulo. Por si só, essa decisão também traz uma 
            estrutura de custos maior vs focar em regiões metropolitanas.
            
            Esse posicionamento se manifesta em uma média de prêmio por segurado pelo menos 40% maior que a Sami.
            """
        )
        st.caption(
            "Método de cálculo: Prêmios Ganhos de Plano de Assistência à Saúde dividido pelo número de Beneficiários no período."
        )

    elif section == 4:

        st.markdown(
            """
            Então, uma comparação mais coerente deve ser com OMINT, Care Plus, Sul América. Planos com posicionamento premium, 
            cobertura predominante em São Paulo, rede credenciada conceituada.
            """
        )

    elif section == 5:
        st.subheader("Ângulo 3: Porte e modalidade", divider="gray")
        st.markdown(
            """
            Alice e Sami pertencem ao recorte de operadoras de Médio Porte (20 - 100 mil beneficiários) e modalidade 
            Medicina de Grupo (vendem para PF e/ou PJ com rede própria ou terceirizada).
            
            TL;DR:
            
            - 3Q23 vs 3Q24, pares registraram queda de 1% em receita. 8.6bi vs 8.8bi no ano anterior
            
            - Alice e Sami registraram crescimento de 77% e 45%, respectivamente
            
            - Interessante notar como em 2022 ambas estavam coladas em receita. Mas, em 2023 e 2024 Alice dispara
            """
        )


def chapter_3():
    st.title("Capítulo 3: Se correr o bicho pega, se crescer o bicho come?")
    st.markdown("Vetor 1: Sinistralidade")


def chapter_4():
    st.title("Capítulo 4: Built different.")


def chapter_5():
    st.title("Capítulo 5: Quem quer rir tem que fazer rir…")


def final_chapter():
    st.title("Capítulo Final: Courage is in shorter supply than genius")
