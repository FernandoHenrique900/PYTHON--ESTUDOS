# Calculadora simples com numeros reais.
# Repete ate o usuario digitar "sair".


def formatar_numero(valor):
    """Inteiro: sem virgula. Quebrado: ate 2 casas apos a virgula."""
    arredondado = round(float(valor), 2)
    if arredondado.is_integer():
        return str(int(arredondado))
    texto = f"{arredondado:.2f}".rstrip("0").rstrip(".")
    return texto.replace(".", ",")


def ler_numero(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Numero invalido")


def calcular(operacao, num1, num2):
    if operacao == "soma":
        return num1 + num2
    if operacao == "subtracao":
        return num1 - num2
    if operacao == "multiplicacao":
        return num1 * num2
    if operacao == "divisao":
        if num2 == 0:
            return None
        return num1 / num2
    return None


while True:
    operacao = input(
        "Qual operacao voce deseja realizar? (soma, subtracao, multiplicacao, divisao): "
    ).strip().lower()

    if operacao == "sair":
        break

    if operacao not in ("soma", "subtracao", "multiplicacao", "divisao"):
        print("Operacao invalida")
        continue

    num1 = ler_numero("Digite o primeiro numero: ")
    num2 = ler_numero("Digite o segundo numero: ")

    resultado = calcular(operacao, num1, num2)
    if resultado is None:
        print("Aviso: divisao por zero nao existe.")
        continue
    print(
        f"O resultado da operacao {operacao} entre {formatar_numero(num1)} "
        f"e {formatar_numero(num2)} e {formatar_numero(resultado)}"
    )

print("Obrigado por usar a calculadora!")
