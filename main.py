"""
Sistema de Gerenciamento de Notas

Este módulo implementa um sistema simples para gerenciar notas acadêmicas,
permitindo adicionar notas, visualizar todas as notas cadastradas e calcular a média.

Autor: xthgo19
Data: Maio 2025
"""

# Lista vazia para guardar as notas
notas = []

def adicionar_nota(nota):
    """
    Adiciona uma nova nota à lista de notas.
    
    Args:
        nota (float): A nota a ser adicionada ao sistema.
    
    Returns:
        None
    """
    notas.append(nota)

def exibir_notas():
    """
    Exibe todas as notas que foram cadastradas no sistema.
    
    Esta função imprime na tela a lista completa de notas armazenadas.
    
    Returns:
        None
    """
    print("Notas cadastradas:", notas)

def calcular_media():
    """
    Calcula a média aritmética de todas as notas cadastradas.
    
    Se não houver notas cadastradas, exibe uma mensagem informativa.
    
    Returns:
        float ou None: Retorna a média das notas se houver notas cadastradas,
                      ou None caso não haja notas.
    """
    if len(notas) == 0:
        print("Nenhuma nota cadastrada.")
        return None
    else:
        media = sum(notas) / len(notas)
        print("Média das notas:", media)
        return media

# Menu principal que fica repetindo até o usuário escolher sair
while True:
    # Exibe o cabeçalho e as opções do menu
    print("\n===== SISTEMA DE GERENCIAMENTO DE NOTAS =====")
    print("\nMenu:")
    print("1 - Adicionar nota")
    print("2 - Exibir notas")
    print("3 - Calcular média")
    print("0 - Sair")
    
    # Solicita a escolha do usuário
    opcao = input("\nEscolha uma opção: ")
    
    # Processa a opção escolhida
    if opcao == "1":
        # Adicionar nota
        try:
            nota = float(input("Digite a nota: "))
            adicionar_nota(nota)
            print("Nota adicionada com sucesso!")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
    
    elif opcao == "2":
        # Exibir notas
        exibir_notas()
    
    elif opcao == "3":
        # Calcular média
        calcular_media()
    
    elif opcao == "0":
        # Sair do programa
        print("Encerrando o sistema. Até logo!")
        break
    
    else:
        # Opção inválida
        print("Opção inválida. Por favor, escolha uma opção válida.")

