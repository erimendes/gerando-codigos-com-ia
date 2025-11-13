# vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado
def repetir_string():
    string = input("Digite uma string: ")
    try:
        numero = int(input("Digite quantas vezes o texto deve ser repetido: "))
        resultado = string * numero
        print("Resultado:", resultado)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")  

repetir_string()

# Exemplo de entrada e saída:
# Entrada:
# Digite uma string: Olá
# Digite um número inteiro: 3
# Saída:
# Resultado: OláOláOlá 
# Entrada:
# Digite uma string: Teste
# Digite um número inteiro: dois
# Saída:
# Por favor, insira um número inteiro válido. 
# Exemplo de entrada e saída: 
# Entrada:
# Digite uma string: Python
# Digite um número inteiro: 2
# Saída:
# Resultado: PythonPython 
# Entrada:
# Digite uma string: AI
# Digite um número inteiro: -1
# Saída:
# Resultado:  
# Entrada:
# Digite uma string: Código
# Digite um número inteiro: 0
# Saída:
# Resultado:  
