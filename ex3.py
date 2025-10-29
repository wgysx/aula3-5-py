inventario = ["sublime", "xenocaçador", "preludio", "kuronami"]

busca = input("Digite o item que deseja procurar no inventário: ")
for item in inventario:
    if item == busca:
        print(f"{busca.capitalize()} foi encontrada!")
        break
else:
    print(f"{busca.capitalize()} não está no inventário.")
