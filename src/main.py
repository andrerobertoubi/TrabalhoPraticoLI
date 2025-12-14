##
# @file main.py
# @brief Programa interativo para operações sobre um vetor de números inteiros.

import math
import webbrowser
import argparse
from pathlib import Path

## @brief Número mínimo permitido
NUMERO_MIN = 1

## @brief Número máximo permitido
NUMERO_MAX = 26

## @brief Número de elementos do vetor
TAMANHO_VETOR = 18

## @brief Identifica o máximo de todos os elementos do vetor
#  @param numeros Lista de números inteiros.
def maximo(numeros: list[int]) -> int:
    return max(numeros)

## @brief Constrói uma matriz 4 por 18, em que cada linha é composta pelo vetor lido
#  @param numeros Lista de números inteiros.
def matriz_4x18(numeros: list[int]) -> str:
    matriz = []
    for _ in range(4):
        line = ' '.join(f'{num:2d}' for num in numeros)  # Formatar cada número com 2 dígitos, alinhados à direita
        matriz.append(line)
    return '\n'.join(matriz)

## @brief Calcula a tangente da primeira metade dos elementos no vetor (em radianos)
#  @param numeros Lista de números inteiros.
def tan_primeira_metade(numeros: list[int]) -> list[float]:
    metade = len(numeros) // 2
    return [math.tan(numeros[i]) for i in range(metade)]

## @brief Devolve a soma dos valores do vetor que são divisíveis por três
#  @param numeros Lista de números inteiros.
def somar_divisiveis_por_tres(numeros: list[int]) -> int:
    return sum(num for num in numeros if num % 3 == 0)

## @brief Calcula a subtração da primeira metade dos elementos no vetor com os da segunda metade
#  @param numeros Lista de números inteiros.
def subtrair_metades(numeros: list[int]) -> list[int]:
    metade = len(numeros) // 2
    primeira_metade = numeros[:metade]
    segunda_metade = numeros[metade:]
    return [primeira_metade[i] - segunda_metade[i] for i in range(metade)]

## @brief Devolve o vetor ordenado por ordem decrescente
#  @param numeros Lista de números inteiros.
def ordenar_decrescente(numeros: list[int]) -> list[int]:
    return sorted(numeros, reverse=True)

## @brief Mostra o menu de opções
def mostrar_menu():
    print('\nMenu de opções:')
    print('-' * 100)
    print('1 - Identificar o máximo de todos os elementos do vetor')
    print('2 - Construir uma matriz 4 por 18, em que cada linha é composta pelo vetor lido')
    print('3 - Calcular a tangente da primeira metade dos elementos no vetor (em radianos)')
    print('4 - Devolver a soma dos valores do vetor que são divisíveis por três')
    print('5 - Calcular a subtração da primeira metade dos elementos no vetor com os da segunda metade')
    print('6 - Devolver o vetor ordenado por ordem decrescente')
    print('7 - Mostrar página de ajuda')
    print('0 - Sair')
    print('-' * 100)

## @brief Pede ao utilizador para inserir números inteiros válidos e devolve o vetor
#  @details Esta função pede ao utilizador para inserir números inteiros entre NUMERO_MIN e NUMERO_MAX até que o vetor atinja o tamanho TAMANHO_VETOR. Números inválidos são rejeitados com uma mensagem de erro.
#  @return Lista de números inteiros válidos.
def ler_vetor() -> list[int]:
    numeros = []
    while len(numeros) < TAMANHO_VETOR:
        entrada = input(f'\n({len(numeros) + 1}/{TAMANHO_VETOR}) Digite um número inteiro entre {NUMERO_MIN} e {NUMERO_MAX}: ')
        try:
            numero = int(entrada)
            if NUMERO_MIN <= numero <= NUMERO_MAX:
                numeros.append(numero)
                print(f'\nNúmero {numero} adicionado com sucesso.')
            else:
                print(f'\n[ERRO]: O número inserido deve estar entre {NUMERO_MIN} e {NUMERO_MAX}.')
        except ValueError:
            print('\n[ERRO]: Por favor, digite um número inteiro válido.')
    return numeros

## @brief Função principal do programa
#  @details Esta função pede ao utilizador números inteiros e guarda-os num vetor, para posteriormente providenciar forma de fazer operações sobre esses valores.
def main():
    if TAMANHO_VETOR % 2 != 0:
        print('\n[AVISO]: O tamanho do vetor é um número ímpar. Algumas funcionalidades podem não funcionar corretamente.')
    numeros = ler_vetor()
    while True:
        mostrar_menu()
        print('\nLista de números inseridos:', numeros)
        opcao = input('Escolha uma opção: ')
        resultado = None
        match opcao:
            case '1':
                resultado = maximo(numeros)
            case '2':
                resultado = matriz_4x18(numeros)
            case '3':
                resultado = tan_primeira_metade(numeros)
            case '4':
                resultado = somar_divisiveis_por_tres(numeros)
            case '5':
                resultado = subtrair_metades(numeros)
            case '6':
                resultado = ordenar_decrescente(numeros)
            case '7':
                doc = Path(__file__).parent.parent / 'docs' / 'html' / 'index.html'
                webbrowser.open(doc.as_uri())
            case '0':
                return
            case _:
                print('ERRO: Opção inválida. Por favor, escolha uma opção válida.')
        if resultado is not None:
            print('Resultado:')
            print(resultado)

if __name__ == '__main__':
    argparse.ArgumentParser(
        description=f'Programa interativo para operações sobre um vetor de {TAMANHO_VETOR} números entre {NUMERO_MIN} e {NUMERO_MAX}.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__  # usa o docstring longo como ajuda adicional
    ).parse_args()
    main()