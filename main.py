"""
O objetivo deste trabalho  é  implementar  um programa que peça ao utilizador 12
números inteiros e os guarde num vetor, para  posteriormente  providenciar forma
de calcular algumas estatísticas ou fazer operações sobre esses valores.
Os valores pedidos devem estar compreendidos entre 4 e 13.
Deve ser feita a VALIDAÇÃO DE ENTRADA!

Após terem sido pedidos os valores, deve  ser mostrado um menu ao utilizador que
lhe permita calcular cada  uma  das  estatísticas referidas em baixo, exatamente
pela  ordem  colocadas  neste  enunciado.  Depois de  se  escolher  uma opção, o
resultado deve ser mostrado no ecrã, e o menu deve voltar a ser exibido.
As funcionalidades mínimas a disponibilizar são as seguintes:

  1 - Cálculo da divisão de todos os elementos no vetor por 2;
  2 - Devolução dos valores em posições múltiplas de três do vetor;
  3 - Devolução do vetor ordenado por ordem decrescente;
  4 - Construção de uma matriz 2 por 12, em que cada linha é composta pelo vetor
      lido (primeira linha) e por números aleatórios (segunda linha);
  5 - Retorno de um elemento aleatório desse vetor (que deve mudar sempre que se
      executa o programa);
  6 - Cálculo da raíz quadrada de todos os elementos no vetor.


Uma  versão  mais elaborada  do projeto  deve exibir adicionalmente as seguintes
características e funcionalidades:

  1 - Leitura de um novo vetor com três valores,  cálculo e devolução do produto
      externo desse vetor com as últimas três casas do vetor inicial;
  2 - Cálculo do mínimo múltiplo comum de cada dois números seguidos do vetor;
  3 - Leitura  de  um novo vetor  1x12,  cálculo  e  devolução  da  matriz 12x12
      resultante do produto do vetor inicial com o novo vetor gerado;
  4 - Cálculo e apresentação da matriz transposta referida no ponto anterior;
  5 - O programa apresenta  adicionalmente  uma  página de ajuda, acessível como
      sendo a entrada 7 no menu.
  6 - O programa  mostra  alguma  ajuda  quando é executado a partir da linha de
      comandos com a flag --help.
"""

import random
import math

NUMERO_MINIMO = 4
NUMERO_MAXIMO = 13

if __name__ == "__main__":
    numeros_inteiros = []

    while True:
        entrada = input(f"Digite um número inteiro entre {NUMERO_MINIMO} e {NUMERO_MAXIMO} (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = int(entrada)
            if numero >= NUMERO_MINIMO and numero <= NUMERO_MAXIMO:
                numeros_inteiros.append(numero)
                print('Números inteiros válidos inseridos:', numeros_inteiros)
            else:
                print(f'Por favor, digite um número entre {NUMERO_MINIMO} e {NUMERO_MAXIMO}.')
        except ValueError:
            print('Por favor, digite um número inteiro válido.')

    while True:
        print("\nMenu de opções:")
        print("1 - Dividir todos os elementos por 2")
        print("2 - Mostrar valores em posições múltiplas de três")
        print("3 - Mostrar vetor ordenado em ordem decrescente")
        print("4 - Construir matriz 2x12 com números aleatórios")
        print("5 - Retornar um elemento aleatório do vetor")
        print("6 - Calcular a raiz quadrada de todos os elementos")
        print("7 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            resultado = [x / 2 for x in numeros_inteiros]
            print("Resultado da divisão por 2:", resultado)
        elif opcao == '2':
            resultado = [numeros_inteiros[i] for i in range(len(numeros_inteiros)) if i % 3 == 0 and i != 0]
            print("Valores em posições múltiplas de três:", resultado)
        elif opcao == '3':
            resultado = sorted(numeros_inteiros, reverse=True)
            print("Vetor ordenado em ordem decrescente:", resultado)
        elif opcao == '4':
            matriz = [numeros_inteiros, [random.randint(NUMERO_MINIMO, NUMERO_MAXIMO) for _ in range(12)]]
            print("Matriz 2x12:")
            for linha in matriz:
                print(linha)
        elif opcao == '5':
            elemento_aleatorio = random.choice(numeros_inteiros)
            print("Elemento aleatório do vetor:", elemento_aleatorio)
        elif opcao == '6':
            resultado = [math.sqrt(x) for x in numeros_inteiros]
            print("Raiz quadrada de todos os elementos:", resultado)
        elif opcao == '7':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")