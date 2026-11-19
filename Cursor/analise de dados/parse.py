"""Lê um CSV, calcula estatísticas por coluna e traça col1 vs col2."""

from pathlib import Path # Biblioteca para manipulação de caminhos de arquivos

import matplotlib.pyplot as plt # Biblioteca para criação de gráficos
import pandas as pd # Biblioteca para manipulação de dados

CSV_PATH = Path(__file__).with_name("dados.csv") # Caminho do arquivo CSV


def main() -> None:
    df = pd.read_csv(CSV_PATH) # Lê o arquivo CSV
    numericas = df.select_dtypes(include="number") # Seleciona as colunas numéricas

    if numericas.empty:
        raise SystemExit(f"Nenhuma coluna numérica em {CSV_PATH.name}") # Exibe uma mensagem de erro se não houver colunas numéricas

    estatisticas = pd.DataFrame( # Cria um DataFrame com as estatísticas
        {
            "media": numericas.mean(), # Média
            "mediana": numericas.median(), # Mediana
            "desvio_padrao": numericas.std(), # Desvio padrão
        }
    )

    print(f"Arquivo: {CSV_PATH.name} ({len(df)} linhas)", flush=True) # Exibe o nome do arquivo e o número de linhas
    print(estatisticas.round(2).to_string(), flush=True)

    if "col1" not in numericas.columns or "col2" not in numericas.columns: # Exibe uma mensagem de erro se não houver as colunas col1 e col2
        raise SystemExit("O CSV precisa das colunas col1 e col2 para o gráfico.")

    fig, ax = plt.subplots(figsize=(8, 5)) # Cria um gráfico com o tamanho 8x5
    ax.scatter(numericas["col1"], numericas["col2"], color="#2563eb", alpha=0.85) # Cria um gráfico de dispersão com a cor #2563eb e o alpha 0.85
    ax.set_xlabel("col1") # Define o label do eixo x como "col1"
    ax.set_ylabel("col2") # Define o label do eixo y como "col2"
    ax.set_title("Dispersão de col1 vs col2") # Define o título do gráfico como "Dispersão de col1 vs col2"
    ax.grid(True, linestyle="--", alpha=0.4)
    fig.tight_layout() # Ajusta o layout do gráfico

    saida = Path(__file__).with_name("dispersao_col1_col2.png") # Define o caminho do arquivo de saída como "dispersao_col1_col2.png"
    fig.savefig(saida, dpi=120) # Salva o gráfico com a resolução 120dpi    
    print(f"\nGráfico salvo em {saida.name}") # Exibe o nome do arquivo de saída
    plt.show() # Exibe o gráfico


if __name__ == "__main__":
    main() # Chama a função main
