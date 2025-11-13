# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
# Solicita a operação desejada ao usuário
operacao = input("Digite a operação desejada (+, -, *, /, //, **, %): ")
# verifca a operação válida e se sim cria uma string com o resultado
# se for + resultado = f"A soma entre{num1} e {num2} é igual a: {num1 + num2}"
vefica = ['+', '-', '*', '/', '//', '**', '%']
if operacao not in vefica:
    print("Operação inválida. Por favor, escolha uma das seguintes operações: +, -, *, /, //, **, %")
if operacao == '+':
    resultado = f"A soma entre {num1} e {num2} é igual a: {num1 + num2}"
elif operacao == '-':
    resultado = f"A subtração entre {num1} e {num2} é igual a: {num1 - num2}"
elif operacao == '*':
    resultado = f"A multiplicação entre {num1} e {num2} é igual a: {num1 * num2}"
elif operacao == '/':
    resultado = f"A divisão entre {num1} e {num2} é igual a: {num1 / num2}"
elif operacao == '//':
    resultado = f"A divisão inteira entre {num1} e {num2} é igual a: {num1 // num2}"
elif operacao == '**':
    resultado = f"A exponenciação entre {num1} e {num2} é igual a: {num1 ** num2}"
elif operacao == '%':
    resultado = f"O módulo entre {num1} e {num2} é igual a: {num1 % num2}"
# exibe o resultado
print(resultado) 

# Realizamos as operações básicas: soma, subtração, multiplicação, divisão, divisão inteira, exponenciação e módulo.  
# E exibimos o resultado de cada operação na tela.
# Cada operação é realizada utilizando os operadores aritméticos correspondentes em Python. 
# O resultado de cada operação é armazenado em uma variável e depois exibido utilizando a função print().
# Operações matemáticas básicas em Python
# Autor: ChatGPT
# Data: 2024-06-15
# Versão: 1.0

# Fim do código