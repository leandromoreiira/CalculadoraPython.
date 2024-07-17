#Definição das funções principais da calculadora
def adicao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1+num2
    print(f"O resultado é {resultado}")
            
def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1-num2
    print(f"O resultado é {resultado}")

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1*num2
    print(f"O resultado é {resultado}")

def divisao():
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1/num2
            if num2 !=0:
                print(f"O resultado é {resultado}")
            else:
                print(f"Erro: Divisão por zero não é permitida")
                
#Declaração da função Calculadora, função essa que chama outras funções
def calculadora():
    #inicio do looping
     while True:
                print("Digite a opção desejada: ")
                print("1 - Adição ")
                print("2 - Subatação ")
                print("3 - Multiplicação ")
                print("4 - Divisão ")
                print("5 - Sair ")

                #recebe a resposta do usuario
                resposta = input("Digite sua escolha de 01 a 05 ")


                #chamada das funções remententes a resposta do usuario
                if resposta == "1":
                    adicao()
                elif resposta == "2":
                    subtracao()
                elif resposta == "3":
                    multiplicacao()
                elif resposta == "4":
                    divisao()
                elif resposta == "5":
                    print("Saindo...")
                    break
                else:
                    print(" Opção Invalida , vamos tentar novamente...")
                    
#chamada da função da calculadora
calculadora()