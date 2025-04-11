import pandas as pd


def get_beneficiaries():
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
    beneficiaries_melted = pd.melt(
        beneficiaries_data,
        id_vars=["Trimestre"],
        value_vars=["Alice", "Sami"],
        var_name="Operadora",
        value_name="Beneficiários (k)",
    )
    return beneficiaries_melted


def get_revenue():
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
    return df


def get_market_trends():
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
    return chart_data

def get_yearly_totals(chart_data):
    return chart_data.groupby("Ano")["Receita em R$ bilhões"].sum().round(1)

def get_startup_revenue():
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
    return startup_revenue


def get_premium_by_beneficiary():
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
    bar_data["Label"] = bar_data["Prêmio por beneficiário (k)"].apply(
        lambda x: f"{x:.1f}"
    )
    return bar_data


def get_premium_comparison():
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
    bar_data["Label"] = bar_data["Prêmio por beneficiário (k)"].apply(
        lambda x: f"R${x}"
    )
    return bar_data


def get_claims():
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
    return line_data


def get_revenue_comparison():
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
    return bar_data
