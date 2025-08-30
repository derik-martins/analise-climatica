# Análise de Dados Climáticos de Porto Alegre (1961-2016)

Este projeto apresenta uma análise de dados focada na série histórica do clima de Porto Alegre, cobrindo um período de 55 anos, de 1961 a 2016. O script desenvolvido em Python processa, trata e visualiza mais de 20.000 registros climáticos a partir de um único arquivo CSV.

## Objetivo

O desafio central foi desenvolver um pipeline de dados funcional: desde a extração e tratamento de um grande volume de registros até a geração de visualizações e insights claros com a biblioteca Matplotlib.

## Funcionalidades

- **Processamento de Dados**: Leitura e manipulação de mais de 20.000 registros de um arquivo CSV
- **Tratamento e Limpeza**: Mapeamento de colunas de interesse (precipitação, temperaturas máxima e mínima) e aplicação do tratamento necessário para a análise
- **Visualização de Dados**: Geração de gráficos e visualizações personalizadas com Matplotlib
- **Análise Flexível**: Permite análises por períodos específicos e a identificação de padrões, como o mês mais chuvoso da série histórica

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento do script
- **Matplotlib**: Biblioteca para a criação dos gráficos e visualizações

## Estrutura do Projeto

```
├── analise_clima.py    # Script principal de análise
├── analisar.csv        # Dataset com dados climáticos
└── README.md           # Documentação do projeto
```

## Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/derik-martins/analise-climatica.git
cd analise-climatica
```

### 2. Instale as dependências

```bash
pip install matplotlib
```

### 3. Execute o script de análise

```bash
python analise_clima.py
```

## Exemplo de Resultado

O script gera visualizações que ajudam a entender o comportamento do clima em Porto Alegre. Um dos resultados possíveis é um gráfico de barras que mostra a precipitação média mensal, destacando visualmente o mês mais chuvoso ao longo da série histórica.

## Dataset

O projeto utiliza dados climáticos históricos de Porto Alegre coletados entre 1961 e 2016, contendo:

- **Precipitação**: Dados de chuva em milímetros
- **Temperatura Máxima**: Registros diários de temperatura máxima
- **Temperatura Mínima**: Registros diários de temperatura mínima
- **Período**: 55 anos de dados históricos (20.000+ registros)
