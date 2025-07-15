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
    pedidos_clientes = clientes.merge(pedidos, left_on="cliente_id", right_on="cliente_id")

    pedidos_clientes["valor_total"] = pedidos_clientes["quantidade"]*pedidos_clientes["preco_unitario"]

    valor_por_cliente = pedidos_clientes.groupby(["cliente_id", "nome", "email"])["valor_total"].sum().reset_index()

    def classificar_cliente(valor: int) -> str:
        if valor <= 500:
            return "fraco"
        if valor <= 2000:
            return "médio"
        if valor > 2000:
            return "ótimo"

    valor_por_cliente["classificacao"] = valor_por_cliente["valor_total"].apply(classificar_cliente)

    return valor_por_cliente




""" clientes_path = "raw_data\\clientes.csv"
pedidos_path = "raw_data\\pedidos.csv"

clientes, pedidos = load_csv(clientes_path, pedidos_path)
df_final = process_df(clientes, pedidos)
print(df_final) """