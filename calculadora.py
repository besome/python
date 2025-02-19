import math as mt

def soma(a,b):
    return a + b
    
def subtracao(a,b):
    return a - b
    
def multiplicacao(a,b):
    return a * b
    
def divisao (a,b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a/b
    
def raiz(a,b):
    if a < 0:
        return "Erro: não é possível calcular a raiz quadrada de um número negativo!"
    return mt.sqrt(a)
    
def Potencia(a,b):
    return mt.pow(a,b)
    

def erro(x, y):
    return "Opção inválida!"
    
if __name__ == '__main__':
    print("##################################\n")
    print("Calculadora Python\n")
    print("Qual operação você deseja realizar?\n")
    opt = input(" 1 - Subtração\n 2 - Soma\n 3 - Divisão\n 4 - Multiplicação\n 5 - Raiz Quadrada\n 6 - Potência\n")
    try:
        a = float(input("Digite o primeiro número: "))
        if opt == 5:
            b = 0
        else:
            b = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Insira um número inteiro ou decimal.")
        exit()
    
    operacoes = {
        "1": subtracao,
        "2": soma,
        "3": divisao,
        "4": multiplicacao,
        "5": raiz,
        "6": Potencia
    }
    
    resultado = operacoes.get(opt, erro)(a, b)

    print(f"Resultado: {resultado}")
    print("##################################\n")
