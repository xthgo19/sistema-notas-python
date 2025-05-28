# Lista vazia para guardar as notas
notas = []

# Função para adicionar nota na lista
def adicionar_nota(nota):
    notas.append(nota)

# Função para exibir todas as notas já cadastradas
def exibir_notas():
    print("Notas cadastradas:", notas)

# Função para calcular a média das notas
def calcular_media():
    if len(notas) == 0:
        print("Nenhuma nota cadastrada.")
    else:
        media = sum(notas) / len(notas)
        print("Média das notas:", media)

# Menu principal que fica repetindo até o usuário escolher sair
while True:
    print("\nMenu:")
    print("1 - Adicionar nota")
    print("2 - Exibir notas")
    print("3 - Calcular média")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nota = float(input("Digite a nota: "))
        adicionar_nota(nota)
    elif opcao == "2":
        exibir_notas()
    elif opcao == "3":
        calcular_media()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

