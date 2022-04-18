
![transparencia](https://user-images.githubusercontent.com/8771239/163825648-3ec6a156-5309-460c-a616-26cd869040b9.jpg)

# Análise dados CEAPS

CEAPS - Cotas para exercício da atividade parlamentar dos Senadores. A cota parlamentar é o valor que os membros do Poder Legislativo (deputados federais e estaduais, senadores e vereadores) têm direito a receber para cobrir despesas em função da sua atividade como parlamentar (agente público).

Basicamente, o CEAPS contém todos os gastos que senadores brasileiros declararam, divididos por ano.

Nessa análise que realizei, avaliei os dados dos gastos entre 2019 a 2022*.

Obs.: Como realizei a análise em Abr/22 os dados deste ano não estão completos.

## Etapas executadas no projeto

#### - Data Cleaning

Os dados do CEAPS contêm uma série de problemas que podem dificultar a criação de análises mais aprofundadas.

Uma das primeiras coisas que realizei foi identificar tais inconsistências, como campos que possuem valores nulos ou duplicados, converter campos de data que estão sendo carregados como texto, correção de valores monetários, nomes incorretos, formatação de campos de CNPJ, etc.

#### - Data Visualization [WORK IN PROGRESS]

Criar visualizações, a partir da base gerada anteriormente.

#### - Forecasting [WORK IN PROGRESS]

Criação de um modelo que irá prever quanto os senadores vão gastar nos próximos três meses.

## Qual problema quero resolver com essa solução?

- Avaliar os gastos realizados pelos senadores entre 2019 a 2022, a fim de investigar se estes estão dentro dos limites estipulados.

## Qual a solução proposta?

- Prever quanto os senadores irão gastar nos próximos 3 meses (Mai/2022 a Jul/2022).
