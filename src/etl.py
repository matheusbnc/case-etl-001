import os
import pandas as pd

def load_csv(clientes_path: str, pedidos_path: str) -> pd.DataFrame:
    """
    Lê dois arquivos e retorna-os como um DataFrame do Pandas.

    Valida se o arquivo existe.

    Args:
        clientes_path (str): Caminho para o arquivo CSV de clientes.
        pedidos_path (str): Caminho para o arquivo CSV de pedidos.

    Returns:
        pd.DataFrame: DataFrame contendo os dados do CSV.

    Raises:
        FileNotFoundError: Se o arquivo não existir.
    """
    if not os.path.exists(clientes_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {clientes_path}")
    if not os.path.exists(pedidos_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {clientes_path}")

    clientes = pd.read_csv(clientes_path)
    pedidos = pd.read_csv(pedidos_path)
    return clientes, pedidos


def process_df(clientes: pd.DataFrame, pedidos: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe dois DataFrames e realiza operações de tratamento e transformação.

    Args:
        clientes (pd.DataFrame): DataFrame de clientes a ser processado.
        pedidos (pd.DataFrame): DataFrame de pedidos a ser processado.
    Returns:
        pd.DataFrame: Dataframe processado
    """
    
