usuarios = ["ana", "", " ", "marcos", "julia123", "marcos@3", "Gabrielly 123"]
for usuario in usuarios:
    if not usuario:
        continue

    for letra in usuario:
        if letra.isspace():
            print(f"Ignorando '{usuario}', (contém espaços em branco).")
            break
            
        if not letra.isalpha():
            print(f"Ignorando '{usuario}', (contém caractéres especiais).")
            break
    else:
        print(f"Cadastrando usuário: {usuario}")