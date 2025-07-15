import os
import pandas as pd
from typing import Tuple

def extract_csv(clientes_path: str, pedidos_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Lê dois arquivos CSV e retorna-os como DataFrames do Pandas.

    Args:
        clientes_path (str): Caminho para o arquivo CSV de clientes.
        pedidos_path (str): Caminho para o arquivo CSV de pedidos.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: DataFrames de clientes e pedidos.

    Raises:
        FileNotFoundError: Se algum arquivo não existir.
    """
    if not os.path.exists(clientes_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {clientes_path}")
    if not os.path.exists(pedidos_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {pedidos_path}")

    clientes = pd.read_csv(clientes_path)
    pedidos = pd.read_csv(pedidos_path)
    return clientes, pedidos

def process_df(clientes: pd.DataFrame, pedidos: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe dois DataFrames e realiza operações de tratamento e transformação.

    Args:
        clientes (pd.DataFrame): DataFrame de clientes.
        pedidos (pd.DataFrame): DataFrame de pedidos.

    Returns:
        pd.DataFrame: DataFrame processado com valor total e classificação.
    """
    pedidos_clientes = clientes.merge(pedidos, on="cliente_id")
    pedidos_clientes["valor_total"] = pedidos_clientes["quantidade"] * pedidos_clientes["preco_unitario"]
    valor_por_cliente = pedidos_clientes.groupby(["cliente_id", "nome", "email"])["valor_total"].sum().reset_index()

    def classificar_cliente(valor: float) -> str:
        if valor <= 500:
            return "fraco"
        elif valor <= 2000:
            return "médio"
        else:
            return "ótimo"

    valor_por_cliente["classificacao"] = valor_por_cliente["valor_total"].apply(classificar_cliente)
    return valor_por_cliente

def load_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Salva um DataFrame como CSV no caminho especificado.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        output_path (str): Caminho de saída.
    """
    df.to_csv(output_path, index=False)
    print(f"Relatório salvo em: {output_path}")

def main(
    clientes_path: str = os.path.join("raw_data", "clientes.csv"),
    pedidos_path: str = os.path.join("raw_data", "pedidos.csv"),
    output_path: str = os.path.join("processed_data", "relatorio_clientes.csv")
):
    clientes, pedidos = extract_csv(clientes_path, pedidos_path)
    df_final = process_df(clientes, pedidos)
    load_csv(df_final, output_path)

if __name__ == "__main__":
    main()
