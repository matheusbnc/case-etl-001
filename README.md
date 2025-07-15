# Case ETL

Projeto de portfólio: pipeline ETL simples em Python para análise de clientes e pedidos.

## Estrutura

- `raw_data/`: arquivos de entrada (`clientes.csv`, `pedidos.csv`)
- `processed_data/`: saída do processamento
- `src/etl.py`: script principal do ETL

## Como executar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
   ou, se preferir, use Poetry:
   ```sh
   poetry install
   ```

2. Execute o ETL:
   ```sh
   python src/etl.py
   ```

O relatório será salvo em `processed_data/relatorio_clientes.csv`.

## Sobre

Este projeto lê dados de clientes e pedidos, calcula o valor total por cliente e classifica cada um conforme o valor movimentado.
