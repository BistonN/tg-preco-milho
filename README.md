## Introdução:
Os brasileiros nos últimos anos está cada vez mais se preocupando com o seu dinheiro e onde o investir. Isso é refletido na bolsa de valores brasileira que divulgou dados dos números de investidores em março de 2020 que chegam á 2,3 ​​milhões sendo que no mesmo mês em 2019 eram apenas 0,9 milhão de investidores. Um dos mercados que cresceu juntamente foi o mercado de futuros, onde é negociado ativos como futuro de moedas, commodities agropecuários, etc. Entre os commodities agrícolas, está o milho, que é uma cultura significativa para o Brasil, em nível de produção e rendimentos. Este ativo é negociado principalmente por investidores que atuam no mercado e produtores da cultura, que baseado em suas estratégias, negociam o contrato futuro do milho para proteger sua produção ou até mesmo alavancar seus ganhos na safra. Portanto este projeto visa estudar a performance de algoritmos de aprendizado de máquinas na previsão do preço do contrato de milho, a fim de auxiliar os negociantes do ativo em suas respectivas estratégias.

## Objetivo:
O presente projeto tem como objetivo coletar dados referente ao mercado futuro de milho da web, salvar em um banco de dados e realizar testes com algoritmos de regressão linear para auxiliar no desenvolvimento do Trabalho de conclusão de Curso dos alunos Renan Moraes Carvalho e João Vitor Biston Nunes.

## Arquitetura:
MongoDB: Banco de Dados
Python: Criação da lógica para importação dos dados no banco e pré processamento dos dados
Orange: Realização dos testes de performance da previsão do preço

## Desenvolvimento:
O desenvolvimento do projeto pode ser dividido em 4 partes:

- Coleta dos dados
- Pré processamento dos dados
- Mineração
- Visualização / Análise

Coleta dos dados: Hoje os dados sobre o mercado financeiro no mundo é de fácil acesso na internet, então para a coleta de dados dos indicadores financeiros como histórico do preço do dólar, do preço do contrato de milho no brasil e na bolsa de chicago. foi utilizado o site investing.com, que fornece de forma gratuita os respectivos dados. Já para os indicadores agrícolas, como previsão da produtividade, produção e área plantada no mês, foi utilizado os boletins mensais de grãos no Brasil publicado pela CONAB (Companhia Nacional de Abastecimento). Todos os indicadores foram salvos em arquivos CSV.

Pré processamento dos dados: A limpeza dos dados foi feito em python onde foi retirado dos arquivos CSV os dados irrelevantes para nós, e acrescentar dados faltantes como por exemplo o preço do milho em dias não úteis, onde foi considerado o preço do último dia útil.

Mineração: Para a parte de mineração foi utilizado o método estatístico para previsão de valores, regressão linear, onde foi utilizado o sistema Orange para realizar os testes.

Visualização / Análise: A visualização dos dados foi um arquivo CSV que foi carregado em uma planilha para a análise. O Orange já disponibiliza indicadores de performance, como R2, MSE, RMSE, Média do erro absoluto, etc. Então não foi preciso fazer esses cálculos manualmente na planilha.