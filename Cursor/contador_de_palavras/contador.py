# Programa para contar palavras em um arquivo de texto

# 1. Peça ao usuário o caminho para um arquivo de texto.
# 2. Leia o conteúdo do arquivo.
# 3. Separe em palavras.
# 4. Conte o número total de palavras.
# 5. Exibe as 10 palavras mais frequentes e sua contagem.


#importações
import os
from collections import Counter

#função para contar palavras
def contar_palavras(arquivo):
    with open(arquivo, "r", encoding="utf-8") as file:
        conteudo = file.read()
    return conteudo.split()

#função para exibir as 10 palavras mais frequentes
def exibir_palavras_frequentes(palavras):
    return Counter(palavras).most_common(10)

#função principal
def main():
    caminho_arquivo = input("Digite o caminho para o arquivo de texto: ")
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado.")
        return
    palavras = contar_palavras(caminho_arquivo)
    print(f"O arquivo contém {len(palavras)} palavras.")
    palavras_frequentes = exibir_palavras_frequentes(palavras)
    print("As 10 palavras mais frequentes são:")
    for palavra, contagem in palavras_frequentes:
        print(f"{palavra}: {contagem}")

#teste
if __name__ == "__main__":
    main()
